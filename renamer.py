import re
import hashlib
from pathlib import Path

def genHash():
    description = input("Describe your image briefly: ").strip().lower()
    while True:
        if not description:
            print("Description cannot be empty.")
        else:
            md5_hash = hashlib.md5(description.encode("utf-8")).hexdigest()
            print("MD5 hash generated.")
            return re.sub(r'[<>:"/\\|?*]', '', md5_hash)

def renameImage(finalName, file_path):
    try:
        file_path.rename(file_path.with_stem(finalName))
        print("The image has been renamed.")
    except PermissionError:
        print("Insufficient permissions, or the file is open.")
    except AttributeError as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    while True:
        raw_path = input("Enter the image path, or drag and drop it here: ").strip().strip("'").strip('"')
        file_path = Path(raw_path)

        if file_path.exists():
            finalName = genHash()
            answerRename = input(f"Would you like to rename the image to '{finalName}'? [Y/N]: ").strip().lower()
            if answerRename in ("y", "yes"):
                    renameImage(finalName, file_path)
            elif answerRename in ("n", "no"):
                    print("Process canceled.")
        else:
            print("Image/File path not found.")

        answerRA = input("Would you like to run again? [Y/N]: ")
        if answerRA in ("y", "yes"):
             continue
        else:
             print("Bye bye!")
             break