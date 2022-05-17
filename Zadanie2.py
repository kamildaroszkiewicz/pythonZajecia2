import math


def drukuj(co, kom:" "):
    print(kom)
    for i in co:
        print(i, end=" ")


def srednia(oceny):
    sumaOcen = sum(oceny)
    return sumaOcen / float(len(oceny))


def mediana(oceny):
    oceny.sort()
    if len(oceny) % 2 == 0:
        half = int(len(oceny) / 2)
        return float(sum(oceny[half - 1:half + 1])) / 2.0
    else:
        return oceny[len(oceny) / 2]


def wariancja(oceny, srednia):
    sigma = 0.0
    for ocena in oceny:
        sigma += (ocena - srednia)**2
    return sigma / len(oceny)


def odchylenie(oceny, srednia):
    w = wariancja(oceny, srednia)
    return math.sqrt(w)


def main(args):
    przedmioty = set(['matematyka', 'polski', 'angielski'])
    drukuj(przedmioty, "Przedmioty: ")

    print("\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter.")
    while True:
        przedmiot = input("Podaj nazwę przedmiotu: ")
        if len(przedmiot):
            if przedmiot in przedmioty:
                print("Ten przedmiot już jest")
            przedmioty.add(przedmiot)
        else:
            drukuj(przedmioty, "\nTwoje przedmioty: ")
            przedmiot = input("\nKtóry przedmiot wybierasz, by dodać oceny?")
            if przedmiot not in przedmioty:
                print("Brak takiego przedmiotu, możesz go dodać.")
            else:
                break

    oceny = []
    ocena = None
    print("\nAby przerwać wprowadzanie ocen, podaj 0 (zero).")

    while not ocena:
        try:
            ocena = int(input("Podaj ocenę (1-6): "))
            if (ocena > 0 and ocena < 7):
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print("Błędna ocena.")
            ocena = None
        except ValueError:
            print("Błędne dane!")

    drukuj(oceny, przedmiot.capitalize() + " - oceny w dzienniczku: ")
    s = srednia(oceny)
    m = mediana(oceny)
    o = odchylenie(oceny, s)
    print("\nŚrednia: {0:5.2f}".format(s))
    print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))