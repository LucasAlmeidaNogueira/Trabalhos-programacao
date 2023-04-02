print("Digite um número")
a=int(input())   
print("\nAgora bote a operação\nElevado a 2 = r          Vezes = *\nDivisão = /")
c=input()
c=c.lower()

if c=="r":
    print(a**2)
    quit ()

print("Finalmente, o último número")                   #tema - raiz quadrada e operação inversa
b=int(input())

print("\nResultado:")

if c=="*":
    print(a*b)

elif c=="/":
    print(a/b)

elif c=="+":
    print(a+b)

elif c=="-":
    print(a-b)

elif c=="^":
    print(a**b)