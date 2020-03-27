#!/usr/bin/env python
import db
import os
import pymongo
import json

db=db.DB()

def menu():
    clear = lambda: os.system('clear') #on Linux System
    clear()
    print("Prosty UI:-)\n")
    
    print("Parametry do listy zakupow")
    while(1==1):
        print("Czy chcesz dodac produkt? y/n")
        ans=raw_input()
        if ans=="n": break
        elif ans=="y":
            kod=raw_input("Podaj kod materialu:")
            qnt=int(raw_input("Podaj ilosc:"))

            zestaw = db.product.find_one({"_id": kod})["content"]

            for x in zestaw:
                kod_elementu = x["id"]
                ilosc = x["quantity"]*qnt
                db.order.update({ "_id": kod_elementu },{ "$inc": { "quantity": -ilosc } })
                


def utworz_liste():
    db.order.remove({})
    for x in db.element.find():
        db.order.insert(x)


def czysc():

    for x in db.order.find():
        if x["quantity"]>=0: db.order.delete_one({"_id": x["_id"]})
        else: db.order.update_one({"_id": x["_id"]},{"$mul":{"quantity": -1}})




if __name__ == "__main__":

    utworz_liste()
    menu()
    czysc()
        


            









