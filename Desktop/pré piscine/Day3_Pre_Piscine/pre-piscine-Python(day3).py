# Task 1.1

mot = input("Entrez une phrase : ")
print(mot)

# Task 1.2
print(mot[0])
print(mot[12])

# Task 1.3
print(mot[-1])

# Task 1.4
print(mot[4:9])

# Task 2.1
mot = "Bonjour JE suis loic et toi tu es ?"
print(mot.lower())

# Task 2.2
print(mot.replace("tu", "ta"))

# Task 2.3
string = " Hello world !"
position = string.find("a")
print(position)

# Task 2.4 , 2.5
p = "abcdefghij"
print(p[::-2][:5][::-1][3:])
# expliquation
# p[:: -2] = " jhfdb "
# [:5] = " jhfdb "
# [:: -1] = " bdfhj "
# [3:] = " hj"
# result = "hj"

# Task 2.6
for i in range(1, 11):
    print("Phrase numero : " + str(i))

# Task 2.7
# Debug print("hello"+ 42). #42 est un entier et non une chaine de caractere il faut le convertir en chaine de caractere

# Task 2.8
s1, s2, s3 = "42", "is", " the answer "
print(s1 + " " + s2 + s3)

# Task 3.1
nomUtilisateur = str(input("Entrez votre nom : "))
print("Bonjour " + nomUtilisateur.title())

# Task 3.2
numUtilisateur = str(input("Entrez un nombre entre 0 et 9 : "))
print(numUtilisateur.__class__)

# Task 3.3
numUtilisateurAddition1 = int(input("Entrez un Premier nombre : "))
numUtilisateurAddition2 = int(input("Entrez un Deuxieme nombre : "))
print(
    "Le résultat de votre addition est : ",
    numUtilisateurAddition1 + numUtilisateurAddition2,
)

# Task 3.4
motUtilisateur = str(input("Entrez une phrase : "))
listeDeMot = motUtilisateur.split(" ")
resultat = ""
for i in listeDeMot:
    resultat += i[0]
print(resultat)

# Task Challenge

text1 = "the CataCat attaCk a Cat"
text2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"


def count_occurrences(text, substrings):
    text_lower = text.lower()
    count = 0
    for substring in substrings:
        substring_lower = substring.lower()
        count += text_lower.count(substring_lower)
        count += text_lower.count(substring_lower[::-1])
    return count


substrings = ["cat", "garden", "mice"]

print(count_occurrences(text1, substrings))
print(count_occurrences(text2, substrings))

# Task 3.5

phraseUtilisateur = str(input("Entrez une phrase : "))
dictionnaireDeLettre = {}
motUtilisateur = phraseUtilisateur.replace(" ", "").lower()
for i in motUtilisateur:
    if i in dictionnaireDeLettre:
        dictionnaireDeLettre[i] += 1
    else:
        dictionnaireDeLettre[i] = 1


