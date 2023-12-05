import json

def read_from_json_file(path_to_json):
    with open(path_to_json) as f:
        data = json.load(f)
        return data

def write_to_json_file(dict, file_path):
    json_object = json.dumps(dict, indent=2)

    with open(file_path, "w") as outfile:
        outfile.write(json_object)
