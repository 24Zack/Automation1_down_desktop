import os
import shutil

# Path 
downloads_path = os.path.expanduser("~/Downloads")

# Target folders
targets = {
    ".pdf": "PDF",
    ".heic": "HEIC"
}


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
