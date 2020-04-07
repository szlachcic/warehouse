#!/usr/bin/env python
#-*- coding: utf-8 -*-
import db
import os
import sys
import time
import excel_sheet

global db

def clean():
    clear = lambda: os.system('clear') #on Linux System
    clear()

def menu():
    clean()
    print("Interfejs administratora\n")
    
    print("1->utwórz materiał")
    print("2->utwórz element")
    print("3->utwórz produkt")

    print("4->przypisz materiały do elementu")
    print("5->przypisz elementy do produktu")

    print("6->korekcja stanów magazynu")

    print("7->przygotuj listę zakupów")
    # print("7->przygotuj listę stanów magazynowych")
    

def create_material():
    clean()
    try:
        name=raw_input("Podaj nazwe materialu:")
        quantity=float(raw_input("Podaj ilosc:"))
        value=float(raw_input("Podaj koszt:"))
        description=raw_input("Opis materialu:")
        supplier=raw_input("Podaj dostawce materialu:")
        delivery_time=float(raw_input("Podaj czas dostawy:"))
        if db.new_material(name, quantity, description, value, supplier, delivery_time)==0: 
            print("Nie udało się utworzyć materiału")
            time.sleep(2)
            return 0

        print("Utworzono nowy materiał")
        tmp=db.material.find_one({"name": name})
        tmp_id=tmp["_id"]
        db.show(tmp_id)
        time.sleep(5)
        return 1

    except:
        print("Nie udało się utworzyć materiału")
        time.sleep(2)
        return 0

def create_component():
    clean()
    try:
        name=raw_input("Podaj nazwe elementu:")
        quantity=float(raw_input("Podaj ilosc:"))
        value=float(raw_input("Podaj koszt:"))
        description=raw_input("Opis elementu:")
        supplier=raw_input("Podaj dostawce:")
        delivery_time=float(raw_input("Podaj czas dostawy:"))
        if db.new_component(name, quantity, description, value, supplier, delivery_time)==0:
            print("Nie udało się utworzyć elementu")
            time.sleep(2)
            return 0

        print("Utworzono nowy element:")
        tmp=db.component.find_one({"name": name})
        tmp_id=tmp["_id"]
        db.show(tmp_id)
        time.sleep(5)
        return 1

    except:
        print("Nie udało się utworzyć elementu")
        time.sleep(2)
        return 0

def create_product():
    clean()
    try:
        name=raw_input("Podaj nazwe produktu:")
        description=raw_input("Opis produktu:")
        if db.new_product(name,description)==0:
            print("Nie udało się utworzyć produkt")
            time.sleep(2)
            return 0

        print("Utworzono nowy produkt")
        tmp=db.product.find_one({"name": name})
        tmp_id=tmp["_id"]
        db.show(tmp_id)
        time.sleep(5)
        return 1

    except:
        print("Nie udało się utworzyć produkt")
        time.sleep(2)
        return 0

def add_material_to_component():
    clean()
    element_code=raw_input("Podaj kod elementu:")
    if code=='q': return

    if db.show(element_code)!=2:
        print("Brak elementu w bazie")
        time.sleep()
        return 0

    try:
        tmp = db.component.find_one({"_id": element_code})
    except: 
        print("Brak elementu w bazie")
        return 0

    while(1==1):
        clean()
        print("Wpisanie q kończy dodawanie materiałow do elementu\n")
        print("Dodawanie materiału do elementu: {}".format(tmp["name"]))
    
        code=raw_input("Podaj kod materialu:")
        if code=='q': break
        elif db.show(code)!=1:
            print("Błędny kod materiału")
            time.sleep(2)
            continue

        quantity=float(raw_input("Podaj ilosc materiału do dodania do elementu:"))
        if db.extend_component(element_code, code,  quantity)==0:
            print("Nie udało się dodać materiału")
            continue
        else: 
            print("Udało się dodać materiał do elementu")
    return 1

def add_component_to_product():
    clean()
    product_code=raw_input("Podaj kod produktu:")
    if code=='q': return

    if db.show(product_code)!=3:
        print("Brak elementu w bazie")
        time.sleep(2)
        return 0

    try:
        tmp = db.product.find_one({"_id": product_code})
    except: 
        print("Brak elementu w bazie")
        time.sleep(2)
        return 0

    while(1==1):
        clean()
        print("Wpisanie q przerywa dodawanie elementów do produktu\n")
        print("Dodawanie elementu do produktu: {}".format(tmp["name"]))
    
        code=raw_input("Podaj kod elementu:")
        if code=='q': break
        elif db.show(code)!=2:
            print("Błędny kod elementu")
            time.sleep(2)
            continue

        quantity=float(raw_input("Podaj ilość elementów:"))
        if db.extend_product(product_code, code,  quantity)==0:
            print("Nie udało się dodać elelemtu")
            continue
        else: 
            print("Udało się dodać element do produktu")

    return 1

def update_quantity():
    while(1==1):
        clean()
        print("Wpisanie q przerywa dodawanie elementów do produktu\n")
    
        code=raw_input("Podaj kod elementu/materiału:")
        if code=='q': break
        elif db.show(code)==0:
            print("Błędny kod elementu")
            time.sleep(2)
            continue

        quantity=float(raw_input("Podaj aktualną ilość:"))
        db.update_quantity(code, quantity)
        print("Aktualny element/materiał:")
        db.show(code)


    return 1


def create_order():
    clean()
    name=raw_input("Podaj nazwę zamówienia:")
    description=raw_input("Podaj opis zamówienia:")

    sheet=excel_sheet.Sheet(name, description)

    db.erase_order()

    while(1==1):
        print("Czy chcesz dodac produkt do uwzględnienia na liście? y/n")
        ans=raw_input()
        if ans=="n": break
        elif ans=="y":
            code=raw_input("Podaj kod produktu:")
            qnt=int(raw_input("Podaj ilość:"))

            content = db.product.find_one({"_id": code})["content"]

            for x in content:
                tmp = db.component.find_one({"_id":x["id"]})

                if tmp["supplier"]=="Kell ideas":
                    for y in tmp["materials"]:
                        code = y["id"]
                        quantity = y["quantity"]*qnt
                        db.order.update({ "_id": code },{ "$inc": { "quantity": -quantity } })

                else:
                    code = x["id"]
                    quantity = x["quantity"]*qnt
                    db.order.update({ "_id": code },{ "$inc": { "quantity": -quantity } })

    for y in db.order.find():
        # if y["supplier"]=="Kell ideas": 
        #     for z in y["materials"]:
        #         tmp=db.material.find_one({"_id": z["id"]})
        #         sheet.update(tmp["_id"], tmp["name"], tmp["description"], tmp["quantity"], tmp["value"], tmp["supplier"], tmp["link"])
        sheet.update(y["_id"], y["name"], y["description"], y["quantity"], y["value"], y["supplier"], y["link"])

    del sheet







if __name__ == "__main__":

    db=db.DB()
    menu()

    while (True):
        komenda=input()

        if komenda == 1: create_material()
        elif komenda == 2: create_component()
        elif komenda == 3: create_product()
        elif komenda == 4: add_material_to_component()
        elif komenda == 5: add_component_to_product()
        elif komenda == 6: update_quantity()
        elif komenda == 7: create_order()
        else: print("Błędną komendę")

        menu()