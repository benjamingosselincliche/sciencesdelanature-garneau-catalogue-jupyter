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

# %%
# Une boucle dans une boucle:
for i in range(3):
    for j in range(5):
        print(f'i = {i} ; j = {j}')  

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
# **Remarque: Il est important de s'assurer que la condition deviendra `False` à un moment donné pour éviter une boucle infinie non désirée.**  <br>

# %%
# Comptage jusqu'à 5 en utilisant une boucle while
count = 1
while count <= 5:
    print(count)
    count += 1

# %%
# Parcours d'une liste avec une boucle while (la fonction len() retourne la longueur de la liste)
liste = [1, "a", 3, "bd", 5]
index = 0
while index < len(liste):
    print(liste[index])
    index += 1

# %%
# Création d'une séquence de puissances de 2 jusqu'à ce qu'elles deviennent supérieures à 100
power_of_two = 1
while power_of_two <= 100:
    print(power_of_two)
    power_of_two *= 2

# %%
# Création d'une boucle infinie
# import time
# import sys

# i = 0
# while True:
#     # On fixe un délai de 1 seconde par itération pour ne pas surcharger la mémoire vive
#     time.sleep(1)
#     # On incrémente l'index
#     i += 1
#     print(f"Secondes écoulées = {i} s. La boucle ne s'arrêtera jamais. Il faut gérer la mémoire vive en conséquence. (Pour arrêter le processus, cliquer sur le bouton stop - interrupt the kernel) ",end='\r')


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
        print('Lift off!')
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

# %% [markdown]
# ---
# # Exemples appliqués:

# %% [markdown]
# ---
# ## Exemple 1 : la température d'une serre
# Dans cet exemple, on simule un système de contrôle de température dans une serre. Un capteur (thermomètre numérique) mesure la température à chaque minutes de la journée. Un système de contrôle de température obéit au commande suivante: 
# 1) mode "chauffage" si T <= 14 °C ;
# 2) mode "refroidissement" si T >= 28 °C ;
# 3) mode "inactif" si  14 °C < T < 28 °C. 
#
# Ainsi, une boucle `while` est utilisée pour que le processus fonctionne toute la journée. 

# %%
#Dans cette cellule, on importe des données qui simulent la température en fonction du temps
import pandas as pd
import numpy as np
import sys
from IPython.display import IFrame, clear_output

# Charger les données à partir du fichier CSV dans un DataFrame
df = pd.read_csv('donnees_temperature.csv')
print("-"*50)
print("Tableau de la température en fonction du temps:")
print(df)

# Convertir le DataFrame en un tableau NumPy
data = df.values

# Afficher le fichier PDF
print("-"*50)
print("Graphique:")
IFrame('variation_temperature.pdf', width=600, height=400)

# %%
#Dans cette cellule, on simule le processus du contrôle de température
import time
import matplotlib.pyplot as plt
import numpy as np

# Définition de la plage horaire (de minuit à minuit)
start_time = 0
end_time = 24 * 60  # Nombre de minutes dans une journée (1440 minutes)

# Définition de l'index pour la boucle while:
time_index = start_time

# Variables pour compter le nombre de minutes pour chaque état du système de contrôle de température et pour l'estimation du coût total
count_minute_chauffage = 0
count_minute_inactif = 0
count_minute_refroidissement = 0
puissance_systeme = 20  #kW
cout_kWh = 0.06 #$

