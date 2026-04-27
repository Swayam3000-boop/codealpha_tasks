"""
Task Automation - Script 1: Move all .jpg files from a folder to a new folder.
Concepts: os, shutil
"""

import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all .jpg files from source_folder to destination_folder.
    Creates destination_folder if it doesn't exist.
    """
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"[+] Created destination folder: '{destination_folder}'")

    # List all files in source folder
    all_files = os.listdir(source_folder)
    jpg_files = [f for f in all_files if f.lower().endswith('.jpg')]

    if not jpg_files:
        print("[-] No .jpg files found in the source folder.")
        return

    moved_count = 0
    for filename in jpg_files:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)

        # Handle filename conflicts
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            dest_path = os.path.join(destination_folder, f"{base}_copy{ext}")

        shutil.move(source_path, dest_path)
        print(f"[✓] Moved: {filename}")
        moved_count += 1

    print(f"\n✅ Done! {moved_count} file(s) moved to '{destination_folder}'.")


# ── Example Usage ──────────────────────────────────────────────
if __name__ == "__main__":
    SOURCE      = "my_photos"          # Folder containing .jpg files
    DESTINATION = "my_photos/jpg_only" # New folder to move them into

    move_jpg_files(SOURCE, DESTINATION)
