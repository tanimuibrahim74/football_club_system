import json  
# Imports the json module so we can read and write JSON files

class FileManager:
    # OOP USED HERE: This is a CLASS (object-oriented programming concept)
    # It represents a "FileManager" object that handles file operations

    def __init__(self, filename="data.json"):
        # OOP USED HERE: This is a CONSTRUCTOR method
        # It runs automatically when an object is created from this class
        self.filename = filename  
        # Stores the file name inside the object (object attribute)

    def save_data(self, data):
        # OOP USED HERE: This is a METHOD inside the class
        # It belongs to FileManager objects

        with open(self.filename, "w") as file:
            # Opens the JSON file in write mode

            json.dump(data, file, indent=4)
            # Writes the data into the JSON file in readable format

    def load_data(self):
        # OOP USED HERE: Another METHOD inside the class

        try:
            # Tries to open and read the file

            with open(self.filename, "r") as file:
                # Opens the JSON file in read mode

                return json.load(file)
                # Reads and converts JSON into Python dictionary

        except FileNotFoundError:
            # Runs if the file does not exist

            return {"players": [], "matches": []}
            # Returns empty default structure instead of crashing
