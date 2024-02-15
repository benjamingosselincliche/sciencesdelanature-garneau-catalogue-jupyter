# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Démonstration sur les boucles avec Python <br>
# ---
# <div style="text-align: center; margin-top: 20px;">
#     <img src="./img/banner.jpg" alt="Drawing"/>
# </div>


# %% [markdown]
# ---
# # Objectifs:
# - Utiliser les boucles `for` et `while` pour répéter des instructions.
# - Utiliser l'opérateur `break` pour sortir d'une boucle.
# - Utiliser l'opérateur `continue` pour passer à l'itération suivante d'une boucle.
# - Utiliser la fonction `range` pour générer une séquence d'entiers.
# Ce, afin de créer des programmes plus efficaces et modulaires.


# %% [markdown]
# ---
# # Boucle `for` (POUR)
# La boucle `for` est utilisée pour répéter un bloc de code un nombre spécifié de fois.          
# La syntaxe de base est la suivante: 
# ```python
# for variable in sequence:
#     # Bloc de code à répéter
# ```
# On peut traduire la boucle `for` par "POUR chaque élément de la séquence, exécutez le bloc de code".  <br>
# Par exemple, pour effectuer 10 fois une tâche spécifique, on peut utiliser la boucle suivante:
# ```python
# for i in range(10):
#  print(i)
# ```
# Dans cet exemple, `i` est la variable d'itération et `range(10)` est la séquence d'entiers de 0 à 9.  <br>
# On peut également utiliser la boucle `for` pour répéter un bloc de code pour chaque élément d'une liste ou d'un tuple.  <br>
# Tant que la séquence est itérable, la boucle `for` peut être utilisée pour répéter un bloc de code sur ses éléments.  <br>  

# %%
# Afficher les entiers de 0 à 9
for i in range(10):
    print(i)  
# %%
# Parcourir une chaîne de caractères et les afficher un par un
string = "Bonjour"
for char in string:
    print(char)

# %%
# Parcourir un dictionnaire et afficher les clés et les valeurs
person = {'nom': 'Jean', 'âge': 30, 'ville': 'Paris'}
for key, value in person.items():
    print(key + ':', value)

# %%
# Parcourir une liste avec l'index des éléments (fonction enumerate)
fruits = ['pomme', 'banane', 'orange']
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# %%
# Parcourir une liste avec un pas spécifique
for i in range(0, 10, 2):
    print(i)

# %% [markdown]
# ---
# # Boucle `while` (TANT QUE)
# La boucle `while` est utilisée pour répéter un bloc de code tant qu'une condition spécifiée est vraie.  <br>
# La syntaxe de base est la suivante:
# ```python
# while condition:
#     # Bloc de code à répéter
# ```
# On peut traduire la boucle `while` par "TANT QUE la condition est vraie, exécutez le bloc de code".  <br>
# La condition est une expression booléenne, cela signifie que le résultat de l'expression doit être `True` pour que le bloc de code soit exécuté.  <br>
# Par exemple, pour afficher les entiers de 0 à 9, on peut utiliser la boucle suivante:
# ```python
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# ```
# Dans    cet exemple, `i` est la variable d'itération et `i < 10` est la condition.  <br>
# **Remarque: Il est important de s'assurer que la condition deviendra `False` à un moment donné pour éviter une boucle infinie.**  <br>

# %%
# Comptage jusqu'à 5 en utilisant une boucle while
count = 1
while count <= 5:
    print(count)
    count += 1

# %%
# Parcours d'une liste avec une boucle while (la fonction len retourne la longueur de la liste)
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# %%
# Création d'une séquence de puissances de 2 jusqu'à ce qu'elles deviennent supérieures à 100
power_of_two = 1
while power_of_two <= 100:
    print(power_of_two)
    power_of_two *= 2



# %% [markdown]
# ---
# # Opération `break` (sortir de la boucle)
# Lorsque l'opération `break` est rencontrée, le programme sort de la boucle et exécute le code qui suit.  <br>
# L'opération `break` peut être utilisée dans les boucles `for` et `while`.  <br>


# %%
# Dans cet exemple, le programme affiche les entiers de 0 à 2, puis sort de la boucle lorsque `i` est égal à 3.
for i in range(10):
    if i == 3:
        break
    print(i)

# %%
# Boucle infinie avec une condition de sortie
x = 10
while True:
    print("Valeur actuelle de x :", x)
    x -= 1
    if x == 0:
        break

# %% [markdown]
# ---
# # Opération `continue` (passer à l'itération suivante)
# Lorsque l'opération `continue` est rencontrée, le programme passe à l'itération suivante de la boucle sans exécuter le code qui suit.  <br>
# L'opération `continue` peut être utilisée dans les boucles `for` et `while`.  <br>

# %%
# Dans cet exemple, le programme affiche les entiers de 0 à 9, sauf 5.
for i in range(10):
    if i == 5:
        continue
    print(i)

# %%
# Afficher uniquement les nombres pairs dans la plage de 1 à 10
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)
