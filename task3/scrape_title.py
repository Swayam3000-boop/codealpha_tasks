"""
Task Automation - Script 3: Scrape the title of a fixed webpage and save it.
Concepts: requests, re, file handling
"""

import re
import requests

def scrape_and_save_title(url, output_file="page_title.txt"):
    """
    Fetches the HTML of the given URL, extracts the <title> tag content,
    and saves it to output_file.
    """
    print(f"[→] Fetching: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()           # Raise error for 4xx/5xx responses
        print(f"[✓] Status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("[✗] Error: Could not connect. Check your internet or URL.")
        return
    except requests.exceptions.Timeout:
        print("[✗] Error: Request timed out.")
        return
    except requests.exceptions.HTTPError as e:
        print(f"[✗] HTTP Error: {e}")
        return

    # Extract <title> using regex
    html = response.text
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)

    if not match:
        print("[-] No <title> tag found on this page.")
        return

    title = match.group(1).strip()
    # Clean up whitespace/newlines inside the title
    title = re.sub(r"\s+", " ", title)

    print(f"[✓] Title found: \"{title}\"")

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"URL   : {url}\n")
        f.write(f"Title : {title}\n")

    print(f"[✓] Saved to: '{output_file}'")


# ── Example Usage ──────────────────────────────────────────────
if __name__ == "__main__":
    TARGET_URL  = "https://www.wikipedia.org"  # Change to any public URL
    OUTPUT_FILE = "page_title.txt"

    scrape_and_save_title(TARGET_URL, OUTPUT_FILE)
