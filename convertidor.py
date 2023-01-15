print("=================")
print("  Anidado de if")
print("=================")

print("\n --Convertidor-- \n")

print("ingrese el numero 1 para convertir numero a palabra")
print("ingrese el numero 2 para convertir palabra a numero \n")

numero = int(input("cual es tu opcion deseada? \n"))


if numero == 1:
    print("\n conversor de numero a palabra. \n")

    eleccion1 = int(input("¿cual es el numero que deseas convertir a palabra? "))

    if eleccion1 == 1:
        print("el numero es el 'Uno'")

    elif eleccion1 == 2:
        print("el numero es el 'Dos'")

    elif eleccion1 == 3:
        print("el numero es el 'Tres'")

    elif eleccion1 == 4:
        print("el numero es el 'Cuatro'")

    elif eleccion1 == 5:
        print("el numero es el 'Cinco'")

    else:
        print("el numero no esta registrado")

elif numero == 2:
    print("\n conversor de palabra a numero \n")

    eleccion2 = input("¿ cual es el numero que deseas convertir a numero? ")
    eleccion2 = eleccion2.lower()

    if eleccion2 == "uno":
        print("el numero es el '1'")

    elif eleccion2 == "dos":
        print("el numero es el '2'")

    elif eleccion2 == "tres":
        print("el numero es el '3'")

    elif eleccion2 == "cuatro":
        print("el numero es el '4'")

    elif eleccion2 == "cinco":
        print("el numero es el '5'")

    else:
        print("el numero no esta registrado")

else:
    print("esa opcion no es valida")

print("fin.")











    

    
    
