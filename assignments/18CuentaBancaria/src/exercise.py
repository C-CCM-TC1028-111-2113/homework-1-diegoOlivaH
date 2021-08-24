def main():
    #escribe tu código abajo de esta línea
print("Ending balance of a bank account")

Blnc = float(input("Input the balance of the previous month:"))
In = float(input("Input the income:"))
Out = float(input("Input the outcome:"))
Checks = (int(input("Input the number of checks:"))*13)
MBlnc=Blnc+In-Out-Checks
BlncF=MBlnc-(MBlnc*0.075)

print("The balance of the account is:",BlncF)

if __name__ == '__main__':
    main()
