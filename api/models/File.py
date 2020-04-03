import json 

def create_file(filename, json_data):
    extension = '.json'
    with open(filename+extension, 'w') as file:
        json.dump(json_data, file, indent=4)