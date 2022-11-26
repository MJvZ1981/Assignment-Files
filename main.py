__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

# part 1
path = os.getcwd()
cache_path = os.path.join(path, "files", "cache")

def clean_cache():
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    else:
        shutil.rmtree(cache_path)
        os.mkdir(cache_path)
    for file in os.listdir(cache_path):
        file_path = os.path.join(cache_path, file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

clean = (clean_cache())

# part 2
def cache_zip(zip_file_path : str, cache_dir_path : str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)

cache_zip(zip_file_path = path + '\\files\\data.zip', cache_dir_path = cache_path)

# part 3
def cached_files():
    os.chdir(cache_path)
    files_path = [os.path.abspath(x) for x in os.listdir(cache_path)]
    return files_path

files = cached_files()
 
# part 4
def find_password(files : list):
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines() 
            for line in lines:
                if line.find('password') >= 0:
                    return line

password = find_password(files)
print(password)
