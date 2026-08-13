#!/usr/bin/env python3
"""
Exterior color grading for 1076 Caprisia Loop.

Legitimate post-processing only:
  - corrects the cold blue cast of winter light
  - deepens sky, water, and evergreen saturation
  - eases back the yellow-orange of dormant turf so it stops dominating
  - lifts shadows, adds a gentle contrast S-curve

NOTHING changes hue. Dormant grass stays dormant — it just recedes.
Originals are preserved in assets/photos_original/.
"""
import os, shutil
import numpy as np
from PIL import Image

SRC   = 'assets/photos'
ORIG  = 'assets/photos_original'
THUMB = 'assets/thumbs'

# Exterior frames only. Interiors are season-neutral and left untouched.
EXTERIOR = set(range(1, 9)) | set(range(25, 34)) | set(range(55, 69))

def rgb_to_hsv(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    df = mx - mn
    h = np.zeros_like(mx)
    m = df > 1e-6
    ri = m & (mx == r); gi = m & (mx == g); bi = m & (mx == b)
    h[ri] = (60 * ((g - b)[ri] / df[ri]) + 360) % 360
    h[gi] = (60 * ((b - r)[gi] / df[gi]) + 120) % 360
    h[bi] = (60 * ((r - g)[bi] / df[bi]) + 240) % 360
    s = np.where(mx > 1e-6, df / np.maximum(mx, 1e-6), 0)
    return h, s, mx

def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - np.abs(((h / 60.0) % 2) - 1))
    m = v - c
    z = np.zeros_like(h)
    i = (h / 60).astype(int) % 6
    r = np.select([i==0,i==1,i==2,i==3,i==4,i==5], [c,x,z,z,x,c])
    g = np.select([i==0,i==1,i==2,i==3,i==4,i==5], [x,c,c,x,z,z])
    b = np.select([i==0,i==1,i==2,i==3,i==4,i==5], [z,z,x,c,c,x])
    return np.stack([r+m, g+m, b+m], -1)

def bump(h, lo, hi, amt, feather=14):
    """Smooth per-hue weight, wrapping at 360."""
    d = np.minimum(np.abs(h - lo), 360 - np.abs(h - lo))
    d2 = np.minimum(np.abs(h - hi), 360 - np.abs(h - hi))
    inside = ((h >= lo) & (h <= hi)) if lo < hi else ((h >= lo) | (h <= hi))
    edge = np.minimum(d, d2)
    w = np.where(inside, 1.0, np.clip(1 - edge / feather, 0, 1))
    return 1.0 + (amt - 1.0) * w

def grade(path, out):
    im = Image.open(path).convert('RGB')
    a = np.asarray(im).astype(np.float32) / 255.0

    # 1. Warm the white balance — winter light runs cold and blue.
    a[..., 0] *= 1.045          # red up
    a[..., 2] *= 0.972          # blue down
    a = np.clip(a, 0, 1)

    h, s, v = rgb_to_hsv(a)

    # 2. Per-hue saturation.
    s *= bump(h, 185, 260, 1.30)   # sky + water  — deepen
    s *= bump(h,  75, 175, 1.26)   # pines, shrubs, live foliage — deepen
    s *= bump(h,  28,  62, 0.84)   # dormant turf — ease back, do not recolor
    s = np.clip(s, 0, 1)

    # 3. Lift shadows, gentle S-curve for contrast.
    v = np.clip(v, 0, 1)
    v = v + 0.045 * (1 - v) ** 2.2          # shadow lift
    v = np.clip(v, 0, 1)
    v = np.clip(v + 0.13 * np.sin(2 * np.pi * (v - 0.5)) * -1, 0, 1)  # S-curve
    v = np.clip(v * 1.015, 0, 1)            # tiny exposure nudge

    out_rgb = np.clip(hsv_to_rgb(h, s, v), 0, 1)
    Image.fromarray((out_rgb * 255).astype(np.uint8)).save(
        out, quality=86, optimize=True, progressive=True)

def main():
    if not os.path.isdir(ORIG):
        shutil.copytree(SRC, ORIG)
        print(f'originals backed up -> {ORIG}')

    done = 0
    for n in sorted(EXTERIOR):
        f = f'{n:02d}.jpg'
        src = os.path.join(ORIG, f)
        if not os.path.exists(src):
            continue
        grade(src, os.path.join(SRC, f))
        im = Image.open(os.path.join(SRC, f))
        im.thumbnail((700, 700), Image.LANCZOS)
        im.save(os.path.join(THUMB, f), quality=65, optimize=True)
        done += 1
    print(f'graded {done} exterior frames; interiors untouched')

if __name__ == '__main__':
    main()
