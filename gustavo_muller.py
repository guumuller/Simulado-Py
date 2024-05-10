#Gustavo Müller Leonini Machado

listaA = []
listaB = []
listaC = []
qt_digitada = 0

while True:
    numero = int(input("Digite um número entre 10 e 100: "))

    if numero < 0:
        print("Digite apenas números positivos!")
        continue
    elif numero == 0 or qt_digitada == 20:
        break
    
    qt_digitada += 1
    
    if 20 <= numero <= 40:
        listaA.append(numero)
    if 50 <= numero <= 70:
        listaB.append(numero)
    if 30 <= numero <= 60:
        listaC.append(numero)
        
    if len(listaA) == 5:
        listaA.clear()
    if len(listaB) == 5:
        listaB.clear()
    if len(listaC) == 5:
        listaC.clear()
        
    print("Lista A:")
    for i, num in enumerate(listaA):
        print(f"Coluna {i + 1}: {num}") 
        
    print("Lista B:")
    for i, num in enumerate(listaB):
        print(f"Coluna {i + 1}: {num}")
    
    print("Lista C:")
    for i, num in enumerate(listaC):
        print(f"Coluna {i + 1}: {num}")          