# region DATA de lettres par langue
# source : https://en.wikipedia.org/wiki/Letter_frequency
LANGUAGE_PROFILES = {
    "english": {
        "e": 12.7,
        "t": 9.1,
        "a": 8.2,
        "o": 7.5,
        "i": 7.0,
        "n": 6.7,
        "s": 6.3,
        "h": 6.1,
        "r": 6.0,
        "d": 4.3,
        "l": 4.0,
        "c": 2.8,
        "u": 2.8,
        "m": 2.4,
        "w": 2.4,
        "f": 2.2,
        "g": 2.0,
        "y": 2.0,
        "p": 1.9,
        "b": 1.5,
        "v": 1.0,
        "k": 0.8,
        "j": 0.2,
        "x": 0.2,
        "q": 0.1,
        "z": 0.1,
    },
    "french": {
        "e": 14.7,
        "a": 7.6,
        "i": 7.5,
        "s": 7.9,
        "n": 7.2,
        "r": 6.6,
        "t": 7.0,
        "o": 5.8,
        "l": 5.5,
        "u": 6.3,
        "d": 3.7,
        "c": 3.3,
        "m": 2.7,
        "p": 3.0,
        "v": 1.8,
        "q": 1.4,
        "f": 1.1,
        "b": 0.9,
        "g": 1.0,
        "h": 1.1,
        "j": 0.3,
        "x": 0.4,
        "y": 0.3,
        "z": 0.1,
        "é": 1.5,
        "è": 0.8,
        "ê": 0.6,
        "ë": 0.1,
        "à": 0.5,
        "ù": 0.1,
        "ç": 0.3,
    },
    "spanish": {
        "e": 13.7,
        "a": 12.5,
        "o": 8.7,
        "s": 7.9,
        "n": 7.0,
        "r": 6.9,
        "l": 5.2,
        "d": 5.0,
        "c": 4.7,
        "t": 4.6,
        "u": 3.9,
        "m": 3.2,
        "p": 2.5,
        "b": 1.4,
        "g": 1.0,
        "v": 0.9,
        "y": 1.0,
        "q": 1.0,
        "h": 0.7,
        "f": 0.5,
        "z": 0.4,
        "j": 0.5,
        "ñ": 0.3,
        "á": 0.4,
        "é": 0.4,
        "í": 0.4,
        "ó": 0.4,
        "ú": 0.4,
    },
    "portuguese": {
        "a": 14.6,
        "e": 12.6,
        "o": 10.7,
        "s": 7.8,
        "r": 6.7,
        "i": 6.2,
        "n": 5.0,
        "d": 4.9,
        "m": 4.7,
        "u": 4.6,
        "t": 4.3,
        "c": 3.9,
        "l": 2.8,
        "p": 2.5,
        "v": 1.6,
        "g": 1.3,
        "h": 1.2,
        "q": 1.2,
        "b": 1.0,
        "f": 1.0,
        "z": 0.5,
        "j": 0.4,
        "x": 0.2,
        "á": 0.5,
        "â": 0.3,
        "ã": 0.5,
        "é": 0.4,
        "ê": 0.2,
        "í": 0.2,
        "ó": 0.4,
        "ô": 0.2,
        "õ": 0.3,
        "ú": 0.2,
        "ç": 0.3,
    },
    "italian": {
        "e": 11.8,
        "a": 11.7,
        "i": 10.7,
        "o": 9.8,
        "n": 6.9,
        "l": 6.5,
        "r": 6.4,
        "t": 5.6,
        "s": 4.9,
        "c": 4.5,
        "d": 3.7,
        "u": 3.2,
        "m": 2.9,
        "p": 3.0,
        "v": 2.1,
        "g": 1.6,
        "h": 0.6,
        "b": 1.0,
        "f": 1.1,
        "z": 1.0,
        "à": 0.2,
        "è": 0.2,
        "é": 0.2,
        "ì": 0.2,
        "ò": 0.2,
        "ù": 0.2,
    },
    "german": {
        "e": 17.4,
        "n": 9.8,
        "i": 7.6,
        "s": 7.3,
        "r": 7.0,
        "a": 6.5,
        "t": 6.2,
        "d": 5.1,
        "h": 4.8,
        "u": 4.3,
        "l": 3.4,
        "c": 3.1,
        "g": 3.0,
        "m": 2.5,
        "o": 2.5,
        "b": 1.9,
        "w": 1.9,
        "f": 1.7,
        "k": 1.2,
        "z": 1.1,
        "ä": 0.6,
        "ö": 0.4,
        "ü": 0.7,
        "ß": 0.3,
        "j": 0.3,
        "v": 0.8,
    },
    "dutch": {
        "e": 18.9,
        "n": 10.0,
        "a": 7.5,
        "t": 6.8,
        "i": 6.5,
        "r": 6.4,
        "o": 6.1,
        "d": 5.6,
        "s": 3.7,
        "l": 3.6,
        "g": 3.4,
        "v": 2.8,
        "h": 2.4,
        "k": 2.3,
        "m": 2.2,
        "u": 1.9,
        "b": 1.6,
        "p": 1.6,
        "w": 1.5,
        "j": 1.5,
        "z": 1.4,
        "f": 0.8,
        "c": 0.6,
        "x": 0.1,
        "y": 0.1,
        "é": 0.2,
        "è": 0.1,
        "ë": 0.1,
    },
    "swedish": {
        "e": 10.2,
        "a": 9.4,
        "n": 8.6,
        "t": 7.7,
        "r": 8.4,
        "s": 6.6,
        "l": 5.3,
        "d": 4.7,
        "o": 4.5,
        "i": 4.8,
        "m": 3.5,
        "g": 2.9,
        "k": 3.1,
        "v": 2.4,
        "h": 2.1,
        "u": 1.9,
        "f": 2.0,
        "b": 1.3,
        "p": 1.8,
        "å": 1.3,
        "ä": 1.8,
        "ö": 1.3,
        "y": 0.6,
        "j": 0.6,
    },
    "polish": {
        "a": 8.9,
        "i": 8.2,
        "e": 7.7,
        "o": 7.6,
        "z": 6.2,
        "n": 5.5,
        "r": 4.7,
        "w": 4.7,
        "y": 4.0,
        "c": 3.9,
        "l": 3.7,
        "t": 3.3,
        "s": 3.2,
        "d": 2.5,
        "k": 2.5,
        "p": 2.4,
        "m": 2.4,
        "u": 2.4,
        "j": 2.3,
        "b": 1.5,
        "g": 1.5,
        "ę": 1.1,
        "ł": 2.1,
        "ś": 0.8,
        "ń": 0.8,
        "ć": 0.8,
        "ó": 0.7,
        "ź": 0.3,
        "ż": 0.4,
    },
    "turkish": {
        "a": 12.9,
        "e": 8.6,
        "i": 8.3,
        "n": 7.9,
        "r": 6.7,
        "l": 6.0,
        "d": 5.2,
        "k": 4.7,
        "t": 3.6,
        "u": 3.2,
        "m": 3.0,
        "o": 2.9,
        "b": 2.8,
        "s": 2.7,
        "y": 2.7,
        "v": 2.4,
        "z": 1.5,
        "g": 1.3,
        "ç": 1.2,
        "ş": 1.2,
        "ğ": 1.1,
        "ı": 5.1,
        "ö": 0.8,
        "ü": 0.9,
        "c": 0.7,
        "h": 0.6,
        "f": 0.5,
        "j": 0.4,
        "p": 0.3,
    },
    "esperanto": {
        "a": 12.0,
        "e": 8.9,
        "i": 10.0,
        "o": 9.8,
        "u": 9.4,
        "n": 8.5,
        "l": 6.1,
        "s": 5.7,
        "r": 5.6,
        "t": 4.8,
        "k": 4.5,
        "m": 3.7,
        "d": 3.5,
        "p": 3.1,
        "v": 2.1,
        "g": 2.0,
        "b": 1.8,
        "f": 1.4,
        "h": 1.2,
        "ĉ": 1.0,
        "ĝ": 0.8,
        "ĵ": 0.5,
        "ŝ": 0.6,
        "ŭ": 0.3,
        "ĥ": 0.2,
        "z": 0.3,
        "c": 0.3,
        "j": 0.6,
    },
}
# endregion


def detectionLanguage(phraseUtilisateur):
    letter_count = {}
    total_letters = 0

    for char in phraseUtilisateur:
        if char.isalpha():
            total_letters += 1
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Calculer la fréquence des lettres dans le texte
    frequenceLettreParText = {
        char: (count / total_letters) * 100 for char, count in letter_count.items()
    }

    # Comparer avec les profils de langue
    best_match = "Aucune"
    smallest_difference = float("inf")

    for language, profile in LANGUAGE_PROFILES.items():
        difference = 0
        for char, freq in profile.items():
            text_freq = frequenceLettreParText.get(char, 0)
            difference += abs(freq - text_freq)

        # Met a jour la plus petite difference
        if difference < smallest_difference:
            smallest_difference = difference
            best_match = language

    return best_match


print(detectionLanguage(motUtilisateur))

""" Tips
difference entre reverse et reversed
reverse est une methode qui renvoie une liste inversée
reversed est une fonction qui renvoie un itérateur inversé
"""
