import json

def load_data(filepath):
    with open(filepath,'r') as f:#this will read the data from json file to python
        return json.load(f)
    
    
def save_data(filepath, data):
    with open(filepath, 'w') as f:# this will write from python to the json file,with automatically will close the file
        json.dump(data, f, indent=4)
        
    