import pymongo
from pymongo import MongoClient
import random

class DB():

    def __init__(self):
        self.client = MongoClient()
        self.client = MongoClient("192.168.1.105", 27017)
        self.db = self.client.warehouse

        self.material = self.db.material
        self.element = self.db.component
        self.order = self.db.order

    def __del__(self):
        pass

    def element_id(self):
        id = int(random.random()*100000)
        id = (id*10)+2
        if self.element.find({"_id": id})== 0:
            self.element_id()
        else:
            return id

    def material_id(self):
        id = int(random.random()*100000)
        id = (id*10)+1
        if self.material.find({"_id": id})== 0:
            self.material_id()
        else:
            return id

    def new_element(self, name, quantity, description, value, supplier, time, array):
        id = self.element_id() 
        element = { "_id": id, "name": name, "quantity": quantity, "description": description, "value": value, "supplier": supplier, "time": time, "material_array": array }
        self.element.insert_one(element)

    def new_material(self, name, quantity, description, value, supplier, time):
        id = self.material_id() 
        material = { "_id": id, "name": name, "quantity": quantity, "description": description, "value": value, "supplier": supplier, "time": time }
        self.material.insert_one(material)

    def list_element(self):
        pass

    def list_material(self):
        pass
    
    def add_element(self, id, qnt=1):
        self.element.update({ "_id": id },{ "$inc": { "ilosc": qnt } })

    def _element(self, qnt=1):
        self.element.update({ "_id": id },{ "$inc": { "ilosc": -qnt } })

    def add_material(self, qnt=1):
        self.material.update({ "_id": id },{ "$inc": { "ilosc": qnt } })

    def odejmij_material(self, qnt=1):
        self.material.update({ "_id": id },{ "$inc": { "ilosc": -qnt } })
