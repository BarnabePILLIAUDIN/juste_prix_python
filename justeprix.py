from random import randint

print("Bienvenue dans le juste prix")
play = True
 
def game():
    max_str = input("Entrer un nombre maximum \n")
    while not max_str.isdigit():
        max_str = input("Entrer un nombre maximum valide \n")
    max = int(max_str)
    lives_str = input("Entrez le nombre de vies \n")
    while not lives_str.isdigit():
        lives_str = input("Entrez le nombre de vies \n")
    lives = int(lives_str)
    winning_number = randint(1, max)
    last_bigger= max
    last_less = 1
    user_number = int(input("Entrez un nombre entre "+str(last_less)+" et "+ str(last_bigger)+"\n"))

    while user_number != winning_number and lives > 0:
        lives -= 1
        if user_number > winning_number:
            print("c'est moins.")
            if user_number< last_bigger:
             last_bigger= user_number
        elif user_number < winning_number:
            print("c'est plus")
            if user_number> last_less:
                last_less = user_number
        print("il vous reste " + str(lives+1))
        user_number = int(
            input("Entrez un nombre entre " + str(last_less) + " et "+str(last_bigger) + "\n"))

    if lives == 0:
        print("Vous avez perdus pas de chances")
        print("Le juste prix était " + str(winning_number))
    else:
        print("Ceci est le jsute prix bien joué")
    choice= input("Voulez vous rejouer? o/n \n")
    if choice== "o":
        return True
    elif choice== "n":
        return False
    else:
        print("Entrée invalide le programe va s'éteindre.")


while play:
    play = game()

print("Au revoir")
