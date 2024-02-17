import os    

if __name__ == "__main__":
    current_directory = os.getcwd()
    list_of_directories = os.listdir(current_directory)
    for directory in list_of_directories:
        path = os.path.join(current_directory, directory)
        if os.path.isdir(path):
            # get the size of the directory
            size = os.path.getsize(path)
            print(f"Directory: {path} - Size: {size} bytes")
        else:
            # get the size of the file
            size = os.path.getsize(path)
            print(f"File: {path} - Size: {size} bytes")
