""" Básico: imprime todos los números enteros del 0 al 150. """

for x in range(0,151):
    print(x)
print("**"*20)

#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for x in range(5,1001,5):
    print(x)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for x in range(1,101):
    if x %5 ==0:
        print(x)
        print("coding") 
    if x %10 ==0:
        print(x)
        print("coding dojo") 
   
    print("coding Dojo")
    
for x in range(1,101):
    if x %10 ==0:
        print(x)
        print("coding dojo") 
    elif x %5 ==0:
        print(x)
        print("coding")