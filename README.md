# deployboat.github.io

The website for [Deploy Boat](https://github.com/deployboat/deployboat), live at
**https://deployboat.github.io**.

It's one HTML page, no framework and no build step. Edit a file, push to `main`,
and GitHub Pages publishes it within a minute or two.

## What's in here

| File | What it's for |
|---|---|
| `index.html` | The whole site: text, styles and the few lines of JavaScript |
| `install.sh` | The short install address. It just runs the real installer from the main repo |
| `og.png` | The preview image people see when the link is shared |
| `apple-touch-icon.png`, `favicon-32.png`, `icon-512.png` | Icons for browsers and phones |
| `site.webmanifest` | Name and icons for "Add to home screen" |
| `robots.txt`, `sitemap.xml` | Help search engines find the page |
| `tools/og.py` | Draws `og.png` and the icons |
| `.nojekyll` | Tells GitHub Pages to serve the files exactly as they are |

## The short install command

```sh
curl -fsSL deployboat.github.io/install.sh | sudo bash
```

`install.sh` here is only a few lines: it downloads and runs
[the real installer](https://github.com/deployboat/deployboat/blob/main/install.sh)
from the main repo. So the short command always installs the latest version,
and nothing here needs to change when the installer does.

Please don't move or rename this file. The README, the site and people's notes all
point to it.

## Making changes

- **Text and layout:** edit `index.html`. Styles are at the top in one `<style>` block,
  with colors defined once in `:root` (light) and the dark mode block right below it.
- **Try it locally:** open `index.html` in a browser. Nothing to install.
- **Publish:** commit and push to `main`.

When you change the headline or the description, also update the social tags at the
top of `index.html` (`og:title`, `og:description`, `twitter:*`) and redraw the image.

## Redrawing the preview image

`og.png` is drawn by a small Python script instead of a design tool, so changing the
words is a quick edit. Keep them in step with the headline on the site. You need Python with [Pillow](https://pypi.org/project/pillow/) and two
free fonts in one folder:

- [Inter](https://fonts.google.com/specimen/Inter) as `inter-400.ttf`, `inter-600.ttf`, `inter-700.ttf`
- [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) as `mono-500.ttf`

Then, from this folder:

```sh
python3 tools/og.py /path/to/fonts .
```

It writes `og.png` and the icons. The text is near the top of `tools/og.py`.

Social sites cache previews. After changing the image, refresh it with Facebook's
Sharing Debugger or LinkedIn's Post Inspector.

## Feedback

Spotted a typo or something unclear? [Open an issue](https://github.com/deployboat/deployboat/issues)
in the main repo.
