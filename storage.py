import json

FILE_NAME = "employees.json"


def save_data(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
