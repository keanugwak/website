# Gemini Proxy Setup

`gemini-proxy.js` keeps the Gemini API key server-side so it's never exposed
in the browser/source code (the previous hardcoded key was auto-revoked by
Google after being detected as leaked).

## Setup on Netlify

1. Generate a new key at https://aistudio.google.com/apikey
2. In the Netlify dashboard: **Site settings → Environment variables**
   → add `GEMINI_API_KEY` = `<your key>`
3. Deploy. `BrainDump.html` calls `/api/gemini`, which `netlify.toml`
   redirects to this function.

## Local development

The plain `python -m http.server` setup (`.claude/launch.json`) does **not**
run Netlify functions, so `/api/gemini` will 404 locally. To test the full
flow locally, use the Netlify CLI instead:

```
npm install -g netlify-cli
netlify dev
```

This serves the site and runs the function together. Create a `.env` file
(gitignored) in the project root with:

```
GEMINI_API_KEY=your-key-here
```
