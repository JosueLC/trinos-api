#Python packages
import json
from uuid import uuid4
#Data Storage Service Class
#Manages the data storage for the application in json files

class DataStorageService():
    def __init__(self,filename : str):
        try:
            self.data_storage_path = f"api/data/{filename}.json"
            self.read_data_storage_file()
        except Exception as e:
            print(e)

    #read data_storage_file
    def read_data_storage_file(self) -> bool:
        try:
            self.data_storage_file = open(self.data_storage_path, "r", encoding="utf-8")
            self.data_storage_json = self.data_storage_file.read()
            self.data_storage_file.close()
            self.data_storage_dictionary = json.loads(self.data_storage_json)
            self.status = 1 #success
            return True
        except FileNotFoundError:
            self.create_new_data_storage_file()
            self.status = 2 #file open failure
            return False
        except json.decoder.JSONDecodeError:
            self.data_storage_dictionary = {}
            self.status = 3 #json decode error
            return False
            
    #create new data_storage_file
    def create_new_data_storage_file(self):
        self.data_storage_file = open(self.data_storage_path, "w+", encoding="utf-8")
        self.data_storage_file.write(json.dumps({}))
        self.data_storage_file.close()
        
    def get_data_storage_dictionary(self):
        return self.data_storage_dictionary

    # get data_storage_dictionary as json list
    def get_data_storage_dictionary_as_list(self) -> list:
        data_storage_dictionary_json_list = []
        for key in self.data_storage_dictionary:
            data_storage_dictionary_json_list.append(self.data_storage_dictionary[key])
        return data_storage_dictionary_json_list

#return a list with the selected attributes from all elements in data_storage_dictionary
    def get_data_storage_dictionary_elements(self,attributes : list) -> list:
        data_storage_dictionary_elements = []
        for key in self.data_storage_dictionary:
            data_storage_dictionary_element = {}
            for attribute in attributes:
                data_storage_dictionary_element[attribute] = self.data_storage_dictionary[key][attribute]
            data_storage_dictionary_elements.append(data_storage_dictionary_element)
        return data_storage_dictionary_elements

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
        try:
            return self.data_storage_dictionary[key]
        except KeyError:
            return None

    # save data_storage_dictionary to data_storage_file
    def save_data_storage_dictionary(self) -> bool:
        try:
            self.data_storage_file = open(self.data_storage_path, "w+", encoding="utf-8")
            self.data_storage_file.write(json.dumps(self.data_storage_dictionary, indent=4))
            self.data_storage_file.close()
            self.status = 1 #success
            return True
        except Exception as e:
            self.status = 4 #file save failure
            return False

    # set a element in data_storage_dictionary
    def set_data_storage_dictionary_element(self,key : str,value):
        self.data_storage_dictionary[key] = value
        return self.save_data_storage_dictionary()
    
    # delete a element in data_storage_dictionary
    def delete_data_storage_dictionary_element(self,key : str):
        del self.data_storage_dictionary[key]
        return self.save_data_storage_dictionary()
    
    # add a element in data_storage_dictionary
    def add_data_storage_dictionary_element(self,key : str,value) -> bool:
        if key in self.data_storage_dictionary:
            return False
        else:
            self.data_storage_dictionary[key] = value
            return self.save_data_storage_dictionary()

    #Generar una clave UUID usando una semilla de tipo string
    def generate_id(self) -> str:
        return str(uuid4())
