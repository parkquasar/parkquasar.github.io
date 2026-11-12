# parkquasar.github.io

Personal page of Junsung Park. Plain HTML and CSS, no build step.

- `index.html`: all content. Each paper is one `<article class="pub">` card, newest first, under a year heading. First-author papers carry a "First author" tag.
- `assets/style.css`: layout, type, and colours.
- `assets/img/`: profile photo and one figure per paper (WebP).
- `Junsung_Park_CV.pdf`: replace this file when the CV changes.
- `assets/fonts/`: Source Serif 4 and Source Sans 3 (SIL Open Font License, see the licence files there).
- `tools/stamp_assets.py`: run it after changing any file under `assets/` or the CV. It adds a content hash to the links in `index.html`, so browsers fetch the new file instead of a cached copy.
