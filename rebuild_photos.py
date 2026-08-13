#!/usr/bin/env python3
"""Rebuild the 1076 Caprisia gallery from the photographer's print originals.

Source : ~/Downloads/1076-caprisia-lp-myrtle-beach-sc-29579/images-for-printing
         3000x2000 originals, photographer's running order in the filename prefix.
         " Tag" variants are the same frames with a red map-pin overlay — excluded.
Output : assets/photos  (2000px, q87)  +  assets/thumbs (700px, q66)
No colour grading. Resize and encode only.
"""
import os, re, glob, shutil
from PIL import Image

SRC   = os.path.expanduser('~/Downloads/1076-caprisia-lp-myrtle-beach-sc-29579/images-for-printing')
REPO  = os.path.expanduser('~/projects/1076-caprisia-loop')
PHOTO = os.path.join(REPO, 'assets/photos')
THUMB = os.path.join(REPO, 'assets/thumbs')

def order_key(p):
    m = re.match(r'(\d+)-print-', os.path.basename(p))
    return int(m.group(1)) if m else 9999

files = [f for f in glob.glob(os.path.join(SRC, '*.jpg')) if ' Tag' not in os.path.basename(f)]
files.sort(key=order_key)
print(f'{len(files)} clean frames found')

for d in (PHOTO, THUMB):
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)

for i, f in enumerate(files, 1):
    n = f'{i:02d}.jpg'
    im = Image.open(f).convert('RGB')
    full = im.copy(); full.thumbnail((2000, 2000), Image.LANCZOS)
    full.save(os.path.join(PHOTO, n), quality=87, optimize=True, progressive=True)
    th = im.copy(); th.thumbnail((700, 700), Image.LANCZOS)
    th.save(os.path.join(THUMB, n), quality=66, optimize=True)
    if i <= 3 or i == len(files):
        print(f'  {n}  <- {os.path.basename(f)}  {full.size}')

print('done')
