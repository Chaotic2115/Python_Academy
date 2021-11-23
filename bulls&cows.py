import random
import time

ODDELOVAC = "-" * 80


def uvod():
    print(f"""Vítej ve hře Bulls and Cows!\n{ODDELOVAC}\nVygeneroval jsem pro tebe tajné čtyřmístné číslo.\n{ODDELOVAC}
Ty zadáš čtyřmístné číslo které:
\t- nebude začínat 0
\t- čísla se nebudou opakovat\n{ODDELOVAC}
Pokud uhodneš některé číslo, jsou tu 2 možnosti:
\t- pokud jsi uhodl číslo i pozici, číslo/čísla jsou bull/bulls
\t- pokud jsi uhodl číslo, ale ne pozici, číslo/čísla jsou cow/cows
Hodně štěstí!\n{ODDELOVAC}""")


def generovane_cislo(delka):
    """
    Funkce generuje nahodné 4místné číslo jako string, které nezačína 0 a žádné číslo se neopakuje.
    """
    g_cislo = ""
    while len(set(g_cislo)) != delka or g_cislo[0] == 0:
        g_cislo = str(random.randint(1000, 9999))
    return g_cislo


def hadane_cislo():
    """
    Funkce nechá uživatele zadat 4místné číslo jako string. Obsahuje kontrolu vstupu. Funkce nekončí do doby, než vstup projde kontrolou.
    """
    while True:
        cislo = input("Zadej čtyřmístné číslo: \n")
        if cislo[0] == "0":
            print("Číslo nesmí začínat 0!\n")
        elif not cislo.isdecimal:
            print("Zadal jsi i něco jiného než čísla!\n")
        elif len(set(cislo)) != 4:
            print("Číslo je delší/kratší než 4, nebo obsahuje některé číslice stejné!\n")
        else:
            break
    return cislo


def hra(g_cislo, h_cislo):
    """
    Funkce hry porovnává vygenerované číslo proti vstupu. Vrací počet bulls/cows v hádaném čísle v jednom kole.
    """
    bulls = 0
    cows = 0
    for index, cislo in enumerate(g_cislo):
        if cislo == h_cislo[index]:
            bulls += 1
        elif cislo in h_cislo:
            cows += 1
    return bulls, cows


def kontrola_hry(bulls, cows, pokusy):
    """
    Funkce vrací výsledky každého kola, kdy hráč hádá číslo.
    """
    konec = False
    if bulls == 4:
        print(f"Gratuluji! Vyhrál jsi na {pokusy} pokusů.")
        konec = True
    else:
        if bulls == 1:
            pripona = ""
        else:
            pripona = "s"
        if cows == 1:
            pripona2 = ""
        else:
            pripona2 = "s"
        print(f"Uhádnuto: | {bulls} bull{pripona} | {cows} cow{pripona2} | Počet pokusů: {pokusy}")
    return konec


def convert(seconds):
    """
    Funkce pro převod sekund na minuty a sekundy, včetně skloňování.
    """
    minutes = seconds // 60
    seconds %= 60
    if minutes == 1:
        pripona = "u"
    elif minutes > 1 and minutes < 5:
        pripona = "y"
    else:
        pripona = ""
    return f"{int(minutes)} minut{pripona} a {round(seconds, 1)} sekund"


def main():
    uvod()
    g_cislo = generovane_cislo(4)
    pokusy = 0
    start = time.time()
    while True:
        h_cislo = hadane_cislo()
        pokusy += 1
        bulls, cows = hra(g_cislo, h_cislo)
        if kontrola_hry(bulls, cows, pokusy):
            break
    end = time.time()
    vysledek = convert(end - start)
    print(f"Uhádnout číslo ti trvalo: {vysledek}")


main()