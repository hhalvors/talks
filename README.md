# Talks

Slides from talks by Hans Halvorson: the source (Beamer, Markdown for
[nordisk](https://github.com/hhalvors/nordisk), or Quarto) and the PDF for each
talk. Feel free to re-use them. The list of talks, with dates and venues, is at
<https://hanshalvorson.com/talks.html>.

## Layout

One folder per talk, named by its `id` in the website's catalog
(`hhalvors.github.io/data/talks-master.yaml`), which links to the files here.

    pittsburgh2026/
      pittsburgh2026.md     source
      pittsburgh2026.pdf    slides

## Not in the repository

- Photographs and scans (`*.jpg`, `*.png`, …) and PowerPoint files are kept
  locally for building the slides but are not committed: many are third-party
  material. The PDFs include them.
- Speaker notes: a nordisk deck is published without its `::: notes` blocks;
  the full version is kept locally as `<name>.md.with-notes`.
- Older versions of a file found elsewhere on disk are kept locally as
  `<name>.local-YYYY-MM-DD`.

## Adding a talk

1. Make a folder named after the talk's `id` in `talks-master.yaml`.
2. Put the source and the PDF in it.
3. In `talks-master.yaml`, set `web: true` and add links of the form
   `https://github.com/hhalvors/talks/blob/main/<id>/<file>`.
