# Fight to Win Marriages

Website for Terrie Beeman's biblical marriage ministry. Hosted on Netlify (project `fight-to-win-marriages`).

## Editing

- Page content, metadata and schema live in `build.py`. Styles live in `site/assets/styles.css`.
- After editing `build.py`, regenerate the HTML and commit both:

  ```sh
  python3 build.py
  ```

- `site/` is the publish directory. Netlify deploys `main` to production and builds a Deploy Preview for every PR.
- Placeholders that still need Terrie's details are wrapped in `ph(...)` in `build.py` and render highlighted in yellow.

## Growth content

- Pain-point hubs live in `content/hubs.py`; blog posts in `content/posts_*.py`; the quiz, call recaps and the (currently unpublished) guide text in `content/resources.py`.
- Posts dated after today stay unpublished until a build on or after their date. `.github/workflows/publish-scheduled-posts.yml` rebuilds daily and commits `site/` when a post comes due. Override locally with `BUILD_DATE=2026-12-31 python3 build.py`.
- In body copy, `[[/path/|anchor]]` makes an internal link and falls back to plain text while the target post is unpublished.
- Set `GA_ID` in `build.py` to turn on GA4 plus lead events (form submits, Calendly, Zoom, quiz).
