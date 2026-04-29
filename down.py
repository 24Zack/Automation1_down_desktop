import os
import shutil

# Path 
DOWNLOAD_PATH = os.path.expanduser("~/Downloads")

# Target folders
targets = {
    ".pdf": "PDF",
    ".heic": "HEIC",
    ".py" : "PYTHON",
    ".r": "RStudio",
    ".c": "C_programming",
    ".pptx": "Powerpoints"
}

OTHERS_EXTS = {".py", ".r", ".c", ".pptx"}

for filename in os.listdir(DOWNLOAD_PATH):
    FullPathFile = os.path.join(DOWNLOAD_PATH, filename)

    if os.path.isfile(FullPathFile):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in targets:
            if ext in OTHERS_EXTS:
                target_folder = os.path.join(DOWNLOAD_PATH, "Others", targets[ext])
            else:
                target_folder = os.path.join(DOWNLOAD_PATH, targets[ext])
        else:
            target_folder = os.path.join(DOWNLOAD_PATH, "Others")

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(FullPathFile, os.path.join(target_folder, filename))

print("Files sorted successfully!")