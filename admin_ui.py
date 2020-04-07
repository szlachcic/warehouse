#!/usr/bin/env python
import db
import os
import sys
import time
import excel_sheet

db=db.DB()

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

    print("8->korekcja stanów magazynu")

    print("6->przygotuj listę zakupów")
    # print("7->przygotuj listę stanów magazynowych")
    

def create_material():
    clean()
    try:
        name=raw_input("Podaj nazwe materialu:")
        quantity=float(raw_input("Podaj ilosc:"))
        value=float(raw_input("Podaj koszt:"))
        description=raw_input("Opis materialu:")
        supplier=raw_input("Podaj dostawce materialu:")
        time=float(raw_input("Podaj czas dostawy:"))
        db.new_material(nazwa, ilosc, opis, koszt, dostawca, czas)

        print("Utworzono nowy materiał")

    except:
        print("Nie udało się utworzyć materiału")

def create_component():
    clean()
    try:
        name=raw_input("Podaj nazwe elementu:")
        quantity=float(raw_input("Podaj ilosc:"))
        value=float(raw_input("Podaj koszt:"))
        description=raw_input("Opis elementu:")
        supplier=raw_input("Podaj dostawce:")
        time=float(raw_input("Podaj czas dostawy:"))
        db.new_component(nazwa, ilosc, opis, koszt, dostawca, czas)

        print("Utworzono nowy element")

    except:
        print("Nie udało się utworzyć elementu")

def create_product():
    clean()
    try:
        name=raw_input("Podaj nazwe produktu:")
        description=raw_input("Opis produktu:")
        db.new_product(nazwa,opis)

        print("Utworzono nowy produkt")

    except:
        print("Nie udało się utworzyć produkt")

def add_material_to_component();
    clean()
    element_code=raw_input("Podaj kod elementu:")
    if db.check_collection(element_code)!=2: 
        print("Błędny kod")
        time.sleep(1000)
        return 0

    tmp = db.element.find_one({"_id": element_code})

    while(1==1):
        clean()
        print("Wpisanie q przerywa dodawanie materiałow do elementu\n")
        print("Dodawanie materiału do elementu: {}".format(tmp["name"]))
    
        code=raw_input("Podaj kod materialu:")
        if code=='q': break()

        if db.check_collection(code)!=1 : 
            print("Błędny kod")
            time.sleep(1000)
            continue

        quantity=float(raw_input("Podaj ilosc materiału:"))
        db.extend_component(element_code, code,  qnt)

def add_component_to_product();
    clean()
    product_code=raw_input("Podaj kod produktu:")
    if db.check_collection(element_code)!=3: 
        print("Błędny kod")
        time.sleep(1000)
        return 0

    tmp = db.product.find_one({"_id": product_code})

    while(1==1):
        clean()
        print("Wpisanie q przerywa dodawanie elementów do produktu\n")
        print("Dodawanie elementu do produktu: {}".format(tmp["name"]))
    
        code=raw_input("Podaj kod elementu:")
        if code=='q': break()

        if db.check_collection(code)!=2 : 
            print("Błędny kod")
            time.sleep(1000)
            continue

        quantity=float(raw_input("Podaj ilość elementów:"))
        db.extend_product(product_code, code,  quantity)

def update_quantity():
    clean()
    code=raw_input("Podaj kod elementu/materiału:")
    if db.check_collection(code)!=1 || db.check_collection(code)!=2: 
        print("Błędny kod")
        time.sleep(1000)
        return 0

    quantity=float(raw_input("Podaj aktualną ilość:"))
    db.update_quantity(code, quantity)

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

            content = db.product.find_one({"_id": kod})["content"]

            for x in content:
                code = x["id"]
                quantity = x["quantity"]*qnt
                db.order.update({ "_id": code },{ "$inc": { "quantity": -quantity } })

    for y in db.order.find():
        if y["supplier"]=="Kell ideas": 
            for z in y["materials"]:
                sheet.update(z["id"], z["name"], z["description"], z["quantity"], z["value"], z["supplier"], z["link"])
        else: sheet.update(y["id"], y["name"], y["description"], y["quantity"], y["value"], y["supplier"], y["link"])

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
        elif komenda == 4: update_quantity()
        elif komenda == 5: create_order()


        else: print("Błędną komendę")

        menu()