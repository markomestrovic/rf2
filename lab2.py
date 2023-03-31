import os
import pandas as pd
import hashlib
import magic
import mimetypes
# specify the directory path where the files are located
dir_path = 'Lab2_download_1'

# create an empty list to store the file names...
file_names = []
extensions = []
md5s=[]
sha1s=[]
sha256s=[]
magic_numbers=[]
extension_matches=[]

f= magic.Magic(uncompress=True,mime=True)

# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        name,extension=os.path.splitext(file)
        file_names.append(name)
        extensions.append(extension)
        md5s.append(hashlib.md5(file.encode('utf-8')).hexdigest()) 
        sha1s.append(hashlib.sha1(file.encode('utf-8')).hexdigest())
        sha256s.append(hashlib.sha256(file.encode('utf-8')).hexdigest())
        magic_number=f.from_file(os.path.join(dir_path,file))
        magic_numbers.append(magic_number)
        # check if the magic number contains the file extension
        if extension.lower() == '':
            extension_matches.append(False)
        elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
            extension_matches.append(True)
        else:
            extension_matches.append(False)

# create a Pandas dataframe with the file names
df = pd.DataFrame(
    {'file_name': file_names, 
     'extension': extensions, 
     'md5': md5s, 
     'sha1': sha1s, 
     'sha256': sha256s, 
     'magic': magic_numbers,
     'Extension_matches': extension_matches})

Target_hash= "c15e32d27635f248c1c8b66bb012850e5b342119"

# specify the directory path where the files are located
dir_path = 'Dokaz'

# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        name,extension=os.path.splitext(file)
        file_names.append(name)
        extensions.append(extension)
        md5s.append(hashlib.md5(file.encode('utf-8')).hexdigest()) 
        sha1s.append(hashlib.sha1(file.encode('utf-8')).hexdigest())
        sha256s.append(hashlib.sha256(file.encode('utf-8')).hexdigest())
        magic_number=f.from_file(os.path.join(dir_path,file))
        magic_numbers.append(magic_number)
        # check if the magic number contains the file extension
        if extension.lower() == '':
            extension_matches.append(False)
        elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
            extension_matches.append(True)
        else:
            extension_matches.append(False)

# create a Pandas dataframe with the file names
df = pd.DataFrame(
    {'file_name': file_names, 
     'extension': extensions, 
     'md5': md5s, 
     'sha1': sha1s, 
     'sha256': sha256s, 
     'magic': magic_numbers,
     'Extension_matches': extension_matches})

# print the dataframe
print(df)