"""
Task Automation - Script 2: Extract all email addresses from a .txt file and save them.
Concepts: re, file handling
"""

import re

def extract_emails(input_file, output_file):
    """
    Reads input_file, finds all valid email addresses using regex,
    removes duplicates, and saves them to output_file (one per line).
    """
    # Regex pattern for standard email addresses
    email_pattern = re.compile(
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    )

    # Read source file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"[✓] Read file: '{input_file}'")
    except FileNotFoundError:
        print(f"[✗] File not found: '{input_file}'")
        return

    # Find all emails and remove duplicates (preserve order)
    found = email_pattern.findall(content)
    unique_emails = list(dict.fromkeys(found))  # dedup while keeping order

    if not unique_emails:
        print("[-] No email addresses found.")
        return

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_emails) + "\n")

    print(f"[✓] Found {len(unique_emails)} unique email(s).")
    print(f"[✓] Saved to: '{output_file}'")
    print("\nEmails extracted:")
    for email in unique_emails:
        print(f"   • {email}")


# ── Example Usage ──────────────────────────────────────────────
if __name__ == "__main__":
    INPUT_FILE  = "contacts.txt"        # Source .txt file with mixed content
    OUTPUT_FILE = "extracted_emails.txt" # Output: one email per line

    extract_emails(INPUT_FILE, OUTPUT_FILE)
