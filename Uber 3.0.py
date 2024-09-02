# Hier staan alle variablen die worden gebruikt in deze script
# Dit past zich aan het getal (int) dat de gebruiker kiest bij het kiezen van de auto
keuze_getal = int (0)
# Dit past zich aan de naam van de auto die de gebruiker kiest
keuze_auto = None
# Dit is de prijs dat zich aanpast afhankelijk van welke auto is gekozen bij de variable 'keuze_auto'
auto_prijs = float (0.0)
# Dit past zich de afstand in kilometers die de gebruiker aangeeft dat hij/zij zal reizen
afstand = int (0)
# Dit is de totaalprijs die de gebruiker zal betalen afhankelijk van welke auto is gekozen(en de bijhorende prijs van de auto) vermenigvuldigd door de aantal kilometers
totaal_prijs = float (0.0)

ritten_kiezen = bool (True)

while ritten_kiezen == True:
    print("Kies de type Uber waarvan u gebruik wilt maken. 1 voor UberX á €1,50/KM. 2 voor UberBlack á €2,00/KM. 3 voor UberVan á €3,50/KM")

    # Dit past de integer 'keuze_getal' aan afhankelijk van wat de gebruiker invoert
    keuze_getal = int(input("Voer uw keuze in: "))

    # Deze statements passen de variable 'keuze_auto' aan afhankelijk van welke keuze de gebruiker maakte bij de variable 'keuze_getal'. Als de gebruiker geen geldige optie invoert zal er een bericht komen dat het incorrect is
    if keuze_getal == 1:
        keuze_auto = "UberX"
        auto_prijs = 1.5
    elif keuze_getal == 2:
        keuze_auto = "UberBlack"
        auto_prijs = 2.0
    elif keuze_getal == 3:
        keuze_auto = "UberVan"
        auto_prijs = 3.5
    else:
        print("U heeft geen geldige keuze gemaakt")

    print(f"U heeft gekozen voor {keuze_auto}")

    # Dit past de variable 'afstand' aan afhankelijk van hoeveel de gebruiker invoert
    afstand = int(input("Voer in hoeveel kilometers u wilt reizen: "))

    totaal_prijs = auto_prijs * afstand

    print(f"U heeft gekozen voor een {keuze_auto} en om {afstand}KM te reizen. Uw kosten komen uit op €{totaal_prijs}.")

    nogeenkeer = (input("Nog een rit toevoegen? -- Yes(y) or No(n)"))
    if nogeenkeer == "y":
        ritten_kiezen = True
    elif nogeenkeer == "n":
        ritten_kiezen = False




