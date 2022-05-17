from random import randint

ilosc = int(input("Ile liczb? "))
lista = []
for i in range(0, ilosc):
    lista.append(randint(0, 100))
print(lista)

print("Dodawanie liczb na końcu listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)
print(lista)

zbior = int(input("Którą liczbę usunąć? "))
lista.remove(zbior)
print(lista)