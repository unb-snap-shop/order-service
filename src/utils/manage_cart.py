import json

filename = 'src/data/cart.json'


def write_json(new_data):
    with open(filename, 'r+') as file:
        # load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside
        file_data.append(new_data)
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

        file.truncate()  # remove any garbaage left over


def get_json():
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        return file_data
