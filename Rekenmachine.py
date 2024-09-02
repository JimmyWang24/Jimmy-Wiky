getal1 = float(input("Enter a number: "))
getal2 = float(input("Enter a number: "))
operation = str(input("Enter operation: "))

if operation == "+":
    print(getal1 + getal2)
elif operation == "-":
    print(getal1 - getal2)
elif operation == "*":
    print(getal1 * getal2)
elif operation == "/":
    print(getal1 / getal2)
else:
    print("Invalid operation")