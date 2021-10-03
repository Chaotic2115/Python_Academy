# Texty pro analýzu
TEXTS = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

ODDELOVAC = "=" * 55
UZIVATELE = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Získání jména a hesla
print(ODDELOVAC)
jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
print(ODDELOVAC)

# kontrola jmnéna a hesla
if heslo == UZIVATELE.get(jmeno):
    print(f"Vítej v Text Analyzátoru, {jmeno}. \nMáš na výběr 3 texty k analýze.")
    print(ODDELOVAC)
    volba = input("Zvol text k analýze(1-3): ")
    print(ODDELOVAC)
else:
    print("Špatné uživatelské jméno nebo heslo! \nUkončuji aplikaci!")
    print(ODDELOVAC)

# listy pro analýzu
prvni_velke = []
cislice = []
velka_pismena = []
mala_pismena = []

# kontrola správnosti volby
if volba.isdigit():
    volba = int(volba) - 1
# procházení a anylýza textu podle volby
    for text in TEXTS:
        text = TEXTS[volba]
        print(f"Zvolený text: \n{text}")
        print(ODDELOVAC)
        cista_slova = [slovo.strip(",.()'") for slovo in text.split()]
        for slovo in cista_slova:
            if slovo.istitle():
                prvni_velke.append(slovo)
            elif slovo.isupper():
                velka_pismena.append(slovo)
            elif slovo.islower():
                mala_pismena.append(slovo)
            elif slovo.isdigit():
                cislice.append(int(slovo))
        print(f"V textu je {len(cista_slova)} slov.\n"
              f"V textu je {len(prvni_velke)} slov začínajících na velké písmeno.\n"
              f"V textu je {len(velka_pismena)} slov psaných velkými písmeny.\n"
              f"V textu je {len(mala_pismena)} slov psaných malými písmeny.\n"
              f"V textu je {len(cislice)} čísel\n"
              f"Součet všech čísel v textu je {sum(cislice)}")
        print(ODDELOVAC)
# sloupcový graf četnosti slov, délky slov uloženy do listu a následně počty délek uloženy do slovníku
        print("Délka | Četnost | Počet")
        print('-' * 55)
        serazena_slova = sorted(cista_slova, key=len)
        list_slov = []
        slovnik_slov = {}
        for slova in serazena_slova:
            list_slov.append(len(slova))
            for i in list_slov:
                slovnik_slov.setdefault(i)
                slovnik_slov[i] = list_slov.count(i)
        for klic in slovnik_slov.keys():
            print(klic, "\t  |", "*" * slovnik_slov[klic], "|", slovnik_slov[klic])
        print(ODDELOVAC)
        break
else:
    print("Neplatná volba textu! \nUkončuji aplikaci!")
    print(ODDELOVAC)