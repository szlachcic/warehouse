import db
import os


db=db.DB()

def menu():
    clear = lambda: os.system('clear') #on Linux System
    clear()
    print("Prosty UI:-)\n")
    
    print("1->utworz material")
    print("2->utworz element")
    print("3->dodaj material")
    print("4->dodaj element")
    print("5->odejmij material")
    print("6->odejmij element")

def utworz_element():
    print("Podaj nazwe elementu:")
    nazwa=input()

    print("Podaj ilosc:")
    ilosc=input()

    print("Podaj koszt:")
    koszt=input()

    print("Opis elemantu:")
    opis=input()

    print("Podaj dostawce elementu:")
    dostawca=input()

    print("Podaj czas dostawy:")
    czas=input()

    db.nowy_element(nazwa, ilosc, opis, koszt, dostawca, czas)

def utworz_material():
    nazwa=input("Podaj nazwe materialu:")

    ilosc=input("Podaj ilosc:")

    koszt=input("Podaj koszt:")

    opis=input("Opis materialu:")

    dostawca=input("Podaj dostawce materialu:")

    czas=input("Podaj czas dostawy:")

    db.nowy_material(nazwa, ilosc, opis, koszt, dostawca, czas)


if __name__ == "__main__":

    menu()

    while (True):
        komenda=input()

        if komenda == 1: utworz_material()
        elif komenda == 2: utworz_element()
        elif komenda == 3: pass
        elif komenda == 4: pass
        elif komenda == 5: pass
        elif komenda == 6: pass
        else: print("zla komenda")

        menu()


