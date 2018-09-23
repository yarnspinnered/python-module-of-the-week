import glob
import os
import shutil
import pathlib

toy = pathlib.Path.home() / '1'

print('BEFORE:', glob.glob('shutil_copy*'))
#destination is a file
shutil.copy('shutil_copy', 'shutil_copy2')
print('AFTER:', glob.glob('shutil_copy*'))

print('======COPYING TO A FOLDER ======')
print('BEFORE:', glob.glob('shutil_copy*'))
# use copy if the destination is a folder
shutil.copy('shutil_copy', 'shutil_copy_folder')
print('AFTER:', glob.glob('*', recursive=True))

print('======FINDING DISK INFO=======')
total_b, used_b, free_b = shutil.disk_usage('/')
gigabyte = 10 ** 9
print("Total: {:6.2f} GB Free: {:6.2f} GB Used: {:6.2f} GB".format(total_b/gigabyte, free_b/gigabyte, used_b/gigabyte))

print('======copying directory=======')
#copytree copies everything recursively, destination must not exist
shutil.copytree('shutil_copy_folder', 'shutil_copy_folder2', ignore=shutil.ignore_patterns('*.py'))

print('======removing directory=======')
shutil.rmtree('shutil_copy_folder2')

print('======finding which file gets called when command is passed=======')
print(shutil.which('virtualenv'))
print(shutil.which('python'))

print('=======walking within a folder to find all matching=======')
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('py'):
            print(file)