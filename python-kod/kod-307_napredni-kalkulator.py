broj1 = float(input("unesite vrijednost prvog broja: "))
broj2 = float(input("unesite vrijednost drugog broja: "))
operator = input("Unesite vrijednost operatora [+,-,*,/] : ")


if operator == "+":
    print(broj1 + broj2)
elif operator == "-":
    print(broj1 - broj2)
elif operator == "*":
    print(broj1 * broj2)
elif operator == "/":
    print(broj1 / broj2)
else:
    print("Uneseni operator nije dopušten! ")