#!/usr/bin/env python3.7
import os

def get_file_info_dict(path=os.getcwd()):
    """
    Returns a dictionary containing information about files in the specified path.

    If no path is specified, uses the current working directory.
    The function will return information on files nested in folders (recursive).
    """
    # Initialize an empty dictionary to store the file info dictionaries
    file_info_dict = {}

    # Iterate over the files in the directory
    for dirpath, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            # Get the file's full path
            file_path = os.path.join(dirpath, file_name)

            # Get the file's size in bytes
            file_size = os.path.getsize(file_path)

            # Get the file's last modified time as a timestamp
            modified_time = os.path.getmtime(file_path)

            # Create a dictionary to store the file's info
            file_info = {
                'file_path': file_path,
                'file_size': file_size,
                'modified_time': modified_time
            }

            # Add the dictionary to the outer dictionary with the file name as key
            file_info_dict[file_name] = file_info

    # Return the dictionary of file info dictionaries
    return file_info_dict


# Call the function with the default argument (current working directory)
#file_info_dict = get_file_info_dict()

# Print the file info dictionary
#print(file_info_dict, sep="\n")



file_info_dict = get_file_info_dict()
for key, value in file_info_dict.items():
    print(key, value, sep=": ")