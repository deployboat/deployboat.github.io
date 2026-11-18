# Draws the social preview image (1200x630) and app icons for the Deploy Boat site.
# Needs Pillow and these free (OFL) fonts in one folder:
#   inter-400.ttf, inter-600.ttf, inter-700.ttf (Inter), mono-500.ttf (JetBrains Mono)
# Run:  python3 tools/og.py <fonts-folder> .
import sys
from PIL import Image, ImageDraw, ImageFont

FONTS, OUT = sys.argv[1], sys.argv[2]
K = 2  # draw at 2x, then shrink: smooth edges
W, H = 1200 * K, 630 * K
# Same colors as the site
BG, INK, MUTED, LINE, CODE = "#fbfbf9", "#1a1a1a", "#6b6b6b", "#e6e4df", "#1c1c1e"
RAINBOW = ["#2457d6", "#8b5cf6", "#ec4899", "#f59e0b", "#10b981"]

def font(name, size):
    return ImageFont.truetype(f"{FONTS}/{name}.ttf", size * K)

def boat(d, x, y, s, ink=INK):
    # the logo: mast, blue sail, hull (on a 32x32 grid)
    p = lambda pts: [(x + a * s / 32, y + b * s / 32) for a, b in pts]
    d.line(p([(16, 4), (16, 22)]), fill=ink, width=max(2, int(2 * s / 32)))
    d.polygon(p([(17, 5), (26, 19), (17, 19)]), fill="#2457d6")
    d.polygon(p([(5, 23), (27, 23), (23, 28), (9, 28)]), fill=ink)

def lerp(c1, c2, t):
    a, b = [int(c1[i:i + 2], 16) for i in (1, 3, 5)], [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

def rainbow_text(img, xy, text, f):
    # Text filled with a left-to-right rainbow, like the site's moving gradient.
    x, y = xy
    l, t, r, b = ImageDraw.Draw(img).textbbox((x, y), text, font=f)
    w, h = r - l, b - t
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((x - l, y - t), text, font=f, fill=255)
    grad = Image.new("RGB", (w, h))
    gd = ImageDraw.Draw(grad)
    for i in range(w):
        pos = i / max(1, w - 1) * (len(RAINBOW) - 1)
        j = min(int(pos), len(RAINBOW) - 2)
        gd.line([(i, 0), (i, h)], fill=lerp(RAINBOW[j], RAINBOW[j + 1], pos - j))
    img.paste(grad, (l, t), mask)

def fit(text, name, size, maxw):
    # Largest size (down to 70%) at which `text` fits in `maxw`.
    s = size
    while s > size * 0.7 and font(name, s).getlength(text) > maxw:
        s -= 1
    return font(name, s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
pad = 80 * K
inner = W - 2 * pad

# Logo
boat(d, pad, 58 * K, 40 * K)
d.text((pad + 52 * K, 63 * K), "Deploy Boat", font=font("inter-700", 28), fill=INK)

# Headline, same words as the site
lines = ["Put your apps on your own server,", "without becoming a sysadmin."]
hf = fit(lines[0], "inter-700", 58, inner)
for i, line in enumerate(lines):
    d.text((pad, (150 + i * 70) * K), line, font=hf, fill=INK)

# The feature that sets it apart
rainbow_text(img, (pad, 310 * K), "You won't need the docs.", font("inter-700", 34))

# Install box, like on the site: title bar + command
bx, by, bw, bh = pad, 384 * K, inner, 118 * K
d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=14 * K, fill=CODE)
d.line((bx, by + 40 * K, bx + bw, by + 40 * K), fill="#2a2a2c", width=K)
d.text((bx + 20 * K, by + 11 * K), "Install on your server", font=font("inter-400", 17), fill="#8b8b90")
cmd = "curl -fsSL deployboat.github.io/install.sh | sudo bash"
mono = fit("$  " + cmd, "mono-500", 27, bw - 44 * K)
d.text((bx + 22 * K, by + 60 * K), "$", font=mono, fill="#5fd38d")
d.text((bx + 22 * K + mono.getlength("$  "), by + 60 * K), cmd, font=mono, fill="#e8e8e8")

# Footer line
d.line((pad, 548 * K, W - pad, 548 * K), fill=LINE, width=2 * K)
d.text((pad, 566 * K), "deployboat.github.io", font=font("inter-600", 22), fill=INK)
d.text((W - pad, 566 * K), "Free & open source · MIT", font=font("inter-400", 22), fill=MUTED, anchor="ra")

img.resize((1200, 630), Image.LANCZOS).save(f"{OUT}/og.png", optimize=True)

# App / bookmark icons: the boat on a soft square.
for size, name in [(180, "apple-touch-icon.png"), (512, "icon-512.png"), (32, "favicon-32.png")]:
    S = size * 4
    ic = Image.new("RGB", (S, S), "#eef3ff")
    boat(ImageDraw.Draw(ic), S * 0.14, S * 0.12, S * 0.72)
    ic.resize((size, size), Image.LANCZOS).save(f"{OUT}/{name}", optimize=True)
print("ok")
