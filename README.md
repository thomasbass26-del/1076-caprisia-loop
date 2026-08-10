# 1076 Caprisia Loop — Single-Property Listing Site

Maria Mendoza · MCMT Global Team · Coldwell Banker Sea Coast Advantage
Built by Triskope LLC

Live: https://thomasbass26-del.github.io/1076-caprisia-loop/

## Listing data
Sourced from mcmtglobal.com (MLS 2604463). $495,500 · 4 bed · 4 bath ·
2,908 heated sq ft · 3,608 total · 0.28 acres · built 2018 · Ranch · pond frontage.
Photos (68) are MCMT's own listing photos from their Luxury Presence CDN.

## Remaining setup
1. Set the form `action` to a Zapier catch hook that creates the lead in Follow Up Boss.
   Hidden fields already carry source, campaign, page URL, and referrer.
2. Optional: point a custom subdomain at this repo (add a CNAME file + DNS CNAME
   to thomasbass26-del.github.io), then update the canonical, OG, and JSON-LD URLs.
3. Re-verify price and status against CCAR MLS before any paid promotion.

## Structure
- `index.html` — entire site (CSS + JS inline)
- `assets/photos/` — 68 full-size images (max 1800px)
- `assets/thumbs/` — 68 thumbnails (max 700px)
- `assets/logo-dark.png` / `logo-light.png` — MCMT lockup
- `llms.txt`, `robots.txt`, `sitemap.xml` — AEO / crawler layer
