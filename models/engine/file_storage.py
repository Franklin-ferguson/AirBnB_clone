#!/usr/bin/python3
"""
Creating a file storage
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Represents a class FileStorage

    Attributes:
        __file_path : name of the file to save objects 
        __objects : dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """
        returns all ojects
        """
        return FileStorage.__objects


    def new(self, obj):
        """
        adds new attributes to the dictionary
        """
    
        object_class_name = obj.__class__.__name__

        key = "{}.{}".format(object_class_name, obj.id)

        FileStorage.__objects[key] = obj


    def save(self):
        """
        serialize the dictionary into json stirng
        """
        full_object_list = FileStorage.__objects

        full_dict = {}

        for obj in full_object_list:
            full_dict[obj] = full_object_list[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(full_dict, f)

    def reload(self):
        """
        Deserializing the json string back to dictionary
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    full_dict = json.load(f)

                    for key, value in full_dict.items():
                        inst_class, obj_id = key.split('.')

                        class_name = eval(inst_class)

                        object_instance = class_name(**value)

                        FileStorage.__objects[key] = object_instance
                except FileNotFoundError:
                    return

