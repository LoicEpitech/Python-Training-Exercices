#Task 1.1 

laListe = [0, 1, 2, 3, 4, 5]
print(laListe[0])

#Task 1.2

print(laListe[-1])

#Task 1.3

laListe.append(42)
laListe.append("forty-two")

#Task 1.4

print(laListe)
for i in laListe:
    print(i)

#Task 1.5

laListe.pop()
print(laListe)

#Task 1.6

laListe.insert(0, -1)
print(laListe)

#Task 1.7

print(laListe[2:5])

#Task 1.8

reverseListe = []
reverseListe.append(laListe[::-1])
print(reverseListe)

#Task 1.9

print(laListe[::2])

#Task 1.10

for i in range(11, 22):
    laListe.append(i)
print(laListe)

#Task 1.11

my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list) Ajoute la seconde liste a la fin de la premiere

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list] La meme chose

#Task 2.1

uneListe = [1, 2, 3, 4, 5]
resultat = 1
for chiffre in uneListe:
    resultat *= chiffre
print(resultat)

#Task 2.2

a = [x + 10 for x in [3, 2, 6, 7, 1, 4]] Ajoute 10 a chaque nombre

#Task 2.3

list(filter(lambda x: x > 10, [42, 3, 4, 7])) filtre et garde seulement les nombres superieur a 10

#Task 2.4

uneListe = [1, 2, 3, 4, 5]
print(min(uneListe))
print(max(uneListe))

#Task 2.5

newListe = []
uneListe = [1, 2, 3, 4, 5]
for k in range(len(uneListe)):
    for i in uneListe:
        newListe.append(max(uneListe))
        uneListe.remove(max(uneListe))
print(newListe)

#Task 2.6

[x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]] multiplie les chiffres impaire par 2 et divise les chiffre paire par 2

#Task 2.7

[*enumerate([42, 3, 4, 18, 3, 10])] enumerate sert a avoir l'index de chaque element dans une liste

#Task 2.8

first_names = ["Jackie", "Chuck", "Arnold", "Sylvester"]
last_names = ["Stallone", "Schwarzenegger", "Norris", "Chan"]
magic = [*zip(first_names, last_names[::-1])] retourne la liste des noms et associe les prenoms dans l'ordre et les noms dans l'ordre inverse
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])


#Task Challenge
import random

listDeNombre = []
for i in range(1000000):
    listDeNombre.append(random.randint(1, 1000001))
listDeNombre = sorted(listDeNombre)
print(listDeNombre)

#Task 3.1

etudiante = {"Key": ["nomJoueur", "nomTeam"], "Value": ["ville", "numEtudiant"]}
etudianteTest = dict.fromkeys(etudiante["Key"], etudiante["Value"])
print(etudianteTest)

#Task 3.2 & #Task 3.3

superheroes = {
    " Batman ": {
        "id": 1,
        " aliases ": [" Bruce Wayne ", " Dark knight ", "Caped Crusade"],
        " location ": {
            " number ": 1007,
            " street ": " Mountain Drive ",
            " city ": " Gotham ",
        },
    },
    " Superman ": {
        "id": 2,
        " aliases ": ["Kal -El", " Clark Kent ", "The Man of Steel "],
        "location": {
            " number ": 344,
            " street ": " Clinton Street ",
            " apartment ": "3D",
            "city": " Metropolis ",
        },
    },
}
print(superheroes[" Superman "]["location"]["city"])

#Task 3.4

dictionaireTest = {
    " dalmatians ": 101,
    "pi": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10**100,
}
print(max(dictionaireTest, key=dictionaireTest.get))

#Task 4.1

nomDePersonne = input("Entrez votre nom: ")
nomAcces = ["Mike", "Noro", "Valentin"]
if nomDePersonne in nomAcces:
    print("Welcome in")
else:
    print("get lost !")

#Task 4.2

listNumber = [1, 1, 2, 2, 3]
listAlpha = ["a", 2, "a", 2, "A"]
print(set(listNumber))
print(set(listAlpha))

#Task 4.3

prenom = input("Entrez votre Prénom: ")

meeting = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

for ligne in meeting:
    if prenom in ligne:
        print(prenom + " vous avez une réunion le " + ligne[0] + " à " + ligne[1])
