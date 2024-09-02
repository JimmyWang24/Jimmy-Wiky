print("Kies de type Uber waarvan u gebruik wilt maken. 1 voor UberX. 2 voor UberBlack. 3 voor UberVan")

keuze = int(input("Voer uw keuze in: "))

afstand = int(input("Voer in hoeveel kilometers u wilt reizen: "))

if keuze == 1:
    print("U heeft gekozen voor UberX om voor ", afstand,"KM te reizen")
    print("De totaal prijs van uw rit is €", 1.5 * afstand)
elif keuze == 2:
    print("U heeft gekozen voor UberBlack om voor ", afstand,"KM te reizen")
    print("De totaal prijs van uw rit is €", 2.0 * afstand)
elif keuze == 3:
    print("U heeft gekozen voor UberVan om voor ", afstand,"KM te reizen")
    print("De totaal prijs van uw rit is €", 3.5 * afstand)
else:
    print("U heeft geen geldige keuze gemaakt")


