# Gebruiker kiest het type Uber
print("Kies het type Uber:")
print("1: Uber X (€1,5 per km)")
print("2: Uber Black (€2,0 per km)")
print("3: Uber Van (€3,5 per km)")
keuze = int(input("Voer het nummer in van de gekozen Uber: "))
# Geef de keuze en de kosten weer
uber_type = "Uber X" * (keuze == 1) + "Uber Black" * (keuze == 2) + "Uber Van" * (keuze == 3)

# Gebruiker voert het aantal kilometers in
kilometers = int(input("Voer het aantal kilometers in: "))

# Bepaal de prijs per kilometer op basis van de keuze
prijs_per_km = 1.5 * (keuze == 1) + 2.0 * (keuze == 2) + 3.5 * (keuze == 3)

# Bereken de totale kosten
totale_kosten = prijs_per_km * kilometers

print(f"Je hebt gekozen voor {uber_type} voor een afstand van {kilometers} km.")
print(f"De totale kosten zijn: €{totale_kosten}")