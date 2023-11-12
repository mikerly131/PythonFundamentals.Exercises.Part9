import json
import os

# Function to open a json file and return a json object of the file contents
# Tried adding some error handling, but can't get it to read files from outside program directory
def open_json_file(filepath: str):

    try:
        with open(os.path.join(os.sys.path[0], filepath), "r") as f:
            all_file_data = json.load(f)
            return all_file_data
    except FileNotFoundError:
        raise FileNotFoundError
    except ValueError:
        raise ValueError
    
    
   
# Function to open all the json files in a directory and return all the contents in a list
"""
def open_all_json_files(directory: str):

        with open(filepath) as f:
        all_file_data = json.load(f)

    return all_file_data
"""

# Planning control flow for a program if needed

# filename = 'data/super_smash_bros/bob.txt'
# mario_data = open_json_file(filename)
# print(mario_data)





