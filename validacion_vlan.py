vlan = int(input("Ingrese el número de VLAN: "))

if vlan >= 1 and vlan <= 1005:
    print("La VLAN corresponde a un rango NORMAL.")
elif vlan >= 1006 and vlan <= 4094:
    print("La VLAN corresponde a un rango EXTENDIDO.")
else:
    print("El número ingresado NO corresponde a una VLAN válida.")
