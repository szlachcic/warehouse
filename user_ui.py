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
    print("Interfejs użytkownika")
    print("CTRL + C - zamknij aplikację")
    
    print("1->dodaj")
    print("2->odejmij")

    print("3->dodaj element odejmując materiały")
    print("4->odejmij elementy dodane do produktu")
    
    print("5->pokaż zeskanowany przedmiot")

def add():

    while True:
        clean()
        print("Wpisanie q przerywa dodawanie")
        code=raw_input("Wczytaj kod:")
        if code =="q": break

        print ("Wczytany przedmiot:")
        if db.show(code)==0: continue

        quantity=float(raw_input("Podaj ilości do dodania:"))
        if quantity>1000: continue

        db.add(code, quantity)

def substract():

    while True:
        clean()
        print("Wpisanie q przerywa odejmowanie")
        code=raw_input("Wczytaj kod:")
        if code =="q": return 0

        print ("Wczytany przedmiot:")
        if db.show(code)==0: continue

        quantity=float(raw_input("Podaj ilości do odjęcia:"))
        if quantity>1000: return 0
    
        db.sub(code, quantity)
        

def add_component_sub_material():

    while True:
        clean()
        print("Wpisanie q kończy dodawanie elementów do magazynu")
        code=raw_input("Wczytaj kod elementu:")
        if code =="q": return 0

        print ("Wczytany element:")
        if db.show(code)!=2: continue

        quantity=float(raw_input("Podaj ilości elementów dodawanych:"))
        if quantity>1000: break

        db.add_component_sub_material(code, quantity)


def product_sub_component():

    while True:
        clean()
        print("Wpisanie q kończy zdejmowanie zestawów elementów z magazynu")
        code=raw_input("Wczytaj kod produktu:")
        if code =="q": return 0

        print ("Wczytany produkt:")
        if db.show(code)!=3: continue

        db.sub_product_sub_component(code)


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

