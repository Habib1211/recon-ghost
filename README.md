# Recon Phantom 👻
> One-click advanced recon automation tool for serious bug bounty hunters.  
Built by Muhammad Habib ⚔️

---

## 🔥 Features

-  Subdomain Enumeration (via `subfinder`)
-  Live Host Detection (via `httpx`)
-  URL Harvesting (`waybackurls`)
-  JavaScript Endpoints Extraction
-  Secrets & Token Detection
-  Passive Vulnerability Scanning (via `nuclei`)

---

## Dependencies

Make sure the following tools are installed and in `$PATH`:

- [`subfinder`](https://github.com/projectdiscovery/subfinder)
- [`httpx`](https://github.com/projectdiscovery/httpx)
- [`waybackurls`](https://github.com/tomnomnom/waybackurls)
- [`nuclei`](https://github.com/projectdiscovery/nuclei)
- `curl`, `grep`, `xargs`, `sort`, etc (default in Linux)

---

## Usage

```bash
git clone https://github.com/yourname/recon-phantom.git
cd recon-phantom

python3 recon-phantom.py -d example.com

 Output Structure
All output is saved in output/example.com_TIMESTAMP/
output/
└── example.com_20250713/
    ├── subdomains.txt
    ├── live.txt
    ├── urls.txt
    ├── urls-with-params.txt
    ├── js_endpoints.txt
    ├── secrets.txt
    └── passive-findings.txt
Future Upgrades (Planned)
 Module-based flags (--no-js, --only-passive)

 Active WAF bypass support

 JS parsing via LinkFinder or custom regex

 CDN + asset grouping

 HTML/Markdown Report generation

⚠️ Legal Disclaimer
Use this tool only for legal and ethical purposes. Always take permission before testing any website.

 Credit
Built with ❤️ by Muhammad Habib
Twitter: @0xHabib | GitHub: Habib1211
