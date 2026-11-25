import random

print('Hola!, bienvenido al juego adivina el numero, el cual esta comprendido del 1 al 100, puedes fallar un maximo de 10 veces, empezamos: ')
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
            if fallos == 1:
                palabra = 'fallo'
            else:
                palabra = 'fallos'
            print('Acertaste!! lo lograste en',fallos,palabra)
            break
        if fallos == 1:
                palabra = 'fallo'
        else:
                palabra = 'fallos'
        print('Ya llevas',fallos,palabra)
        if  7<= fallos <=8:
            print('Cuidado crack te quedan', 10 - fallos,palabra)
        elif fallos == 9:
            print('Cuidado crack te quedan', 10 - fallos,'fallo')
    if fallos == 10:
        print('Has perdido el numero era', NumeroRandom)

    while True:
        Question=(input('Quisieras jugar de nuevo? si o no: ')).lower().strip()
        if Question in ('si', 'sí'):
         break
        elif Question == 'no':
            AnotherGame=False 
            print('Adios')
            break
        else:
            print('Responde si o no: ')