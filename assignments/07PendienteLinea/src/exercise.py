def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
print("Slope Calculator")
x1 = float(input("Input the value of x1: "))
x2 = float(input("Input the value of x2: "))
y1 = float(input("Input the value of y1: "))
y2 = float(input("Input the value of y2: "))

m = (y2-y1)/(x2-x1)
print("The value of the slope is: ")
print(m)



if __name__ == '__main__':
    main()
