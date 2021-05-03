"""
int a = 12;
int b = 5;

if(a<b)
{
	System.out.println("a es menor que b");
}
else (b<a)
{
	System.out.println("b es menor que a");
}
else
{
	System.out.println("a es igual a b");
}
"""

#Pyhtoon
a = 12
b = 5.5

if a<b:
	# imprimir algo...
else:
	# imprimir algo...

if a<b:
	print("a es menor que b")
else b<a:
	print("b es menor que a")
else:
	print("a es igual a b")


# En Pyhtoon se pone el signo de gatito para poner notas.
'''
Tres comillas para texto.
'''
"""
Tipos de datos:
- double
- int
- float
- boolean
- String*: Objeto > datatype
- bye
- long
- bigInt

Lenguajes Compilados
> C++, C, C#, Java***...

Lenguajes Interpretados:
> Pyhtoon, Javascript, ruby...

Maquinas virtuales
>
"""

#En Pyhtoon no se necesita punto y coma, no necesita corhetes, tipo de variables es....

#########################################################

#Pyhtoon
	
	# Usar arreglos > arrays
	# [dato 1, dato2, dato3, dato4]
	# LiST -> ["hola", "mundo", 2, 3, 3.5]...
	# INDEXAR ->: "hola", 1: "mundo," ... -1

nombre = ["hola", "mundo". "soy", "Andre"]

cuantos = len(nombres)
"""
print(arr[0])
print(arr[-1])
"""
# Usar un Ciclo
# While, For, Do While
# FOR

for nombre in nombres:
	print(nombre)
print("----------------------")
for i in range(cuantos):
	print(nombres[i])

abs = "abcdefghijklmnopqrstuvwxz"

for letra in abc:
	if letra == "i":
		break
	print(letra")")

i=0

while i < cuantos:
	print("Anda le")
	i+=1 # i = i + 1

# Datos del usuario > terminal
# Input() : String
# Parse o cast -> Int, Float, String...

nombre = input("Ingresa tu nombre:")
print("Tu nombre es: " + nombre)

edad = int(input("Ingresa tu edad:"))
print("Tu edad es:" + edad)

if int(edad) < 18:
	print("No puedes tomar!")
else:
	print("TOMAR")

### Ejercicio
# Pedir n (el usuario lo da) nombres al usuario, lo van a guardar en una lista (list)
#Print al revés a la lista
# n = int(input("Ingresa cuantos nombres quieres ingresar:"))
