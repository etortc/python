from datetime import date
from datetime import datetime

#Entrada de datos
año = float(input("año de nacimiento: "))
fechaactual = date.today()
fecha = datetime.now()


#calculos
edad = fechaactual.year - año

#salida
print(f"su edad es: {edad}")
print(fecha)
print(fechaactual)


