# Notes on apple-app-site-association

This folder contains the `apple-app-site-association` file required for iOS Universal Links to work with the Jigsaw app (`DVFZGL7K36.com.softwarebyeugene.Jigsaw`).

## ⚠️ Important: MIME Type Fix via Cloudflare

GitHub Pages does **not** serve this file with the correct `Content-Type: application/json`, which iOS requires. To fix this:

- A **Cloudflare Worker** was deployed to intercept requests to:

  ```
  /.well-known/apple-app-site-association
  /apple-app-site-association
  ```

- The Worker proxies the request to GitHub Pages and forces the correct MIME type and caching headers:

  ```js
  addEventListener('fetch', event => {
    const url = new URL(event.request.url);
    if (url.pathname === '/.well-known/apple-app-site-association'
     || url.pathname === '/apple-app-site-association') {
      return event.respondWith(
        fetch('https://softwarebyeugene.github.io/.well-known/apple-app-site-association')
          .then(resp => new Response(resp.body, {
            status: resp.status,
            headers: {
              'Content-Type': 'application/json',
              'Cache-Control': 'max-age=600'
            }))
      );
    }
    return event.respondWith(fetch(event.request));
  });
  ```

## ✍️ Reminder for future updates

- If this file is changed, **no additional deployment is needed** unless the file URL or domain changes.
- The Worker simply proxies the raw file from GitHub — make sure the JSON stays valid and updated.
