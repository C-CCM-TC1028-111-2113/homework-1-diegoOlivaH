def main():
    #escribe tu código abajo de esta línea
print("GameStop´s: Videogame price calculator")

new = int(input("Input the amount of new games: "))
usd = int(input("Input the amount of used games: "))

T = (new*1000)+(usd*350)

print("You will be paying:" , T)

if __name__ == '__main__':
    main()
