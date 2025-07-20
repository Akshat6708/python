import os

# Set the directory path you want to list
directory_path = "/windows/System32"  # "." means current directory

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
