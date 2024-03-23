#!/usr/bin/python3
"""
creating a class called BaseModel
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Represent a class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing the case BaseModel
        
        Args:
            *args : Unused
            **kwargs : Key and value pairs attributes
        """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dt_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the attribute updated_at to the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns the dictionary of the BaseModel
        key and value pair of the class object name
        """
        current_dict = self.__dict__.copy()
        current_dict["created_at"] = self.created_at.isoformat()
        current_dict["updated_at"] = self.updated_at.isoformat()
        current_dict["__class__"] = self.__class__.__name__
        return current_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        current_class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(current_class_name, self.id, self.__dict__)
