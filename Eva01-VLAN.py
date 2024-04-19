# este Scrip indicara si corresponde al rango normal o rango extendido
VLANnum = int(input("Cual es el número de VLAN? "))
if VLANnum >= 1 and VLANnum <= 1005:
    print("Esta es una VLAN de Rango Normal.")
elif VLANnum >=1006 and VLANnum <= 4094:
    print("Esta es una VLAN de Rango Extendido")
else:
    print("Esta no es una VLAN de Rango Normal o Extendido.")
