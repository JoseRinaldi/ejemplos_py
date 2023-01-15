print("=================")
print("   Ejercicios")
print("=================")

print("Depertamento de atencion al cliente (clave 1)")
print("Departamento de logistica (clave 2)")
print("gerencia (clave 3)\n")

nombre = input("Ingrese el nombre del empleado: ")
clave = int(input("ingrese clave del area: "))
años = float(input("ingrese los años de antiguedad: "))
print("\n")

if clave == 1:

    if años <= 1:
        print("Le corresponden al empleado ", nombre , " 6 dias de vacaciones")
    elif años >= 2 and años <= 6:
        print("Le corresponden al empleado ", nombre , "  14 dias de vacaciones")
    else:
        print("Le corresponden al empleado ", nombre , "  20 dias de vacaciones")
        
elif clave == 2:
    if años <= 1:
        print("Le correspondenal empleado ", nombre , "  7 dias de vacaciones")
    elif años >= 2 and años <= 6:
        print("Le corresponden al empleado ", nombre , "  15 dias de vacaciones")
    else:
        print("Le corresponden al empleado ", nombre , "  22 dias de vacaciones")
    

elif clave == 3:
    if años <= 1:
        print("Le correspondenal empleado ", nombre , "  10 dias de vacaciones")
    elif años >= 2 and años <= 6:
        print("Le corresponden al empleado ", nombre , "  20 dias de vacaciones")
    else:
        print("Le corresponden al empleado ", nombre , "  30 dias de vacaciones")
    
else:
    print("Ha ingresado mal el area ")
