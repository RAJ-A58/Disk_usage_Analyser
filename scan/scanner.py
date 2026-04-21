import os
from datetime import datetime
from database.operations import insert_file


def scan_folder(folder_path):
    file_count = 0
    skipped = 0

    if not os.path.exists(folder_path):
        print("Invalid path")         #To check for the path if exist
        return

    print("\nScanning started...\n")

    for root, dirs, files in os.walk(folder_path):  #os.walk() is a generator that yields a tuple (dirpath, dirnames, filenames) for each directory in the directory tree rooted at top (including top itself).
        for file in files:
            path = os.path.join(root, file)  #join folder + filename to get the full path of the file

            try:
                size = os.path.getsize(path) #extract size
                ext = os.path.splitext(file)[1]  #
                modified = datetime.fromtimestamp(os.path.getmtime(path))

                insert_file((file, size, ext, modified, path))
                file_count += 1

            except Exception as e:
                skipped += 1
                continue
    print("\nScan complete!")
    print(f"Files processed: {file_count}")
    print(f"Files skipped: {skipped}")