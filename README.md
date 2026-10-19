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
