print("Digite um número")
a=float(input())   
print("\nAgora bote a operação\nElevado a 2 = e          Vezes = *\nDivisão = /              Mais = +\nMenos = -                Raiz quadrada = r\nOperac. inversa = i      Elevado = ^")
c=input()
c=c.lower()


if c=="e":
    print("\nResultado:")
    print(a**2)
    quit ()

elif c=="r":
    print("\nResultado:")
    print(a**0.5)
    quit()

elif c=="i":
    print("\nResultado:")
    print(1/a)
    quit()

print("\nFinalmente, o último número")                   #tema - raiz quadrada e operação inversa
b=float(input())

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
