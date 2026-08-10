# 1076 Caprisia Loop — Single-Property Listing Site

MCMT Global Team · Coldwell Banker Sea Coast Advantage
Built by Triskope LLC

## Before publishing

1. **Verify every figure** against CCAR MLS. All numbers live in the `LISTING`
   object near the bottom of `index.html` and in the JSON-LD block. Aggregator
   sources disagreed on price and square footage.
2. Replace `REPLACE-WITH-DOMAIN` throughout `index.html`, `robots.txt`,
   and `sitemap.xml`.
3. Set the form `action` to the Zapier catch hook that creates the lead in
   Follow Up Boss.
4. Add MLS photos to `assets/` and list them in `LISTING.photos`, then set
   `emptySlots` to 0.
5. Confirm lat/lng from Google Maps.

## Deploy (GitHub Pages)

```bash
cd 1076-caprisia-loop
git init
git add -A
git commit -m "1076 Caprisia Loop listing site"
git branch -M main
git remote add origin https://github.com/<account>/1076-caprisia-loop.git
git push -u origin main
```

Then: repo → Settings → Pages → Source: `main` / `root`.

For a custom subdomain, add a `CNAME` file containing the hostname
(e.g. `1076caprisialoop.mcmtglobal.com`) and point a DNS CNAME record at
`<account>.github.io`.
