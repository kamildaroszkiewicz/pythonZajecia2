a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")
c = input("Podaj liczbę c: ")

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print(b)
else:
    print(c)

print("Wydrukowano najmniejszą z możliwych liczb")

