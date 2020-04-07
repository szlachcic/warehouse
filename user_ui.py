#!/usr/bin/env python
#-*- coding: utf-8 -*-
import db
import os
import sys

global db

def clean():
    clear = lambda: os.system('clear') #on Linux System
    clear()


def menu():
    clean()
    print("Interfejs użytkownika\n")
    
    print("1->dodaj")
    print("2->odejmij")

    print("3->dodaj element i odejmin materiały")
    print("4->odejmij elementy dodane do produktu")
    
    print("5->pokaż zeskanowany przedmiot")

def add():

    while True:
        clean()
        print("Wpisanie q przerywa dodawanie")

        code=raw_input("Wczytaj kod:")
        print ("Wczytany przedmiot:")
        db.show(code)
        quantity=float(raw_input("Podaj ilości do dodania:"))
        if quantity>1000: break

        if db.check_collection!=0:
            db.add(code, quantity)
        elif code =="q": break
        else: print("Wczytano błędny kod")

def substract():

    while True:
        clean()
        print("Wpisanie q przerywa odejmowanie")

        code=raw_input("Wczytaj kod:")
        print ("Wczytany przedmiot:")
        db.show(code)
        quantity=float(raw_input("Podaj ilości do odjęcia:"))
        if quantity>1000: break

        if db.check_collection!=0:
            db.sub(code, quantity)
        elif code =="q": break
        else: print("Wczytano błędny kod")

def add_component_sub_material():

    while True:
        clean()
        print("Wpisanie q kończy dodawanie elementów do magazynu")

        code=raw_input("Wczytaj kod elementu:")
        print ("Wczytany element:")
        db.show(code)
        quantity=float(raw_input("Podaj ilości elementów dodawanych:"))
        if quantity>1000: break

        if db.check_collection!=0:
            db.add_component_sub_material(code, quantity)
        elif code =="q": break
        else: print("Wczytano błędny kod")

def product_sub_component():

    while True:
        clean()
        print("Wpisanie q kończy zdejmowanie zestawów elementów z magazynu")

        code=raw_input("Wczytaj kod produktu:")
        print ("Wczytany produkt:")
        db.show(code)

        if db.check_collection!=0:
            db.sub_product_sub_component(code)
        elif code =="q": break
        else: print("Wczytano błędny kod")

def show():

    while True:
       
        print("Wpisanie q kończy wyświetlanie")
        code=raw_input("Wczytaj kod produktu:")
        clean()
        print ("Wczytany produkt:")
        db.show(code, True)

if __name__ == "__main__":

    db=db.DB()
    menu()


    while (True):
        komenda=input()

        if komenda == 1: add()
        elif komenda == 2: substract()
        elif komenda == 3: add_component_sub_material()
        elif komenda == 4: product_sub_component()
        elif komenda == 5: show()
        else: print("Podano błędną komendę")

        menu()

