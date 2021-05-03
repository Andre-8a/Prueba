
def caja(precio, monto):
	return(monto-precio)

precio_articulo = float(input("Ingrese el precio del articulo a pagar: "))
monto_ingreso = float(input("Ingrese el monto a pagar: "))
resultado = caja(precio_articulo, monto_ingreso)
print("El cambio es de: " + str(resultado) + ' pesos')
