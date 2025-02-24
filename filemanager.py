import os, shutil

path = r"A:/Files"
file_name = os.listdir(path)

folder_names = ['/csv files', '/image files', '/text files', '/ms files']

##Fixed
for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        print ((path + folder_names[loop]))
        os.makedirs(path + folder_names[loop])


for file in file_name:
    if '.csv' in file and not os.path.exists(path + '/csv files' + file):
        shutil.move(path + file, path + '/csv files' + file)