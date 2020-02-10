import pymongo
from pymongo import MongoClient
import random


class DB():

    def __init__(self):
        self.client = MongoClient()
        self.client = MongoClient("192.168.1.109", 27017)
        self.db = self.client.magazyn

        self.material = self.db.materialy
        self.element = self.db.elementy
        self.zestaw = self.db.zestawy
        self.produkt = self.db.produkty
        self.zamowienie = self.db.zamowienia

    def __del__(self):
        pass

    def element_id(self):
        id = int(random.random()*1000000000)
        id = 4000000000+id
        if self.element.find({"_id": id})== 0:
            self.element_id()
        else:
            return id

    def nowy_element(self, nazwa, ilosc, opis, koszt, dostawca, czas):
       id = self.element_id() 
       element = { "_id": id, "nazwa": nazwa, "ilosc": ilosc, "opis": opis, "koszt": koszt, "dostawca": dostawca, "czas": czas }
       self.element.insert_one(element)
       
    def material_id(self):
        id = int(random.random()*1000000000)
        id = 5000000000+id
        if self.element.find({"_id": id})== 0:
            self.element_id()
        else:
            return id

    def nowy_material(self, nazwa, ilosc, opis, koszt, dostawca, czas):
        id = self.material_id() 
        element = { "_id": id, "nazwa": nazwa, "ilosc": ilosc, "opis": opis, "koszt": koszt, "dostawca": dostawca, "czas": czas }
        self.material.insert_one(element)

    def list_element(self):
        pass

    def list_material(self):
        pass
    
    def dodaj_element(self, id, ilosc=1):
        self.element.update({ "_id": id },{ "$inc": { "ilosc": ilosc } })

    def odejmij_element(self, ilosc=1):
        self.element.update({ "_id": id },{ "$inc": { "ilosc": -ilosc } })

    def add_material(self, ilosc=1):
        self.material.update({ "_id": id },{ "$inc": { "ilosc": ilosc } })

    def odejmij_material(self, ilosc=1):
        self.material.update({ "_id": id },{ "$inc": { "ilosc": -ilosc } })
