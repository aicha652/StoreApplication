"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return self.__objects
        else:
            dict_result = {}
            for key, val in self.__objects.items():
                if val.__class__.__name__ == cls.__name__:
                    dict_result.update({key: val})
            return dict_result

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        #"""Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.admin import User
        from models.products import Product
        from models.products import Category

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Product, 'Category': Category
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except (FileNotFoundError, BaseException):
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects if it's inside """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ deserializing the JSON file to objects """
        self.reload()