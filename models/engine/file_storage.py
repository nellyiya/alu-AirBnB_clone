#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    # def reload(self):
    #     """Reloads the stored objects"""
    #     if not os.path.isfile(FileStorage.__file_path):
    #         return
    #     with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
    #         obj_dict = json.load(f)
    #         obj_dict = {k: self.classes()[v["__class__"]](**v)
    #                     for k, v in obj_dict.items()}
    #         # TODO: should this overwrite or insert?
    #         FileStorage.__objects = obj_dict

    def reload(self):
        """Reloads the stored objects from the JSON file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                cls_name = v["__class__"]
                cls = self.classes().get(cls_name)
                if cls is None:
                    print(f"Class {cls_name} is not found in classes dictionary.")
                    continue
                FileStorage.__objects[k] = cls(**v)
        except Exception as e:
            print(f"Error reloading from {FileStorage.__file_path}: {e}")

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()