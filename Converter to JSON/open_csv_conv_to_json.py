import csv
from json import dump, dumps
from operator import attrgetter


# os.path.abspath(os.getcwd())
# # 'c:\\Users\\skarz\\Documents\\#IMPORTANT\\PYTHON\\Projects\\CSV to JSON'

class file_to_json:
    def __init__(self, file_path):
        self.file_path = file_path

    def csv_to_json(self, json_file_path):
        csvFile = open(self.file_path, 'r')
        jsonFile = open(json_file_path, 'w')

        # open a csv file handler
        fieldnames = ("Close", "High", "Low", "Open", "Volume")
        reader = csv.DictReader(csvFile, fieldnames)

        for row in reader:
            dump(row, jsonFile, separators=(', ', ':'))
            jsonFile.write('\n')

        csvFile.close()
        jsonFile.close()

    def txt_to_json(self, json_file_path):
        # fields in the sample file
        # fields = ['name', 'designation', 'age', 'salary']

        # dictionary where the lines from text will be stored
        dict1 = {}

        txtFile = open(self.file_path, 'r')
        jsonFile = open(json_file_path, 'w')

        for line in txtFile:
            # reads and trims each line, finally gives only the valid words
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()

        # creating json file
        dump(dict1, jsonFile, indent=4, sort_keys=False)
        jsonFile.close()

        txtFile.close()
        jsonFile.close()

    def py_to_json(self, json_file_path):
        pyFile = open(self.file_path, 'r')
        jsonFile = open(json_file_path, 'w')

        variable_names = [s for s in dir(pyFile) if not s.startswith('__')]

        my_dict = {variable_name: attrgetter(variable_name)(pyFile)
                   for variable_name in variable_names}
        print(dumps(my_dict, jsonFile))

    def txt_to_csv(self, csv_file_path):
        pass

    def json_to_csv(self, json_file_path):
        pass

    def json_to_txt(self, json_file_path):
        pass


# driver code (be careful while providing the path of the csv file,
# make sure to use double backslashes or single forward slashes)
# (provide the file path relative to your machine)
file_path = input('Enter the absolute path of the file: ')

if file_path.endswith('.csv'):
    file_to_json(file_path).csv_to_json()
    json_file_path = input('Enter the absolute path of the JSON file: ')

elif file_path.endswith('.txt'):
    file_to_json(file_path).txt_to_json()
    json_file_path = input('Enter the absolute path of the JSON file: ')

elif file_path.endswith('.py'):
    file_to_json(file_path).py_to_json()
    json_file_path = input('Enter the absolute path of the JSON file: ')

elif file_path.endswith('.json'):
    print("Please enter a valid file path! Don't parse .json to .json!")

else:
    print('Please enter a valid file path')
