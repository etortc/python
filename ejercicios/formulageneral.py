#entrada de datos
print("ingrese los datos de ax2 +/- b2 +/- c = 0 cuando resulte 0: ")

a = float(input("ingrese valor de a: "))
b = float(input("ingrese valor de b: "))
c = float(input("ingrese valor de c: "))

#calculos y operaciones
parte1 = ((-b) + (pow((b ** 2) - (4 * a * c) , .5) )) / ( 2 * a)
parte2 = ((-b) - (pow((b ** 2) - (4 * a * c) , .5) )) / ( 2 * a)

#resultados

print(f"valor x1 = {round(parte1,2)}")
print(f"valor x2 = {round(parte2,2)}")

