import os    
import sys

if __name__ == "__main__":
    target_dir = str(sys.argv[1])
    list_of_directories = os.listdir(target_dir)
    for directory in list_of_directories:
        path = os.path.join(target_dir, directory)
        if os.path.isdir(path):
            # get the size of the directory
            size = os.path.getsize(path)
            print(f"Directory: {path} - Size: {size} bytes")
        else:
            # get the size of the file
            size = os.path.getsize(path)
            print(f"File: {path} - Size: {size} bytes")
