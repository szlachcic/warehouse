#-*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import random
import pprint
import sys

class DB():


    def __init__(self):
        try:
            self.client = MongoClient()
            self.client = MongoClient("192.168.1.100", 37111, serverSelectionTimeoutMS = 5000)
            self.db = self.client.warehouse
            self.client.server_info()

            self.material = self.db.material
            self.component = self.db.component
            self.order = self.db.order
            self.product = self.db.product
            print("Connected to database")
        except pymongo.errors.ConnectionFailure as e:
            print("Can not connect to database")
            sys.exit(e)
            return 0
   
    def __del__(self):
        self.client.close()

    # Random free id from material collection
    def material_id(self):
        id = int(random.random()*100000)
        id = (id*10)+1
        if self.material.find({"_id": id})==0 | id<100000:
            self.material_id()
        else:
            return str(id)

    # Random free id from component collection
    def component_id(self):
        id = int(random.random()*100000)
        id = (id*10)+2
        if self.component.find({"_id": id})==0 | id<100000:
            self.component_id()
        else:
            return str(id)

    # Random free id from product collection
    def product_id(self):
        id = int(random.random()*100000)
        id = (id*10)+3
        if self.product.find({"_id": id})==0 | id<100000:
            self.product_id()
        else:
            return str(id)

    def new_material(self, name, quantity, description, value, supplier, time):
        id = self.material_id() 
        material = { "_id": id, "name": name, "quantity": quantity, "description": description, "value": value, "supplier": supplier, "time": time}
        try: 
            self.material.insert_one(material)
        except: 
            print("Can not inster material into collection")

    def new_component(self, name, quantity, description, value, supplier, time):
        id = self.component_id() 
        component = { "_id": id, "name": name, "quantity": quantity, "description": description, "value": value, "supplier": supplier, "time": time}
        try:
            self.component.insert_one(component)
        except:
            print("Can not inster component into collection")

    def new_product(self, name, description):
        id = self.product_id() 
        product = { "_id": id, "name": name, "description": description}
        try:
            self.product.insert_one(product)
        except: 
            print("Can not inster product into collection")

    def extend_component(self, component_id, material_id, quantity):
        tmp = self.material.find_one({"_id": material_id})
        try:
            self.component.update(
                { "_id": component_id },
                { "$push": { "materials": { "id": material_id,"name": tmp["name"] ,"quantity": quantity } } }
            )
        except:
            print("Can not extend component's materials list")

    def extend_product(self, product_id, component_id, quantity):
        tmp = self.component.find_one({"_id": component_id})
        try:
            self.product.update(
                { "_id": product_id },
                { "$push": { "content": { "id": component_id,"name": tmp["name"] ,"quantity": quantity } } }
            )
        except:
            print("Can not extend product's content list")

    def check_collection(self, id):
        code=int(id)
        if code>999995 and code<100000: return 0
        elif code%10==1: return 1
        elif code%10==2: return 2
        elif code%10==3: return 3
        else: return 0

    def add(self, id, quantity=1):
        if self.check_collection(id)==1: self.add_material(id, quantity)
        elif self.check_collection(id)==2: self.add_component(id, quantity)
        else: return 0

        return 1

    def sub(self, id, quantity=1):
        if self.check_collection(id)==1: self.sub_material(id, quantity)
        elif self.check_collection(id)==2: self.sub_component(id, quantity)
        else: return 0

        return 1

    def update_quantity(id, quantity):
        if check_collection(id)==1: db.update_material(id, quantity)
        elif check_collection(id)==2: db.update_component(id, quantity)
        else: return 0

        return 1

    
    def add_component(self, id, qnt=1):
        try:
            self.component.update({ "_id": id },{ "$inc": { "quantity": qnt } })
        except:
            print("Can not add component")

    def sub_component(self, id, qnt=1):
        try:
            self.component.update({ "_id": id },{ "$inc": { "quantity": -qnt } })
        except:
            print("Can not substract component")

    def add_material(self, id, qnt=1):
        try:
            self.material.update({ "_id": id },{ "$inc": { "quantity": qnt } })
        except:
            print("Can not add material")

    def sub_material(self, id, qnt=1):
        try:
            self.material.update({ "_id": id },{ "$inc": { "quantity": -qnt } })
        except:
            print("Can not substract material")

    def add_product(self, id):
        try:
            tmp = self.product.find_one({"_id": id})
        except:
            print("Can not find in product list")

        for x in tmp["content"]:
            self.add_component(x["id"], x["quantity"])

    def update_component(self, id, quantity):
        try:
            self.component.update({ "_id": id },{ "$set": { "quantity": quantity } })
        except:
            print("Can not update element quantity")

    def update_material(self, id, quantity):
        try:
            self.material.update({ "_id": id },{ "$set": { "quantity": quantity } })
        except:
            print("Can not update material quantity")

    def sub_product_sub_component(self, id):
        try:
            tmp = self.product.find_one({"_id": id})
        except:
            print("Can not find in product list")

        for x in tmp["content"]:
            self.sub_component(x["id"], x["quantity"])

    def add_component_sub_material(self, id, quantity=1):
        try:
            tmp = self.component.find_one({"_id": id})
            self.add_component(id, quantity)
        except:
            print("Can not find in component list")
            return 0

        try:
            for x in tmp["materials"]:
                self.sub_material(x["id"], x["quantity"]*quantity)
            return 1
        except: return 1

    def show(self, id, all=False):

        grup=self.check_collection(id)

        if grup==1: 
            try:
                tmp = self.material.find_one({"_id": id})
            except:
                print("Can not find in material list")
                return 0

            print("\nColection: Material")    
            print("ID: {}".format(tmp["_id"]))
            print("Name: {}".format(tmp["name"]))
            # print("Description: {}".format(tmp["description"]))
            print("Quantity: {}".format(tmp["quantity"]))
            # print("Supplier: {}".format(tmp["supplier"]))
            # print("Value: {}".format(tmp["value"]))
            # print("Delivery time: {}".format(tmp["time"]))

        elif grup==2: 
            try:
                tmp = self.component.find_one({"_id": id})
            except:
                print("Can not find in component list")
                return 0

            print("\nColection: Component")    
            print("ID: {}".format(tmp["_id"]))
            print("Name: {}".format(tmp["name"]))
            # print("Description: {}".format(tmp["description"]))
            print("Quantity: {}".format(tmp["quantity"]))
            # print("Supplier: {}".format(tmp["supplier"]))
            # print("Value: {}".format(tmp["value"]))
            # print("Delivery time: {}".format(tmp["time"]))

            if all==True:
                try:
                    for x in tmp["materials"]:
                        print("\nMaterial:")
                        print("ID: {}".format(x["id"]))
                        print("Name: {}".format(x["name"]))
                        print("Quantity: {}".format(x["quantity"]))
                except: 
                    print ("No materials")

            return 1

        elif grup==3: 
            try:
                tmp = self.product.find_one({"_id": id})
            except:
                print("Can not find in product list")
                return 0

            print("\nColection: Product")    
            print("Product ID: {}".format(tmp["_id"]))
            print("Product name: {}".format(tmp["name"]))

            return 1

        else: 
            print("Incorrect ID")
            return 0

    def erase_order(self):
        self.order.remove({})

        for x in self.element.find():
            self.order.insert(x)
        
    # def update_order(self, id, quantity)

