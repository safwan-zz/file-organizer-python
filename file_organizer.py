import os
import shutil
import time

# Getting the path
path = input('Enter your folder path = ')

if not os.path.exists(path):
    print('Invalid path')
    exit()
time.sleep(10)

if not os.path.isdir(path):
    print('Not a folder')
    exit()
time.sleep(10)

files = os.listdir(path)

for file in files:
    # Skip directories
    if os.path.isdir(os.path.join(path, file)):
        continue
    
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # remove the dot

    if extension == "":
        extension = "no_extension"  # for files without extension

    # Create a folder for this extension if it doesn't exist
    folder_path = os.path.join(path, extension)
    if not os.path.exists(folder_path):
        os.mkedirs(folder_path)

    # Move the file into the folder
    src_file = os.path.join(path, file)
    dest_file = os.path.join(folder_path, file)
    shutil.move(src_file, dest_file)

print("Files have been organized by extension.")
time.sleep(10)
