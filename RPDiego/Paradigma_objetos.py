def multi(mo, mr, sum):
    if mr == 1:
        return mo
    elif mr >= 1:
        #print(mo , mr)
        mo += sum
        mr -= 1
        return multi(mo, mr, sum)
    elif mr == 0:
        return 0

num1 = int(input("Ingrese el multiplicador: "))
num2 = int(input("Ingrese el numero a multiplicar: "))
num3 = num1
print("La multiplicacion es igual a: ", multi(num1, num2, num3))
