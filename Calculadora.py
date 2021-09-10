n1 = float(input("Ingresar el primer número: ") )
n2 = float(input("Ingresar el segundo número: ") )

opcion = 0
while True:
	print("""
	
	1) Sumar 
	2) Restar 
	3) Multiplicar 
	4) Cambiar los números elegidos
	5) Dividir
	6) Apagar calculadora
	""")
	opcion = int(input("Elige una opción: ") )     

	if opcion == 1:
		print(" ")
		print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
	elif opcion == 2:
		print(" ")
		print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
	elif opcion == 3:
		print(" ")
		print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
	elif opcion == 4:
		n1 = float(input("Ingresa el primer número: ") )
		n2 = float(input("Ingresa el segundo número: ") )
	elif opcion == 5:
		if n2 == 0:
			print (" No se puede dividir por cero")
		else:
			print(" ")
			print("RESULTADO: La division de",n1,"*",n2,"es igual a",n1/n2)
	elif opcion == 6:
		break
	else:
		print("La opción ingresada es incorrecta")
