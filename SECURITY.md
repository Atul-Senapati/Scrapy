# Security Policy

## Reporting a vulnerability

If you find a security issue in this project, please report it privately rather than opening a public issue.

Use GitHub's private reporting: open the repository's **Security** tab and choose **Report a vulnerability**
(https://github.com/Atul-Senapati/Scrapy/security/advisories/new).

Please include what you found, the steps to reproduce it, and the impact you expect. You can expect an initial reply within a few days.

## Scope

- The web UI in `frontend/` and the server in `serve.py`
- The deployment files (`Dockerfile`, `render.yaml`)
- The bundled scraper code, which comes from [omkarcloud/amazon-scraper](https://github.com/omkarcloud/amazon-scraper)

## Deployment notes

- The hosted demo has no login. Anyone with the link can use it. Add authentication before exposing it beyond a demo.
- If you set `AMAZON_PROXY`, keep the credentials in an environment variable and never commit them.
- Do not commit `.env` files or API keys.

## Responsible use

Scraping Amazon may be restricted by its terms of service and by local law on data scraping, copyright and privacy. You are responsible for using this software lawfully and ethically. The authors are not liable for misuse.

The software is provided "as is", without warranty of any kind, as described in the [MIT License](LICENSE).
