import random
from threading import Timer

play = True

while play:
    secret = random.randint(1,10)

    guess = None 
    count = 0

    while guess != secret:
        timeout = 10
        t = Timer(timeout, print, ['Sorry, times up'])
        t.start()
        prompt = "Vous avez %d secondes pour saisir un chiffre entre 1 et 10: \n" % timeout
        guess = input(prompt)
        t.cancel()
        if timeout == 0:
            break

        # guess = input('Saisissez un chiffre entre 1 et 10: ')
        if guess.isdigit():
            guess = int(guess)
        else : 
            print('Veuillez saisir un NOMBRE')

        count += 1
        if count == 4:
            print("Vous avez atteint le nombre max d'essais (4)")
            break

        if guess > secret :
            print ('Trop grand')
        elif guess < secret :
            print ('Trop petit')
        else :
            print("Bravo ! Vous avez gagné en", count, "coups !")
            # break    
            answer = int(input('Tapez 1 pour REJOUER et 2 pour ARRETER: '))
        
            if answer == 1:
                play = True
                continue
            elif answer == 2:
                play = False
            else:
                answer = int(input('Incorrect option. Type "1" to try again or "2" to leave the game'))