#Entrada de datos
edad = int(input("ingrese su edad: "))

if (edad >= 18 and edad <= 120):
    print("mayor de edad")
elif (edad < 18 and edad >= 1):
    print("menor de edad")
else:
    print("otra cosa")
