import random
import time
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


def temps_restant(start_time, max_time):
    return max_time - (time.time() - start_time)


def theGame(theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time):
    if temps_restant(start_time, max_time) <= 0:
        print("⏰ Times UP!")
        print("😕👎 You lost... The word was:", theWord + ". Try again!")
        return True  # True = stop le jeu

    if nbEssai <= 0:
        print("😕👎 You lost... The word was:", theWord + ". Try again!")
        return True

    print(f"⏳ Remaning time: {int(temps_restant(start_time, max_time))}s")
    proposition = input("Suggest a letter: ").lower()

    if len(proposition) != 1 or not proposition.isalpha():
        print("Please submit only ONE letter.")
        return theGame(
            theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time
        )

    if proposition in lettres_tapees:
        print("You already tried this letter! Try another one.")
        return theGame(
            theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time
        )

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
        print("🏆 Won! The word was:", theWord)
        return True

    # On continue si le temps n’est pas fini
    return theGame(
        theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time
    )


def difficulty(level: chr):
    if level == "e":
        return 60
    elif level == "h":
        return 15
    else:
        return 30


def multiMode():

    lvlForTime = input(
        "Choose the difficulty of the game easy(e)/medium(m)/hard(h) 💪 : "
    ).lower()
    max_time = difficulty(lvlForTime)
    start_time = time.time()

    print("👥 Multiplayer Mode")
    theWord = input("Player 1, please type a secret word: ").lower()

    print("\n" * 50)  # Cacher le mot

    while len(theWord) < 4 or not theWord.isalpha():
        theWord = input("Please type a valid word (only letters, min 4): ").lower()

    nbEssai = pickNumber()
    lettres_trouvees = set()
    lettres_tapees = set()

    print("Player 2, it's your turn to guess! 🪢")
    print("The word contains", len(theWord), "letters.")
    print(sizeWord(theWord))
    print("You have", nbEssai, "tries left.")

    theGame(theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time)


def soloMode():

    lvlForTime = input(
        "Choose the difficulty of the game easy(e)/medium(m)/hard(h) 💪 : "
    ).lower()
    max_time = difficulty(lvlForTime)
    start_time = time.time()

    theWord = ""
    while len(theWord) < 4:
        theWord = random.choice(list(english_words_set)).lower()

    nbEssai = pickNumber()
    lettres_trouvees = set()
    lettres_tapees = set()

    print("Welcome to the Hangman game! 🪢")
    print("The word contains", len(theWord), "letters.")
    print(sizeWord(theWord))
    print("You have", nbEssai, "tries left.")

    theGame(theWord, lettres_trouvees, lettres_tapees, nbEssai, start_time, max_time)


mode = input("Do you want to play Solo (s) or Multiplayer (m)? ").lower()

if mode == "m":
    multiMode()
else:
    soloMode()
