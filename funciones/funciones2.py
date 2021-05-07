def Sumar(a,b):
    return a + b

def Restar(a,b):
    return a - b

def Multiplicar(a,b):
    return a * b

def Dividir(a,b):
    return a / b
    
x = int(input("numero 1: "))
y = int(input("numero 2: "))

suma = Sumar(x,y)
print(suma)

resta = Restar(x,y)
print(resta)

multiplicacion = Multiplicar(x, y)
print(multiplicacion)

division = Dividir(x, y)
print(division)

