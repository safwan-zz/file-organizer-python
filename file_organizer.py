import os
import shutil
# getting the path
path = input('Enter your folder path = ')
# checking if the path exists
if not os.path.exists(path):
    print('Path does not exist')
    exit()
#checking if a folder exists in the path
if not os.path.isdir(path):
    print('Path is not a directory')
    exit()

# getting files from the folder
files = os.listdir(path)
for file in files:
# splitting filename and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1: ]
# for no extension files
    if extension == "":
        extension = 'No extension'
# creating folders for each file type
    folder_path = os.path.join(path, extension)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
# moving files to the created folders
    src_path = os.path.join(path, file)
    dist_path = os.path.join(folder_path, file )
    shutil.move(src_path, dist_path)




















