# Task 1.2
num = int(input("Entrez un nombre entier: "))
if num == 42:
    print("This is correct !")
else:
    print("This isn't correct !")

# Task 1.3
num = int(input("Entrez un nombre entier: "))
if num % 2 == 0:
    print("This integer is odd !")
else:
    print("This integer is even !")

# Task 1.4
mot = input("Entrez un mot: ")
if mot == "open sesame":
    print("access granted")
else:
    if mot == "will you open, you goddamn !@&/°":
        print("access fucking granted")
    else:
        print("permission denied")

# Task 1.5
num = int(input("Entrez un numero: "))
if num == 42:
    print("a")
elif num <= 21:
    print("b")
elif num % 2 == 0:
    print("c")
elif num / 2 > 21:
    print("d")
elif num % 2 != 0 and num >= 45:
    print("e")
else:
    print("f")

# Task 1.6
a = 42
b = 41
if a == b:
    print("A and B is the sames ")
if b <= a:
    print("B is equal or lower as A")
if b != a:
    print("B his diferent from A")

# Task 2.1
for i in range(1, 1001):
    print(i)

# Task 2.2
chaine = " "
for i in input("Entrez un mot: "):
    chaine = chaine + i + i
print(chaine)

# Task 2.3
i = 10000
while i != 1:
    i = i - 1
    if i % 7 == 0:
        print(i)

# Task 2.4
i = -30
while i != 30:
    i = i + 1
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# Task 2.5
n_bottles = 99
for n in range(n_bottles, 0, -1):
    print(f"{n} bottles of beer on the wall.")
    print(f"{n} bottles of beer.")
    print("Take one down, pass it around,")
    print(f"{n-1} bottles of beer on the wall\n")

print("No more bottles of beer on the wall,")
print("no more bottles of beer.")
print("Go to the store and buy some more,")
print("99 bottles of beer on the wall...")

# Task 2.6
n = int(input("Entrez un nombre: "))
for i in range(2, n // 2 + 1):
    multiples = []
    for j in reversed(range(n)):
        if j % i == 0 and j != 0:
            multiples.append(j)
    print(multiples)

# Task challenge
voyelle = ["a", "e", "i", "o", "y", "u"]
ChaineUtilisateur = input("Entrez une chaine et un nombre: ").lower()
espace = ChaineUtilisateur.split(maxsplit=1)
possedeUneVoyelle = False
num = int(espace[1])
for i in espace[0]:
    if voyelle.__contains__(i):
        print(num)
        possedeUneVoyelle = True
        break
if num >= 42 and not possedeUneVoyelle:
    print(num)
elif not possedeUneVoyelle:
    print(espace[0])

# Task 3.1
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
tableau = []
chaine = input("Entrez une chaine de caractere: ").lower()
key = int(input("Entrez une cle: "))

for i in range(len(chaine)):
    for j in range(len(alphabet)):
        if chaine[i] == alphabet[j]:
            position = j
            new_position = (position + key) % 26
            tableau.append(alphabet[new_position])
            break
print("".join(tableau))


# Task 3.2
def decriptageCesar(key, chaine):
    texte = ""
    espaces = []
    for indexDuCaractere, char in enumerate(chaine):
        if char == " ":
            espaces.append(indexDuCaractere)
    chaine_sans_espaces = chaine.replace(" ", "").lower()
    for i in chaine_sans_espaces:
        position = alphabet.index(i)
        new_position = (position - key) % 26
        texte = texte + alphabet[new_position]
    texte_liste = list(texte)
    for indexDuCaractere in espaces:
        texte_liste.insert(indexDuCaractere, " ")
    return "".join(texte_liste)


chaine = input("Entrez une chaine de caractere: ").lower().re
for k in range(1, len(alphabet) + 1):
    print(f"Key {k}: ={decriptageCesar(k, chaine)}")

# Task 3.3
texte = input("Entrez un texte: ").lower()
cleTexte = input("Entrez un cle: ").lower()


def cryptageVigenere(texte, cleTexte):
    if len(texte) != len(cleTexte):
        return "Erreur: Le texte et la clé doivent avoir la même longueur."
    texteFinal = ""
    for i, l in enumerate(texte):
        position = alphabet.index(l)
        clePosition = alphabet.index(cleTexte[i])
        new_position = (position + clePosition) % 26
        texteFinal = texteFinal + alphabet[new_position]
    return texteFinal

print(cryptageVigenere(texte, cleTexte))


# Task 3.4
texte = input("Entrez un texte: ").lower()


def decriptageVigenere(texte, cleTexte):
    if len(texte) != len(cleTexte):
        return "Erreur: Le texte et la clé doivent avoir la même longueur."
    texteFinal = ""
    for i, l in enumerate(texte):
        position = alphabet.index(l)
        clePosition = alphabet.index(cleTexte[i])
        new_position = (position - clePosition) % 26
        texteFinal = texteFinal + alphabet[new_position]
    return texteFinal


def touteLessCles(longueurCle):
    combinaison = [""]
    for i in range(longueurCle):
        listeCle = []
        for prefixe in combinaison:
            for lettre in alphabet:
                listeCle.append(prefixe + lettre)
        combinaison = listeCle
    return combinaison


longueurCle = len(texte)
for i in range(longueurCle):
    for cle in touteLessCles(longueurCle):
        i = 1 + i
        print(f"Key numero {i} {cle} = {decriptageVigenere(texte,cle)}")
