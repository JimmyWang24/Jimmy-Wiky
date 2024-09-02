pizzaSize = input("Welk formaat wilt u?: Small (s), Medium (m), Large (l): ")
totaalprijs = 15 * (pizzaSize == "s") + 20 * (pizzaSize == "m") + 25 * (pizzaSize == "l")

pepperoni = input("Extra pepperoni?: Yes (y), No (n): ")
if pepperoni == "y" and pizzaSize == "s":
    totaalprijs += 2
elif pepperoni == "y" and pizzaSize == "m" or pizzaSize == "l":
    totaalprijs += 3
else:
    totaalprijs += 0

cheese = input("Extra kaas?: Yes (y), No (n): ")
totaalprijs += 1 if cheese == "y" else 0

print(f"Uw totaal bedrag komt uit op €{totaalprijs:.2f}")