def uvod():
  oddelovac = "=" * 60
  print(f"""\nVítej ve hře piškvorky!\n{oddelovac}
PRAVIDLA:
Hráči střídavě umístí značku na pozici v hracím poli 3x3. 
Vítězí ten, kdo jako první vytvoří řadu:
  * horizontálně
  * vertikáně
  * diagonalně\n{oddelovac}\n""")


def hraci_plocha():
  """
  Funkce vytiskne hrací plochu 3x3.
  """
  plocha = []
  radek = "+---+---+---+"
  radek2 = "|   |   |   |"
  plocha2 = []
  for i in range(4):
    i = radek2
    plocha.append(radek)
    plocha.append(i)
    plocha2 = "\n".join(plocha[0:-1])
  return plocha2




def tah_hrace(znak_hrace):
  """
  Funkce nechá zadat hráče číslo 1-9 na hrací ploše. Nenechá hráče zadat větší/menší číslo než je hrací plocha.
  """
  while True:
    vstup_hrace = int(input(f"Hráč {znak_hrace} | Napiš číslo svého tahu: "))
    if vstup_hrace < 1 or vstup_hrace > 9:
      print("Jsi mimo hrací plochu")
    else:
      break
  return vstup_hrace, znak_hrace


def replace(string, position, character):
  """
  Pomocná funkce pro přepisování hrací plochy.
  """
  return string[:position] + character + string[position+1:]


def prepsani_znaku(plocha, tah, znak_hrace):
  """
  Funkce pro přepsání znaku na hrací ploše. Lze přepsat jen prázdné pole.
  """
  if tah == 1 and plocha[16] == " ":
    plocha = replace(plocha, 16, znak_hrace)
  elif tah == 2 and plocha[20] == " ":
    plocha = replace(plocha, 20, znak_hrace)
  elif tah == 3 and plocha[24] == " ":
    plocha = replace(plocha, 24, znak_hrace)
  elif tah == 4 and plocha[44] == " ":
    plocha = replace(plocha, 44, znak_hrace)
  elif tah == 5 and plocha[48] == " ":
    plocha = replace(plocha, 48, znak_hrace)
  elif tah == 6 and plocha[52] == " ":
    plocha = replace(plocha, 52, znak_hrace)
  elif tah == 7 and plocha[72] == " ":
    plocha = replace(plocha, 72, znak_hrace)
  elif tah == 8 and plocha[76] == " ":
    plocha = replace(plocha, 76, znak_hrace)
  elif tah == 9 and plocha[80] == " ":
    plocha = replace(plocha, 80, znak_hrace)
  else:
    print("\nToto pole není prázdné!\n")
    return False
  return plocha    
  

def konec(plocha, znak_hrace):
  """
  Funkce pro kontrolu výhry. Pokud se zaplní celé pole, hra končí remízou.
  """
  if plocha[16] == znak_hrace and plocha[20] == znak_hrace and plocha[24] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[44] == znak_hrace and plocha[48] == znak_hrace and plocha[52] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[72] == znak_hrace and plocha[76] == znak_hrace and plocha[80] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[16] == znak_hrace and plocha[44] == znak_hrace and plocha[72] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[20] == znak_hrace and plocha[48] == znak_hrace and plocha[76] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[24] == znak_hrace and plocha[52] == znak_hrace and plocha[80] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[16] == znak_hrace and plocha[48] == znak_hrace and plocha[80] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[24] == znak_hrace and plocha[48] == znak_hrace and plocha[72] == znak_hrace:
    return print(f"Gratuluji, hráč {znak_hrace} vyhrál!\nKonec hry!"), True
  elif plocha[16] != " " and plocha[20] != " " and plocha[24] != " " and plocha[44] != " " and plocha[48] != " " and plocha[52] != " " and plocha[72] != " " and plocha[76] != " " and plocha[80] != " ":
    return print("Remíza!\nKonec hry!"), True


def main():
  oddelovac = "-" * 50
  uvod()
  herni_plocha = hraci_plocha()
  print(herni_plocha)
  
  while True:  
    znaky_hracu = ["O", "X"]
    for znak in znaky_hracu:
      print(oddelovac)
      tah, znak_hrace = tah_hrace(znak)
      herni_kolo = prepsani_znaku(herni_plocha, tah, znak)
      if herni_kolo == False:
        break
      print(herni_kolo)
      herni_plocha = herni_kolo
      if konec(herni_plocha, znak_hrace):
        exit()


main()