# La boucle while exécute un processus pour la journée entière
while True:
    # On simule la mesure de la température avec un capteur:
    temperature_mesuree = data[time_index][1]

    # On fixe l'état du système de contrôle de température en fonction de la température mesurée et on compte le nombre de minute dans l'état:
    if temperature_mesuree <= 14:
        etat_systeme_temperature_controle = "chauffage"
        count_minute_chauffage += 1
    elif 14 < temperature_mesuree < 28:
        etat_systeme_temperature_controle = "inactif"
        count_minute_inactif += 1
    else:
        etat_systeme_temperature_controle = "refroidissement"
        count_minute_refroidissement += 1

    # On affiche le démarrage du système
    if time_index == 0:
        print(f'Le système a démarré à {time_index} min.' + '\n' + '-'*50)
        

    # On affiche dynamiquement le temps, la température mesurée et l'état du système de contrôle de température
    print(f'Temps: {data[time_index][0]} min ; Température : {data[time_index][1]:.3f} degré celsius ;  État système contrôle température : {etat_systeme_temperature_controle}'+' '*100, end='\r')

    # On simule un écoulement du temps (met en pause l'exécution du programme pendant 0.01 seconde et incrémente time_index)
    time.sleep(.01)
    time_index += 1

    # On affiche un message indiquant le rapport du système en fin de journée et on arrête l'exécution du programme:
    if time_index == end_time:
        #Calcul du cout d'utilisation
        nb_kWh = puissance_systeme*(count_minute_chauffage + count_minute_refroidissement)/60
        cout = cout_kWh*nb_kWh
        
        print(' '*100, end ='\r')
        print(f"Le système s'est arrêté à {time_index} min." + '\n' + '-'*50)
        print("Rapport système:")
        print("Le système de contrôle de température a fonctionné sans interruption aujourd'hui!")
        print(f'Nombre de minutes utilisées en mode "chauffage": {count_minute_chauffage} min')
        print(f'Nombre de minutes utilisées en mode "refroidissement": {count_minute_refroidissement} min')
        print(f'Nombre de minutes en mode "inactif": {count_minute_eteint} min')
        print(f'Énergie totale estimée: {nb_kWh:.2f} kWh')
        print(f'Coût total de fonctionnement estimé: {cout:.2f} $')
        # On termine la boucle. 
        break  


# %% [markdown]
# ---
# ## Exemple 2 : le triangle de Sierpinsky
#
# Le triangle de Sierpinski est un exemple classique d'une fractale. Les fractales sont des objets mathématiques ayant des formes géométriques complexes qui se répètent à différentes échelles (auto-similarité) et qui sont générées par des boucles itératives. 
#
# La création du triangle de Sierpinski implique :
#
# 1) Étape initiale : Définition d'un triangle équilatéral qui sert de racine.
#
# 2) Itération (ici une boucle `for`): À chaque itération, chaque triangle est divisé en trois triangles plus petits, et le processus se poursuit jusqu'à ce qu'on atteigne le niveau de détail souhaité (l'ordre du triangle).
#
# Le résultat est un motif fractal auto-similaire, où chaque partie de la figure ressemble à l'ensemble complet à une échelle plus petite. 

# %%
import matplotlib.pyplot as plt
import numpy as np
import time

def sierpinski_triangle(n_order):
    #Sommets de départ du triangle
    triangles_vertices = np.array([[[0, 0], [1, 0], [0.5, np.sqrt(3)/2]]])

    #Boucle for pour générer le triangle de Sierpinski d'ordre n_order
    for i in range(n_order):
        # Liste pour stocker les nouveaux sommets des triangles d'ordre i formés par les points milieux des triangles d'ordre i-1
        new_triangles_vertices = []
        # Boucle for sur les sommets des triangles d'ordre i-1
        for v0, v1, v2 in triangles_vertices:
            # Calcul des points milieux
            midpoints = [(v0 + v1) / 2, (v1 + v2) / 2, (v2 + v0) / 2]
            # Ajout des sommets des triangles d'ordre i avec la fusion de liste extend
            new_triangles_vertices.extend([(v0, midpoints[0], midpoints[2]), 
                                 (v1, midpoints[1], midpoints[0]), 
                                 (v2, midpoints[2], midpoints[1])])
        # Remplacement des sommets des triangles d'ordre i-1 par les nouveaux sommets des triangles d'ordre i
        triangles_vertices = new_triangles_vertices

    #La fonction retourne les sommets des triangles d'ordre n_order
    return triangles_vertices

    
def sierpinski_triangle_graph(n_order):

    # On appelle la fonction sierpinski_triangle:
    triangles_vertices = sierpinski_triangle(n_order)

    #Création de la figure:
    fig, ax = plt.subplots(figsize=(4, 4), dpi=120)
    ax.set_title(f'Triangle de Sierpinski : ordre {n_order}')
    ax.axis('equal')
    ax.axis('off')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 0.9660254037844386)

    #Boucle for pour tracer tous les triangles:
    for v0, v1, v2 in triangles_vertices:
        triangle = plt.Polygon([v0, v1, v2], closed=True, facecolor='black')
        ax.add_patch(triangle)

    plt.show()
    

# Appel de la fonction avec le nombre d'itérations (n_order) souhaité:
for n_order in range(9):
    sierpinski_triangle_graph(n_order)


# %%
# Appel de la fonction avec le nombre d'itérations (n_order) souhaité:
for n_order in range(9):
    t0 = time.time()
    sierpinski_triangle_graph(n_order)
    delta_time = time.time() - t0
    print(f"temps de calcul pour l'ordre {n_order} : {delta_time} s" +'\n'+'-'*50)

# %%
