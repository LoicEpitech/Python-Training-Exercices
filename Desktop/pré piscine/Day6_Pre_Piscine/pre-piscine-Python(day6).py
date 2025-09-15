# Task 1.1


def f1():
    return 42


def f2(x):
    return 2 * x


print(f1())  # 42
print(f2(5) + f1())  # 2*5 + 42 Soit 52


# Task 1.2 & 1.3


def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


for i in range(1, 5):
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()


# Task 1.4


def nbSandwitch(nbToPrepare: int = 1):
    if nbToPrepare < 1:
        print("I can't do this!")
    for i in range(nbToPrepare):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()


nbSandwitch(2)

# Task 4.3


def isVegan():
    bread()
    lettuce()
    tomato()
    lettuce()
    tomato()
    bread()


def nbSandwitch(nbToPrepare: int = 1, veganOrNot: bool = False):
    if nbToPrepare < 1:
        print("I can't do this!")
    if veganOrNot == True:
        for i in range(nbToPrepare):
            isVegan()
    else:
        for i in range(nbToPrepare):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()


nbSandwitch(3, True)


# Task Challenge
def calcule():
    print(42**84)
    print(42**168)


# Task 2.1
def sumOneToNumber(nombre: int):
    if nombre <= 0:
        return 0
    return nombre + sumOneToNumber(nombre - 1)


print(sumOneToNumber(42))

# Task 2.2

import re
import unicodedata


def nettoyer_chaine(texte: str) -> str:
    texte = unicodedata.normalize(
        "NFD", texte
    )  # décompose les lettres accentuées en lettre + accent séparé.
    texte = "".join(
        c for c in texte if unicodedata.category(c) != "Mn"
    )  # enlève tous les accents, ne gardant que la lettre de base.

    texte = re.sub(r"[^a-zA-Z0-9]", "", texte)  # Supprimer tout sauf lettres/chiffres
    return texte.lower()


def isPalindrome(chainePalindrome: str):
    chainePalindrome.lower
    chainePalindrome = nettoyer_chaine(chainePalindrome)
    if len(chainePalindrome) <= 1:
        return True
    if chainePalindrome[0] != chainePalindrome[-1]:
        return False
    return isPalindrome(chainePalindrome[1:-1])


def palindromeRecursive():
    mot = input("Entrez votre palindrome: ")
    if isPalindrome(mot):
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")


palindromeRecursive()


# Task 2.3

arborescence = {
    "mon_projet": {
        "README.md": None,
        "main.py": None,
        "requirements.txt": None,
        "docs": {"introduction.md": None, "architecture.md": None},
        "src": {
            "utils.py": None,
            "data": {"dataset.csv": None, "preprocess.py": None},
            "models": {"model.py": None, "trainer.py": None},
        },
        "tests": {
            "test_main.py": None,
            "test_utils.py": None,
            "test_models": {"test_trainer.py": None},
        },
    }
}


def list_directorie(directorie: dict, prefix=""):
    for k, v in directorie.items():
        print(f"{prefix}{k}")
    if isinstance(v, dict):
        list_directorie(v, prefix + "  ")


list_directorie(arborescence)

# Task 3.1


def funA(n: int, s: str):
    if len(str(s)) >= n:
        return True
    else:
        return False


def funB(n: int, s: str):
    count = 0
    for Caract in s:
        if not (Caract.isalnum()):  # alpha-numérique
            count += 1
    if count >= n:
        return True
    else:
        return False


def funC(n: int, s: str):  # Nombre
    count = 0
    for Lettre in s:
        if Lettre.isdigit():
            count += 1
    if count >= n:
        return True
    else:
        return False


# Task 3.2 & 3.3
def passCheck(fun, nbNeeded: int, password: str):
    try:
        return fun(nbNeeded, password)
    except TypeError as e:
        print(f"Erreur de type dans la fonction {e}")


print(passCheck(funA, 16, "mysecretpassword"))
print(passCheck(funB, 3, "mysecretpassword"))
print(passCheck(funC, 1, "mysecretpassword"))
