#!/usr/bin/python3
'''FileStorage class file'''
from models.base_model import BaseModel
from models.user import User
import json
import models


class FileStorage:
    ''' File Storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionnary objects'''
        return self.__objects

    def new(self, obj):
        '''assigns a value to an instance attribute'''
        c = obj.__class__.__name__ + "." + obj.id
        self.__objects[c] = obj

    def save(self):
        '''saves to json file'''
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        '''loads from json file without errors'''
        try:
            with open(self.__file_path, 'r') as f:
                dic = json.load(f)

            for keys in dic.keys():
                self.__objects[keys] = BaseModel(**dic[keys])
        except FileNotFoundError:
            pass
