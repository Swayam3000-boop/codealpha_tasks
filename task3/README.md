# 🐍 Task Automation with Python Scripts

A collection of three beginner-friendly Python scripts that automate small, repetitive real-world tasks using core Python libraries like `os`, `shutil`, `re`, and `requests`.

---

## 📁 Project Structure

python-task-automation/
├── move_jpg_files.py      # Moves all .jpg files to a new folder
├── extract_emails.py      # Extracts email addresses from a .txt file
├── scrape_title.py        # Scrapes and saves a webpage's title
└── README.md
---

## 📜 Scripts Overview

### 1. `move_jpg_files.py` — Move JPG Files
Scans a source folder, finds all `.jpg` files, and moves them into a destination folder. Creates the destination automatically if it doesn't exist.

**Concepts used:** `os`, `shutil`

### 2. `extract_emails.py` — Extract Email Addresses
Reads a `.txt` file containing mixed content, extracts all valid email addresses using regex, removes duplicates, and saves them to an output file.


**Concepts used:** `re`, file handling

### 3. `scrape_title.py` — Scrape Webpage Title
Sends an HTTP GET request to a URL, parses the HTML to find the `<title>` tag, and saves the result to a `.txt` file.

**Concepts used:** `requests`, `re`, file handling

---

## ⚙️ Requirements

- Python 3.x
- `requests` library (for Script 3 only)

Install dependencies:
```bash
pip install requests
```

---

## 🚀 How to Run

### Script 1 — Move JPG Files
Edit the `SOURCE` and `DESTINATION` variables, then run:
```bash
python move_jpg_files.py
```

### Script 2 — Extract Emails
Edit the `INPUT_FILE` and `OUTPUT_FILE` variables, then run:
```bash
python extract_emails.py
```

### Script 3 — Scrape Page Title
Edit the `TARGET_URL` and `OUTPUT_FILE` variables, then run:
```bash
python scrape_title.py
```

---

## 🧠 Key Concepts

| Library | Used For |
|---|---|
| `os` | Checking paths, listing directories |
| `shutil` | Moving files between folders |
| `re` | Regex pattern matching |
| `requests` | Making HTTP GET requests |
