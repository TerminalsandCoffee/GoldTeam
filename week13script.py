#!/usr/bin/env python3.7

import os

#get current working directory
cwd = os.getcwd() 

#init empty list to store dict
file_list = []

#iterate over the files in the working dir
for file_name in os.listdir(cwd):
    #get full path
    file_path = os.path.join(cwd, file_name)
    
    #size in bytes
    file_size = os.path.getsize(file_path)
    
    #last modified time
    modified_time = os.path.getmtime(file_path)
    
    #create dict to store
    file_info = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
        'modified_time': modified_time
    }
    
    #add the dict tor the list
    file_list.append(file_info)
    
#print list of dict
#for file_info in file_list: > you can comment this out if you have more than one dict
    print(file_info, sep="\n")
