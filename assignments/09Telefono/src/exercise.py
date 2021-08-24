def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
print("Monthly Telefonic Fee Calculator")

msj = int(input("Input the number of messages:"))
mgb = float(input("Input the number of megas:"))
mint = int(input("Input the number of minutes:"))

Mensual = (msj+mgb+mint)*0.8

print("The monthly fee will be of:", Mensual)

if __name__ == '__main__':
    main()
