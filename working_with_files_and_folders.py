import os

folder_path = 'some/path/to/folder'
file_name = 'file_name.extension'


#to check if file exists
os.path.exists(folder_path+'/'+file_name)

#check if it's really a file (or a folder)
os.path.isfile(folder_path+'/'+file_name)


#open, read, close text file
status_file = open(file_name, 'r')
file_txt = status_file.read()
status_file.close()



