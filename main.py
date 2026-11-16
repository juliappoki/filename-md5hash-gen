import re
from pathlib import Path
import hashlib

raw_path = input("Enter the image path, or drag and drop it here: ").strip().strip("'").strip('"')
file_path = Path(raw_path)
finalName = ""

def genHash():
    global finalName
    description = input("Describe your image briefly: ").strip().lower()
    while True:
        if not description:
            print("Description cannot be empty.")
        else:
            md5_hash = hashlib.md5(description.encode("utf-8")).hexdigest()
            finalName = re.sub(r'[<>:"/\\|?*]', '', md5_hash)
            print("MD5 hash generated.")
            break

def renameImage():
    global finalName
    global file_path
    try:
        file_path.rename(file_path.with_stem(finalName))
        print("The image has been renamed.")
    except PermissionError:
        print("Insufficient permissions, or the file is open.")
    except AttributeError:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    if file_path.exists():
        genHash()
        answer = input(f"Would you like to rename the image to '{finalName}'? [Y/N]: ").strip().lower()
        if answer in ("y", "yes"):
                renameImage()
        elif answer in ("n", "no"):
                print("Process canceled.")
    else:
        print("Image/File path not found.")