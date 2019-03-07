'''
Common file handling operations in Python
for quick reference
'''

import os
import shutil

folder_path = 'some/path/to/folder'
file_name = 'file_name.extension'


#list files inside a directory
os.listdir(folder_path)

#join file name with folder name
os.path.join(folder_path, file_name)

#to check if file exists
os.path.exists(folder_path+'/'+file_name)

#check if it's really a file (or a folder)
os.path.isfile(folder_path+'/'+file_name)


#open, read, close text file
status_file = open(file_name, 'r')
file_txt = status_file.read()
status_file.close()


#rename or move a file
old_location = 'old/folder/old_file.ext'
new_location = 'new/folder/new_file.ext'

shutil.move(old_location, new_location)


#delete a file
os.unlink(folder_path+file_name)

#delete file recursively
#first check if file is a directory, then remove all contents within it
if os.path.isdir(folder_path):
    shutil.rmtree(folder_path)


