import os

DIRECTORY = "D:/Photos"

def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)

def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


