# Mobile UI and developer-menu fix

- Forces readable white input/select backgrounds and dark text on mobile and desktop.
- Improves mobile spacing and fixes dashboard metric contrast.
- Sets Streamlit client toolbar to minimal, hides top bar and disables detailed Python errors in the browser.
- Does not prevent Community Cloud host-controlled sleeping/error screens or guarantee that Fork links are absent from those screens.
- Test on a phone: login, registration, class selector, search boxes, materials search, password inputs, dropdown menus.
- Keep existing Neon secrets and database; never commit secrets.
- Deploy to a staging app first, then verify production after merging.
