import os    
import sys


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


if __name__ == "__main__":
    target_dir = str(sys.argv[1])
    list_of_directories = os.listdir(target_dir)
    for directory in list_of_directories:
        if directory == "soe":
            continue
        path = os.path.join(target_dir, directory)
        if os.path.isdir(path):
            # get the size of the directory
            try:
                size = get_size(path)
                print(f"Directory: {path} - Size: {size} bytes")
            except PermissionError:
                print(f"Permission denied: {path}")
            except FileNotFoundError:
                print(f"File not found: {path}")
        else:
            # get the size of the file
            try:
                size = os.path.getsize(path)
                print(f"File: {path} - Size: {size} bytes")
            except PermissionError:
                print(f"Permission denied: {path}")
            except FileNotFoundError:
                print(f"File not found: {path}")
