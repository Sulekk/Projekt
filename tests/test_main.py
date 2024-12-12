import os
from main import zapisz_do_pliku, wczytaj_z_pliku, dodaj_studenta, dodaj_obecnosc

def test_zapisz_i_wczytaj_do_pliku():
    dane = {"klucz": "wartoœæ"}
    zapisz_do_pliku("test.json", dane)
    assert os.path.exists("test.json")
    wczytane_dane = wczytaj_z_pliku("test.json")
    assert wczytane_dane == dane
    os.remove("test.json")

def test_dodaj_studenta():
    lista = []
    dodaj_studenta(lista, "Jan Kowalski")
    assert "Jan Kowalski" in lista

def test_dodaj_obecnosc():
    obecnosci = {}
    dodaj_obecnosc(obecnosci, "Jan Kowalski", "2024-12-12")
    assert "Jan Kowalski" in obecnosci
    assert "2024-12-12" in obecnosci["Jan Kowalski"]
