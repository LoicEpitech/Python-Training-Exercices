import random
from english_words import english_words_set


def pickNumber():
    return random.randint(5, 15)


def sizeWord(theWord: str):
    return "_ " * len(theWord)


def gameAffichage(theWord, lettres_trouvees):
    affichage = ""
    for x in theWord:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "
    return affichage


def jouerTour(theWord, lettres_trouvees, lettres_tapees, nbEssai):
    if nbEssai <= 0:
        print("You lost... The word was:", theWord + ". Try again!")
        return

    proposition = input("Suggest a letter: ").lower()

    if len(proposition) != 1 or not proposition.isalpha():
        print("Please submit only ONE letter.")
        return jouerTour(theWord, lettres_trouvees, lettres_tapees, nbEssai)

    if proposition in lettres_tapees:
        print("You already tried this letter! Try another one.")
        return jouerTour(theWord, lettres_trouvees, lettres_tapees, nbEssai)

    lettres_tapees.add(proposition)

    if proposition in theWord:
        lettres_trouvees.add(proposition)
        print("Well done!")
    else:
        nbEssai -= 1
        print("Missed! You still have", nbEssai, "tries left.")

    affichage = gameAffichage(theWord, lettres_trouvees)
    print(affichage)

    if "_" not in affichage:
        print("Won! The word was:", theWord)
        return

    # Récursive pour éviter un while
    jouerTour(theWord, lettres_trouvees, lettres_tapees, nbEssai)


def theGame():
    theWord = ""
    while len(theWord) < 4:
        theWord = random.choice(list(english_words_set)).lower()
    nbEssai = pickNumber()
    lettres_trouvees = set()
    lettres_tapees = set()

    print("Welcome to the Hangman game!")
    print("The word contains", len(theWord), "letters.")
    print(sizeWord(theWord))
    print("You have", nbEssai, "tries left.")
    # print(theWord)

    jouerTour(theWord, lettres_trouvees, lettres_tapees, nbEssai)


theGame()
