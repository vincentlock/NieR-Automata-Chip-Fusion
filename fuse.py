import json

filename = "chips.json"

try:
    with open(filename, 'r') as file:
        # content = file.read()
        # print(content)
        data = json.load(file)
        # print(data)
except FileNotFoundError:
    raise FileNotFoundError(f"The file {filename} could not be found.")
except PermissionError:
    raise PermissionError(f"You do not have permission to read {filename}.")
except Exception as e:
    raise SystemError(f"An error occurred: {e}")
