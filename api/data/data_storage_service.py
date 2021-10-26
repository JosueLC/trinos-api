#Python packages
import json
#Data Storage Service Class
#Manages the data storage for the application in json files

class DataStorageService():
    def __init__(self,filename : str):
        self.data_storage_path = f"api/data/{filename}.json"
        self.data_storage_file = open(self.data_storage_path, "r", encoding="utf-8")
        self.data_storage_json = self.data_storage_file.read()
        self.data_storage_file.close()
        self.data_storage_dictionary = json.loads(self.data_storage_json)

    def get_data_storage_dictionary(self):
        return self.data_storage_dictionary

    def get_data_storage_json(self):
        return self.data_storage_json

    def get_data_storage_path(self):
        return self.data_storage_path

    def get_data_storage_file(self):
        return self.data_storage_file

    def get_data_storage_file_name(self):
        return self.data_storage_file.name

    def get_data_storage_file_mode(self):
        return self.data_storage_file.mode

    def get_data_storage_file_size(self):
        return self.data_storage_file.size

    # get a element from data_storage_dictionary
    def get_data_storage_dictionary_element(self,key : str):
        return self.data_storage_dictionary[key]

    # save data_storage_dictionary to data_storage_file
    def save_data_storage_dictionary(self):
        self.data_storage_file = open(self.data_storage_path, "w+", encoding="utf-8")
        self.data_storage_file.write(json.dumps(self.data_storage_dictionary))
        self.data_storage_file.close()

    # set a element in data_storage_dictionary
    def set_data_storage_dictionary_element(self,key : str,value):
        self.data_storage_dictionary[key] = value
        self.save_data_storage_dictionary()
    
    # delete a element in data_storage_dictionary
    def delete_data_storage_dictionary_element(self,key : str):
        del self.data_storage_dictionary[key]
        self.save_data_storage_dictionary()
    
    # add a element in data_storage_dictionary
    def add_data_storage_dictionary_element(self,key : str,value):
        self.data_storage_dictionary[key] = value
        self.save_data_storage_dictionary()


    
