#Entrada de datos
numero1 = float(input("calificacion 1: "))
numero2 = float(input("calificacion 2: "))
numero3 = float(input("calificacion 3: "))

#calculos y operaciones
Promedio = (numero1 + numero2 + numero3) / 3

#print(f"promedio= round({Promedio},2)")
if(Promedio <= 5):
    print("reprobado")
elif(Promedio > 5):
    print("aprobado")










