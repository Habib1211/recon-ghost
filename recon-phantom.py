#!/usr/bin/env python3

import os
import subprocess
import argparse
from datetime import datetime

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running: {cmd}\n{e}")

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def recon_phantom(domain):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base_path = f"output/{domain}_{timestamp}"
    create_folder(base_path)

    print(f"[+] Starting recon on: {domain}")

    # 1. Subdomain Enumeration
    print("[+] Running subdomain enumeration...")
    run_cmd(f"subfinder -d {domain} -silent > {base_path}/subdomains.txt")

    # 2. Live Host Check
    print("[+] Checking for live hosts...")
    run_cmd(f"cat {base_path}/subdomains.txt | httpx -silent > {base_path}/live.txt")

    # 3. URL Harvesting
    print("[+] Harvesting URLs...")
    run_cmd(f"cat {base_path}/live.txt | waybackurls > {base_path}/urls.txt")
    run_cmd(f"cat {base_path}/urls.txt | grep '=' | sort -u > {base_path}/urls-with-params.txt")

    # 4. JS Endpoints & Secrets
    print("[+] Extracting JS endpoints...")
    run_cmd(f"cat {base_path}/urls.txt | grep '.js' | uniq > {base_path}/js_endpoints.txt")

    print("[+] Searching for tokens/secrets...")
    run_cmd(f"cat {base_path}/js_endpoints.txt | xargs -I {{}} curl -s {{}} | grep -Eo '(AIza[0-9A-Za-z-_]{35}|[a-zA-Z0-9_\-]{25,})' | sort -u > {base_path}/secrets.txt")

    # 5. Passive Vulnerability Scan
    print("[+] Running passive nuclei scan...")
    run_cmd(f"cat {base_path}/live.txt | nuclei -silent -t ~/nuclei-templates/ -es info,unknown -o {base_path}/passive-findings.txt")

    print(f"[+] Recon completed. Results saved in: {base_path}")

def main():
    parser = argparse.ArgumentParser(description="Recon Phantom - One click advanced recon tool")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    args = parser.parse_args()

    recon_phantom(args.domain)

if __name__ == "__main__":
    main()

