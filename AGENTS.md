# SoftwareByEugene website

This repository publishes `https://softwarebyeugene.com/` through GitHub Pages.
The canonical repository is `https://github.com/softwarebyeugene/softwarebyeugene.github.io`.

## Publishing

- The established deployment workflow is to commit the intended changes and push to `main`. GitHub Pages then builds and publishes the site automatically.
- Eugene explicitly authorizes this repository's ordinary Git push / GitHub Pages workflow as an exception to the general harness-only deployment guidance. Do not require a new harness capability or ask for a separate exception when Eugene requests publication here.
- A request such as “publish” authorizes the commit and push needed to publish the approved content. A request to update this repository's persistent guidance also authorizes committing and pushing that guidance so future checkouts receive it.
- Before pushing, inspect the remote, branch, working tree, and exact diff; preserve unrelated changes and run checks appropriate to the change. Do not force-push.
- After pushing, verify that the GitHub Pages “pages build and deployment” run for the exact pushed SHA finishes successfully. For public content changes, verify the intended HTTPS URL returns HTTP 200 and contains the approved content before reporting it live.
- Cloudflare may rewrite email links and inject its email-protection script. Verify the published policy text and intended behavior rather than requiring a byte-for-byte match with source HTML.
- This authorization covers the existing publishing workflow. Domain, DNS, repository access, hosting configuration, and destructive changes still require their own authorization.

## Content

- Keep approved copy as requested. Do not reintroduce draft banners, longer policy language, or internal review notes when publishing.
- HangTime's privacy page is `hangtime/privacy/index.html`, published at `https://softwarebyeugene.com/hangtime/privacy/`. Its approved policy is: “HangTime does not collect any personal data.”
