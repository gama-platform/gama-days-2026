# GAMA Days 2026

Source website for the GAMA Days 2026 conference, built with [Astro](https://astro.build).

## Editing content

The site is intentionally just two pages. Each lives in `src/pages/` as a
Markdown file — edit the file, the shared navbar/footer/hero come from
`src/layouts/PageLayout.astro` automatically, no need to touch HTML.

| Page | File |
|---|---|
| Home (dates, Call for Papers, link to the previous edition) | `src/pages/index.md` |
| Committee | `src/pages/committee.md` |

Each file starts with frontmatter (title, hero text, optional image/buttons),
followed by the page content in Markdown. `index.md` also has a `<div
class="key-dates">` block near the top for the three key-date stats — copy
that block's markup if you need to change the dates, and a `<ol class="steps">`
block for the numbered "How to submit" list.

Program, Keynotes, Register and Open Fora were dropped since they had no real
content yet — add them back as new files in `src/pages/` (and a nav entry in
`Navbar.astro`) once there's something real to put on them.

Shared chrome (navbar links, footer) lives in `src/components/Navbar.astro`
and `src/components/Footer.astro` — edit navigation **there only**, once, and
every page picks it up automatically.

## Running it

```sh
npm install
npm run dev      # local dev server
npm run build    # static output into dist/
npm run preview  # serve the built output
```

## Deployment

The site is served from `gama-platform.org/gama-days-2026/`, so
`astro.config.mjs` sets `base: '/gama-days-2026'`. `.github/workflows/deploy.yml`
builds the site and deploys it to GitHub Pages on every push to `main`.

**This requires the repository's Pages source to be set to "GitHub Actions"**
(Settings → Pages → Build and deployment → Source), since it currently deploys
directly from the `main` branch.

Old `.html` URLs from the previous multi-page site (`CFP.html`,
`CFParticipation.html`, `program.html`, `keynotes.html`, `openfora.html`,
`committee.html`) redirect to their new home, via the `redirects` config in
`astro.config.mjs`, so existing links keep working.
