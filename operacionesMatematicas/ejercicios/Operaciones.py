from math import sqrt
# Entrada de datos
numero1 = float(input("Escribe un numero: "))
numero2 = float(input("Escribe otro numero: "))


# calculos y/o operaciones
suma = (numero1 + numero2)
potencia1 = numero1 ** 2
potencia2 = pow(numero2, 3)
raiz_cuadrada = sqrt (numero1)
raiz_cuadrada_2 = pow(numero2, 1/2)
raiz_cubica = pow(numero1, 1/3)
modulo_residuo = numero1 % numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
multiplicacion_y_suma_de_los_numeros = (numero1 * numero2) + numero1


#salida de datos
print("suma = " + str(suma))
print(f"suma =  {suma}")
print(f"cuadrado=  {potencia1}")
print (f"al cubo= {potencia2}")
print(f"raiz cuadrada= {raiz_cuadrada}")
print(f"raiz cuadrada2= {raiz_cuadrada_2}")
print(f"raiz cubica= {raiz_cubica}")
print(f"division= {division}")
print(f"residuo= {modulo_residuo}")
print(f"multiplicacion= {multiplicacion}")
print(f"multiplicacion y suma= {multiplicacion_y_suma_de_los_numeros}")



