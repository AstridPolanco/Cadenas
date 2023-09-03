precio = input("Ingrese el precio del producto: ")
print("Euros: ", precio[:precio.find(".")], "Centimos: ", precio[precio.find(".")+1:])