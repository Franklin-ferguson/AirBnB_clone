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
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

