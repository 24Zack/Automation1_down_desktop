import os
import shutil

# Path to your Desktop
desktop_path = os.path.expanduser("~/Desktop")

# Target folders
targets = {
    ".pdf": "PDF",
    ".heic": "HEIC"
}

# Loop through files on the Desktop
for filename in os.listdir(desktop_path):
    full_path = os.path.join(desktop_path, filename)

    if os.path.isfile(full_path):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in targets:
            target_folder = os.path.join(desktop_path, targets[ext])
        else:
            target_folder = os.path.join(desktop_path, "Others")

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(full_path, os.path.join(target_folder, filename))

print("Files sorted successfully!")
