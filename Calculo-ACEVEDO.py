import math

PI = 3.141592
VALOR1 = (2 * PI) * 3
VALOR2 = (2 * PI) * 8
VALOR3 = (2 * PI) * 10

print("Para un radio de 3, su circunferienca sera de:", VALOR1 )
print("Para un radio de 8, su circunferienca sera de:", VALOR2 )
print("Para un radio de 10, su circunferienca sera de:", VALOR3 )

otro = int(input("quiere intentar otro valor? 1 = si 2 = no:"))

if otro == 1:
    valor = int(input("Ingrese el valor:"))
    valor_nuevo = float((2 * PI) * valor)
    print(valor_nuevo)
else:
    print("gracias")
