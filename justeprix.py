from random import randint

print("Bienvenue dans le juste prix")
play = True
 
def game():
    winningNumber = randint(1, 100)
    userNumber = int(input("Entrez un nombre \n"))
    lives = 4
    lastbigger = 100
    lastless = 1

    while userNumber != winningNumber and lives > 0:
        lives -= 1
        if userNumber > winningNumber:
            print("c'est moins.")
            if userNumber< lastbigger:
                lastbigger = userNumber
        elif userNumber < winningNumber:
            print("c'est plus")
            if userNumber> lastless:
                lastless = userNumber
        print("il vous reste " + str(lives+1))
        userNumber = int(
            input("Entrez un nombre entre " + str(lastless) + " et "+str(lastbigger) + "\n"))

    if lives == 0:
        print("Vous avez perdus pas de chances")
        print("Le juste prix était " + str(winningNumber))
    else:
        print("Ceci est le jsute prix bien joué")
    choix = input("Voulez vous rejouer? o/n \n")
    if choix == "o":
        return True
    elif choix == "n":
        return False
    else:
        print("Entrée invalide le programe va s'éteindre.")


while play:
    play = game()

print("Au revoir")
