# programa para ordenar de manera ascendente 3 numeros cualquiera

print("------------------------------------")
print("----------ordenar numeros-----------")
print("------------------------------------")

# input
a = int(input("digite el primer numero: "))
b = int(input("digite el segundo numero: "))
c = int(input("digite el tercer numero: "))

# processing and output
if a > b and a > c:
    if b > c:
        print("El número mayor es "+str(a)+", el número del medio es "+str(b)+" y el número menor es "+str(c))
    else:
        print("El número mayor es "+str(a)+", el número del medio es "+str(c)+" y el número menor es "+str(b))
elif c > a and c > b:
    if a > b:
        print("El número mayor es "+str(c)+", el número del medio es "+str(a)+" y el número menor es "+str(b))
    else:
        print("El número mayor es "+str(c)+", el número del medio es "+str(b)+" y el número menor es "+str(a))

else:
    if b > a and b > c:
        if a > c:
            print("El número mayor es "+str(b)+", el número del medio es "+str(a)+" y el número menor es "+str(c))
        else:
            print("El número mayor es "+str(a)+", el número del medio es "+str(c)+" y el número menor es "+str(a))

