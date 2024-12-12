import json

def zapisz_do_pliku(nazwa_pliku, dane):
    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik)

def wczytaj_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        return json.load(plik)

def dodaj_studenta(lista_studentow, student):
    lista_studentow.append(student)

def dodaj_obecnosc(obecnosci, student, data):
    if student not in obecnosci:
        obecnosci[student] = []
    obecnosci[student].append(data)
