__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

# part 0
path = os.getcwd()
cache_path = os.path.join(path, "cache")
zip_file_path = os.path.join(path, "data.zip")
cache_dir_path = cache_path

# part 1
def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)   
    os.mkdir(cache_path)

# part 2
def cache_zip(zip_file_path : str, cache_dir_path : str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)

# part 3
def cached_files():
    os.chdir(cache_path)
    files_path = [os.path.abspath(x) for x in os.listdir(cache_path)]
    return files_path
 
# part 4
def find_password(files : list):
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines() 
            for line in lines:
                if line.find('password') >= 0:
                    words = line.split(" ")
# vond deze persoonlijk iets generieker (omdat je niet weet waar password staat, maar de opdracht wel deze tip geeft)                   
                    for word in words:              
                        if 'password' not in word:
                            return word 

if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_file_path, cache_dir_path)
    cached_files()
    print(find_password(cached_files()))
