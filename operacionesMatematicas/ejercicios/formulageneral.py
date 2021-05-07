#entrada de datos

a = int(input("ingrese valor de a: "))
b = int(input("ingrese valor de b: "))
c = int(input("ingrese valor de c: "))

#calculos y operaciones
parte1 = ((-b) + (.5 ** ((b ** 2) - (4 * a * c) ))) / ( 2 * a)
parte2 = ((-b) - (.5 ** ((b ** 2) - (4 * a * c) ))) / ( 2 * a)

#resultados

print(f"valor x1 = {parte1}")
print(f"valor x2 = {parte2}")

