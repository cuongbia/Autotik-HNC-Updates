"""Byte-exact release delta; apply uses only standard-library file operations."""
import hashlib
import json
from pathlib import Path
import shutil
import struct
import sys
import zipfile


def digest(path):
    with Path(path).open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def pack(baseline, target, destination):
    from PyInstaller.archive.readers import CArchiveReader
    old, new = CArchiveReader(str(baseline)), CArchiveReader(str(target))
    old_pyz, new_pyz = old.open_embedded_archive('PYZ.pyz'), new.open_embedded_archive('PYZ.pyz')
    parts = []
    cursor = 0
    with Path(baseline).open('rb') as before, Path(target).open('rb') as after, zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as bundle:
        def patch(position, length):
            nonlocal cursor
            assert cursor == position
            after.seek(position)
            name = f'blocks/{len(parts):05d}'
            bundle.writestr(name, after.read(length))
            parts.append(['patch', name, length])
            cursor += length

        def copy(position, old_position, length):
            nonlocal cursor
            assert cursor == position
            parts.append(['copy', old_position, length])
            cursor += length

        patch(0, new._start_offset)
        for name, (offset, length, *unused) in new.toc.items():
            position = new._start_offset+offset
            if not length:
                continue
            if name == 'PYZ.pyz':
                patch(position, 16)
                for module, (kind, start, size) in new_pyz.toc.items():
                    if not size:
                        continue
                    prev = old_pyz.toc.get(module)
                    if prev and prev[2] == size:
                        before.seek(old_pyz._start_offset+prev[1]);after.seek(new_pyz._start_offset+start)
                        same = before.read(size) == after.read(size)
                    else:
                        same = False
                    if same:
                        copy(position+start, old_pyz._start_offset+prev[1], size)
                    else:
                        patch(position+start, size)
                patch(cursor, position+length-cursor)
            else:
                prev = old.toc.get(name)
                if prev and prev[1] == length:
                    before.seek(old._start_offset+prev[0]);after.seek(position)
                    same = before.read(length) == after.read(length)
                else:
                    same = False
                if same:
                    copy(position, old._start_offset+prev[0], length)
                else:
                    patch(position, length)
        patch(cursor, Path(target).stat().st_size-cursor)
        metadata = dict(schema=1, baseline_sha256=digest(baseline), target_sha256=digest(target),
                        target_size=Path(target).stat().st_size, parts=parts)
        bundle.writestr('delta.json', json.dumps(metadata, separators=(',', ':')))
    print(json.dumps({'delta_size':Path(destination).stat().st_size,'target_sha256':metadata['target_sha256']}))


def apply(baseline, delta, target):
    baseline, target = Path(baseline), Path(target)
    if baseline.resolve() == target.resolve():
        raise ValueError('Delta output must not replace baseline.')
    with zipfile.ZipFile(delta) as bundle:
        metadata = json.loads(bundle.read('delta.json'))
        if metadata['schema'] != 1 or digest(baseline) != metadata['baseline_sha256']:
            raise ValueError('Incorrect baseline release.')
        parts = metadata['parts']
        if len(parts) > 20000 or sum(p[2] for p in parts) != metadata['target_size'] or metadata['target_size'] > 500_000_000:
            raise ValueError('Invalid delta size.')
        with baseline.open('rb') as source, target.open('wb') as output:
            for kind, reference, length in parts:
                if length < 0:
                    raise ValueError('Invalid delta segment.')
                if kind == 'copy':
                    source.seek(reference)
                    remaining = length
                    while remaining:
                        chunk = source.read(min(remaining, 1024*1024))
                        if not chunk:
                            raise ValueError('Truncated baseline.')
                        output.write(chunk);remaining -= len(chunk)
                elif kind == 'patch':
                    data = bundle.read(reference)
                    if len(data) != length:
                        raise ValueError('Invalid patch block.')
                    output.write(data)
                else:
                    raise ValueError('Unknown delta segment.')
    if digest(target) != metadata['target_sha256']:
        target.unlink(missing_ok=True)
        raise ValueError('Reconstructed executable hash mismatch.')
    print('Verified release executable:', metadata['target_sha256'])


if __name__ == '__main__':
    if len(sys.argv) != 5 or sys.argv[1] not in {'pack', 'apply'}:
        raise SystemExit('Usage: release_delta.py pack|apply BASELINE TARGET_OR_DELTA OUTPUT')
    (pack if sys.argv[1] == 'pack' else apply)(*sys.argv[2:])
