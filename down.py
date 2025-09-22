import os
import shutil

# Path to your Downloads
downloads_path = os.path.expanduser("~/Downloads")

# Target folders
targets = {
    ".pdf": "PDF",
    ".heic": "HEIC"
}

# Loop through files in the Downloads
for filename in os.listdir(downloads_path):
    full_path = os.path.join(downloads_path, filename)

    if os.path.isfile(full_path):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in targets:
            target_folder = os.path.join(downloads_path, targets[ext])
        else:
            target_folder = os.path.join(downloads_path, "Others")

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(full_path, os.path.join(target_folder, filename))

print("Files sorted successfully!")

# Note: This script assumes that the target folders (PDF, HEIC, Others) do not already exist.