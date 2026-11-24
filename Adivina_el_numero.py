import random

print('Hola!, bienvenido al juego adivina el numero, el cual esta comprendido del 1 al 100, puedes fallar un maximo de 10 veces, empezamos')
AnotherGame = True

while AnotherGame:
    NumeroRandom=random.randint(1,100)
    intentos=[]
    fallos= 0

    while fallos < 10:
        while  True:

            try:
                Respuesta= int(input('Escribe un numero del 1 al 100: '))
                if Respuesta < 1 or Respuesta > 100:
                    print('Solamente numeros del 1 al 100')
                else:
                    break
            except ValueError:
                print('Solamente numeros del 1 al 100')
        nuevo= Respuesta not in intentos
        if Respuesta not in intentos:
            intentos.append(Respuesta)
        else:
            fallos+=1
        if Respuesta < NumeroRandom:
            if nuevo:
                fallos +=1
            print('Pista: Mas alto')
            
        elif Respuesta > NumeroRandom:
            if nuevo:
                fallos +=1
            print('Pista: Mas bajo')
        else:
            print('Acertaste!! lo lograste en',fallos,'fallos')
            break
        
        print('ya van',fallos,'fallos')
        if  7<= fallos <=9:
            print('Cuidado crack te quedan', 10 - fallos,'fallos')
    if fallos == 10:
        print('has perdido el numero era', NumeroRandom)

    while True:
        Question=(input('Quisieras jugar de nuevo? si o no: '))
        if Question =='si':
         break
        elif Question =='no':
            AnotherGame=False 
            print('Adios')
            break
        else:
            print('Responde si o no: ')