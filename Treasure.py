print("Je bevind je op een onbewoond eiland waar geruchten rond gaan dat een verborgen schatkist te vinden is.")

keuze1 = input("Je ziet voor je een donker moeras (m). Langs de kust zie je ook een paar schipbreuken (s). Waar wil je heen gaan?: ")
if keuze1 == "m":
    print("Zodra je jouw eerste stap in het moeras neemt, voel je een nat gevoel bij je enkel. Je kijkt omlaag, een vlees-etende plant heeft te vast! Je wordt meegetrokken in het moeras, zonder hoop...")
elif keuze1 == "s":
    print("""Terwijl je langs een van de schipbreuken loopt zie je iets binnen glinsteren. Je loopt dichterbij en ziet een gigantisch kompas. De kompaswijzer ligt ernaast op de vloer. Boven het kompas staat een tekst: "Oost West, Zuid Slechts".""")
else:
    print("Je hebt een ongeldige optie ingevoerd.")

keuze2 = input("Je denkt dat de kompaswijzer op de juiste positie moet staan. Hoe leg je het neer? Noord (n), Zuid (z), Oost (o), West (w): ")
if keuze2 == "z" or "w" or "o":
    print("Je hoort de kompaswijzer in het kompas klikken. Vervolgens nog een tik, en nog een tik, en nog een. Het tempo gaat steeds sneller. Je begint te denken dat je een fout hebt gemaakt. Voordat je een stap weg kan nemen /*BOOM/*! Misschien had je meer raadsel puzzles thuis maken...")
elif keuze2 == "n":
    print("Het moment dat je de kompaswijzer wijst naar Noord voel je het zand onder je voeten rommelen. Het gigantische kompas begint langzaam opzij te rollen. Daarachter zie je een diep, donker grot. Je besluit om het voorzichtig te betreden.")

