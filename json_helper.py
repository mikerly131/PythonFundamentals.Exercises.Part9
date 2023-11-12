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
# In this case, each json object is a dictionary in the final list
# Will skip over any files that are not json structured
def open_all_json_files(dirpath: str):

    if os.path.isdir(dirpath) == False:
        raise NotADirectoryError
    else:
        file_list = os.listdir(dirpath)

    all_files_data = []

    for file_name in file_list:
        path = os.path.join(dirpath, file_name)
        try:
            json_data = open_json_file(path)
            all_files_data.append(json_data)
        except FileNotFoundError:
            continue
        except ValueError:
            continue

    return all_files_data



# Planning control flow for running as a program if needed
if __name__ == '__main__':
    filename = 'data/super_smash_bros/mario.json'
    mario_data = open_json_file(filename)
    print(mario_data)

    file_dir = '/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_bros'
    all_files_data = open_all_json_files(file_dir)
    print(all_files_data)






