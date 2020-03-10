
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

    nazwa=raw_input("Podaj nazwe elementu:")

    ilosc=int(raw_input("Podaj ilosc:"))

    koszt=int(raw_input("Podaj koszt:"))

    opis=raw_input("Opis elementu:")

    dostawca=raw_input("Podaj dostawce elementu:")

    czas=int(raw_input("Podaj czas dostawy:"))

    lista{}

    
    
    db.new_element(nazwa, ilosc, opis, koszt, dostawca, czas, lista)

def utworz_material():
    nazwa=raw_input("Podaj nazwe materialu:")

    ilosc=int(raw_input("Podaj ilosc:"))

    koszt=int(raw_input("Podaj koszt:"))

    opis=raw_input("Opis materialu:")

    dostawca=raw_input("Podaj dostawce materialu:")

    czas=int(raw_input("Podaj czas dostawy:"))

    db.new_material(nazwa, ilosc, opis, koszt, dostawca, czas)


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


