
#entrada de datos
pagodiario = float(input("pago diario: "))
diasdemes = float(input("numero de dias: "))

#calculos y operaciones
pagobruto = pagodiario * diasdemes
ivatrasladado = pagobruto * 0.16
subtotal = pagobruto + ivatrasladado
ivaretenido =  .1066 * pagobruto
isr = pagobruto * .10
pagoneto = subtotal - ivaretenido - isr

#\n salto de linea
#\t tabulador
#shift + alt + flecha abajo (copia la linea abajo)

print(f"el pago mensual es de: {pagoneto}")
print(f"el pago pago bruto es de: {pagobruto}")
print(f"el iva trasladado es de: {ivatrasladado}")
print(f"el subtotal es de: {subtotal}")
print(f"el iva retenido es de: {ivaretenido}")
print(f"el isr retenido es de: {isr}")




