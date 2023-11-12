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


# Function takes a directory path, write to directory path
# It finds json files in directory path, and writes all the json data to a new file in the write to directory path
def write_pickle(source_file_directory: str, write_to_directory: str, file_name: str):
        
    data_to_write = open_all_json_files(source_file_directory)
    json_data_to_write = json.dumps(data_to_write)

    if os.path.isdir(write_to_directory) == False:
        raise NotADirectoryError
    else:
        write_path = os.path.join(write_to_directory, file_name)
        write_out = open(write_path, 'w')
        write_out.write(json_data_to_write)
        #for json_object in json_data_to_write:
        #    write_out.write(f'{json_object}\n')
        write_out.close()

# Function gets a json file and loads contents as they appear in the file (json format)
def load_pickle_file(filepath: str):

    file_to_print = open_json_file(filepath)
    for line in file_to_print:
        json_line = json.dumps(line)
        if file_to_print.index(line) < len(file_to_print)-1:
            print(f'{json_line},')
        else:
            print(json_line)
   

# Planning control flow for running as a program if needed
# if __name__ == '__main__':
    # filename = 'data/super_smash_bros/mario.json'
    # mario_data = open_json_file(filename)
    # print(mario_data)

    # file_dir = '/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_bros'
    # all_files_data = open_all_json_files(file_dir)
    # print(all_files_data)

    # write_to_dir = '/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_pickles'
    # all_data_to_write = write_pickle(file_dir, write_to_dir)
    # with open('/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_pickles/super_smash_characters.pickle', 'r') as f:
    #    print(f.read())

    # load_pickle_file('/Users/mike/projects/zcw_python/PythonFundamentals.Exercises.Part9/data/super_smash_pickles/super_smash_characters.pickle')







