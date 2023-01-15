print("========================")
print("Ejercicio de par o impar")
print("========================")

numero = int(input("Ingrese un numero: "))

resto = numero % 2

if resto == 0:
    print("el numero ", numero ," es par")
else:
    print("el numero ", numero ,"es impar")

print("FIN.")
