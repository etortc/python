
#entrada de datos
litros = float(input("nivel de cisterna en litros: "))

#operaciones y condicionales

if(litros < 0):
    print("fuga en cisterna")
elif(litros == 0):
    print("encender bomba de agua")
elif(litros > 0 and litros < 2):
    print("acelerar bomba de agua")
elif(litros >= 2 and litros < 4):
    print("bomba trabajando")
elif(litros >= 4 and litros < 6):
    print("desacelerar bomba")
elif(litros == 6):
    print("apagar bomba")
elif(litros > 6):
    print("desbordamiento de agua en sisterna")





