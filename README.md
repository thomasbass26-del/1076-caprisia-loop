# 1076 Caprisia Loop — Single-Property Listing Site

Maria Mendoza · MCMT Global Team · Coldwell Banker Sea Coast Advantage
Built by Triskope LLC · https://thomasbass26-del.github.io/1076-caprisia-loop/

## Media
- 77 photographs, from the photographer's 3000px print originals, served at 2000px
- Video: hero loop (silent, 8s), full tour (71s), vertical tour (46s) — encoded from
  the branded 1080p masters supplied in the photographer package

## Remaining setup
1. Set the form `action` to a Zapier catch hook that creates the lead in Follow Up Boss.
2. Confirm the open house date/time against CCAR MLS (banner + Event schema).
3. Optional: point a subdomain at this repo. Add a CNAME file ONLY after the DNS
   record exists and resolves — adding it early breaks the github.io URL.

## Structure
- `index.html` — entire site, CSS and JS inline
- `assets/photos/` `assets/thumbs/` — 77 frames each
- `assets/video/` — hero loop, tour, vertical tour, posters
- `llms.txt`, `robots.txt`, `sitemap.xml` — AEO / crawler layer
