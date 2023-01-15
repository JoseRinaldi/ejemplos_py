print("=======================")
print("Buscar mayor")
print("=======================\n")

a = int(input("ingrese un numero:"))
b = int(input("\n""ingrese un numero:"))
c = int(input("\n""ingrese un numero:"))

if a > b and a > c:
    print("\n""el mayor es ", a)
elif b > a and b > c:
    print("\n""el mayor es ", b)
else:
    print("\n""el mayor es ", c)

print("\n""fin.")
