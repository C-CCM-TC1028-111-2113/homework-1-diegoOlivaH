def main():
    #escribe tu código abajo de esta línea
print("Calculator for Publishers")

wrds = int(input("Please Input the Number of Words in the documeent you are willing to publish:"))
pags = wrds/475
cost = pags*60
Fcost= cost-cost*0.1
print("The price in order to publish this document is: ",Fcost)


if __name__ == '__main__':
    main()
