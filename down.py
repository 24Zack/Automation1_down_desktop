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


for filename in os.listdir(DOWNLOAD_PATH):
    FullPathFile = os.path.join(DOWNLOAD_PATH, filename)

    if os.path.isfile(FullPathFile):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in targets:
            if ext == ".py":
                target_folder = os.path.join(DOWNLOAD_PATH, "Others", targets[ext])
            elif ext == ".r":
                target_folder = os.path.join(DOWNLOAD_PATH, "Others", targets[ext])
            elif ext == ".c":
                target_folder = os.path.join(DOWNLOAD_PATH, "Others", targets[ext])
            elif ext == ".pptx":
                target_folder =  os.path.join(DOWNLOAD_PATH, "Others", targets[ext])
            else:
                target_folder = os.path.join(DOWNLOAD_PATH, targets[ext])
        else:
            target_folder = os.path.join(DOWNLOAD_PATH, "Others")

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(FullPathFile, os.path.join(target_folder, filename))

print("Files sorted successfully!")
