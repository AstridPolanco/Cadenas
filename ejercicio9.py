fechaNac = input("Ingresa tu fecha de nacimiento siguiendo el formato dd/mm/aaaa: \n")
dia = fechaNac[:fechaNac.find('/')]
mesaño = fechaNac[fechaNac.find('/')+1:]
mes= mesaño[:mesaño.find('/')]
año= mesaño[mesaño.find('/')+1:]

print(dia)
print(mes)
print(año)