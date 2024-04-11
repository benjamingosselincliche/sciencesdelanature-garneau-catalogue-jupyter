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
# # Démonstration sur les structures de données avec Python <br>
# ---
# <div style="text-align: center; margin-top: 20px;">
#     <img src="../img/bannerStructures.jpg" alt="Drawing"/>
# </div>


# %% [markdown]
# ---
# # Objectifs:
# - Utiliser les `listes`
# - Utiliser les `tuples`
# - Utiliser les `dictionnaires`
# - Utiliser les `ensembles`
# - Utiliser les `tableaux` (Array)
# - Utiliser les `dataframes`    <br>
# Ce, afin de manipuler les données de manière efficace dans un programme.

# %% [markdown]
# ---
# # Les listes  <br>
# Une liste est une collection d'éléments ordonnée et modifiable.
# La syntaxe pour créer une liste est d'utiliser des crochets `[]` et séparer les éléments par des virgules `,`.<br>
# Exemple:
# ```python
# ma_liste = ["pomme", "banane", "fraise"]
# ```
# Elle est très **flexible** et peut contenir des éléments de différents types.<br>
# Elle est **modifiable**, c'est-à-dire que vous pouvez y changer, ajouter et supprimer des éléments.<br>
# Elle est **indexée**, c'est-à-dire que vous pouvez accéder à n'importe quel élément de la liste en utilisant son index.

# %%
# Création d'une liste des planètes du système solaire
planetes = ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]

# Affichage de la liste des planètes
print("Planètes du système solaire :", planetes)

# Accès à un élément spécifique de la liste (par exemple, la deuxième planète)
# Rappel : comme dans la pluspart des structures de données, le premier élément est à l'index 0
deuxieme_planete = planetes[1]
print("La deuxième planète est :", deuxieme_planete)

# Ajout d'une nouvelle (ancienne) planète à la fin de la liste
planetes.append("Pluton")

# Affichage de la liste mise à jour
print("Planètes du système solaire (avec Pluton) :", planetes)

# %% [markdown]
# ---
# # Les tuples  <br>
# Un tuple est une collection d'éléments ordonnée et **non modifiable**.
# La syntaxe pour créer un tuple est d'utiliser des parenthèses `()` et séparer les éléments par des virgules `,`.<br>
# Exemple:
# ```python
# mon_tuple = ("pomme", "banane", "fraise")
# ```
# Elle est très **flexible** et peut contenir des éléments de différents types.<br>
# Elle est **non modifiable**, c'est-à-dire que vous ne pouvez pas y changer, ajouter ou supprimer des éléments.<br>
# Elle est **indexée**, c'est-à-dire que vous pouvez accéder à n'importe quel élément du tuple en utilisant son index.

# %%
# Création d'un tuple représentant les caractéristiques de l'étoile Bételgeuse
etoile = ("Bételgeuse", "Rouge", 643, 1400, True)

# Affichage des informations sur l'étoile
print("Nom de l'étoile :", etoile[0])
print("Couleur de l'étoile :", etoile[1])
print("Distance de l'étoile à la Terre (en années-lumière) :", etoile[2])
print("Masse de l'étoile (en fois la masse du Soleil) :", etoile[3])
print("Est-ce que l'étoile est une supergéante ?", "Oui" if etoile[4] else "Non")

# %% [markdown]
# ---
# # Les dictionnaires  <br>
# Un dictionnaire est une collection d'éléments **non ordonnée**, **modifiable** et **indexée**.
#
# La syntaxe pour créer un dictionnaire est d'utiliser des accolades `{}` et séparer les éléments par des virgules `,`.<br>
# Les éléments d'un dictionnaire sont des **paires clé-valeur**, où chaque clé est unique.<br>
# *Note : les clés sont placées avant les valeurs, séparées par deux-points `:`*<br>
# Exemple:
# ```python
# mon_dictionnaire = {
#     "nom": "John",
#     "age": 30,
#     "ville": "New York"
# }
# ```
# Elle est très **flexible** et peut contenir des éléments de différents types.<br>
# Elle est **modifiable**, c'est-à-dire que vous pouvez y changer, ajouter et supprimer des éléments.<br>
# Elle est **indexée**, c'est-à-dire que vous pouvez accéder à n'importe quel élément du dictionnaire en utilisant sa clé.

# %%
# Création d'un dictionnaire représentant les caractéristiques de l'étoile Bételgeuse
etoile = {
    "nom": "Bételgeuse",
    "couleur": "Rouge",
    "distance": 643,
    "masse": 1400,
    "supergeante": True
}
# Affichage des informations sur l'étoile
print("Nom de l'étoile :", etoile["nom"])
print("Couleur de l'étoile :", etoile["couleur"])
print("Distance de l'étoile à la Terre (en années-lumière) :", etoile["distance"])
print("Masse de l'étoile (en fois la masse du Soleil) :", etoile["masse"])
print("Est-ce que l'étoile est une supergéante ?", "Oui" if etoile["supergeante"] else "Non")


# %% [markdown]
# ---
# # Les ensembles  <br>
# Un ensemble est une collection d'éléments **non ordonnée** et **non indexée**. <br>
# Les éléments d'un ensemble sont **uniques** et **non modifiables** (mais vous pouvez ajouter ou supprimer des éléments).<br>
# La syntaxe pour créer un ensemble est d'utiliser des accolades `{}` et séparer les éléments par des virgules `,`.<br>
# Exemple: 
# ```python
# mon_ensemble = {"pomme", "banane", "fraise"}
# ```
# Elle peut contenir des éléments de différents types.<br>
# Elle est **modifiable**, c'est-à-dire que vous pouvez y ajouter ou supprimer des éléments.<br>
# *Attention : les éléments d'un ensemble ne sont pas modifiables.*<br>
# Elle est **non indexée**, c'est-à-dire que vous ne pouvez pas accéder à un élément spécifique de l'ensemble directement.

# %%
# Création d'un ensemble de types d'étoiles observables dans une région du ciel
types_etoiles_region = {"Naine jaune", "Naine blanche", "Géante rouge", "Étoile à neutrons"}

# Affichage des types d'étoiles observables dans la région du ciel
print("Types d'étoiles observables dans la région du ciel :", types_etoiles_region)

# Ajout d'un nouveau type d'étoile à l'ensemble (par exemple, une supergéante)
types_etoiles_region.add("Supergéante")

# Vérification de la présence d'un type d'étoile spécifique dans l'ensemble (par exemple, une naine rouge)
if "Naine rouge" in types_etoiles_region:
    print("Les naines rouges sont présentes dans la région du ciel.")
else:
    print("Les naines rouges ne sont pas présentes dans la région du ciel.")

# Suppression d'un type d'étoile de l'ensemble (par exemple, une étoile à neutrons)
types_etoiles_region.remove("Étoile à neutrons")

# Affichage de l'ensemble mis à jour de types d'étoiles observables dans la région du ciel
print("Types d'étoiles observables dans la région du ciel (avec supergéante et sans étoile à neutrons) :", types_etoiles_region)

# %% [markdown]
# ---
# # Les tableaux  <br>
# Les tableaux ne sont pas nativement supportés par Python, mais vous pouvez utiliser des bibliothèques comme `numpy` pour les manipuler.<br>
# La majorité des langages de programmation supportent les tableaux et on les utilise réguliérement dans des contextes de calculs scientifiques.<br>
# Un tableau est une structure de données qui contient une collection **d'éléments de même type**.<br>
# On ne peut donc pas mélanger des types de données dans un tableau.<br>
# Les éléments d'un tableau sont **indexés** et **modifiables**.<br>
# Un tableau a normalement un taille fixe, mais dans certaines bibliothèques, comme `numpy`, on peut créer des tableaux de taille dynamique.<br>
# *Note : L'indexation des tableaux commence à 0*  <br>
# Exemple:
# ```python
# import numpy as np    # Importation de la bibliothèque numpy 
# mon_tableau = np.array([1, 2, 3, 4, 5])
# ```
# On peut visualiser le tableau précédent comme une liste ordonnée de nombres :<br>
# <table style="border: 1px solid black;">
#     <tr>
#         <th>1</th>
#         <th>2</th>
#         <th>3</th>
#         <th>4</th>
#         <th>5</th>
#     </tr>
# </table>


# %%
# Importation de la bibliothèque numpy
import numpy as np

# Création d'un tableau unidimensionnel des distances des étoiles à la Terre en années-lumière
distances_etoiles = np.array([4.24, 39.9, 25.3, 94.4, 4.37, 880])

# Affichage du tableau
print("Distances des étoiles à la Terre en années-lumière :", distances_etoiles)

# Accès à un élément spécifique du tableau (par exemple, la distance de la première étoile)
print("Distance de la première étoile à la Terre en années-lumière :", distances_etoiles[0])

# Calcul de la distance maximale
distance_maximale = np.max(distances_etoiles)
print("Distance maximale à la Terre en années-lumière :", distance_maximale)

# Calcul de la distance minimale
distance_minimale = np.min(distances_etoiles)
print("Distance minimale à la Terre en années-lumière :", distance_minimale)

# Calcul de la moyenne des distances
distance_moyenne = np.mean(distances_etoiles)
print("Distance moyenne à la Terre en années-lumière :", distance_moyenne)

# %% [markdown]
# ---
# # Les dataframes <br>
# Les **dataframes** sont des structures de données bidimensionnelles, similaires à des tableaux, mais avec des fonctionnalités supplémentaires vous permettant de manipuler et d'analyser les données plus facilement.<br>
# Cette structure de données est particulièrement utile pour représenter et manipuler des ensembles de données structurées où les lignes et les colonnes sont étiquetées.<br>
# Ils ne sont pas nativement supportés par Python, mais vous pouvez utiliser des bibliothèques comme `pandas` pour les utiliser.<br>
# Les dataframes sont très utilisés dans le domaine de la science des données et de l'analyse de données.<br>
# Ils sont très flexibles et peuvent contenir des éléments de différents types.<br>
# Ils sont **indexés** et **modifiables**.<br>
# Exemple:
# ```python
# import pandas as pd    # Importation de la bibliothèque pandas
# mon_dataframe = pd.DataFrame({
#     "nom": ["John", "Alice", "Bob"],
#     "age": [30, 25, 35],
#     "ville": ["New York", "Los Angeles", "Chicago"]
#
# })
# ```
# On peut voir le dataframe précédent comme un tableau avec des colonnes nommées :<br>
# <table style="border: 1px solid black;">
#     <tr>
#         <th>nom</th>
#         <th>age</th>
#         <th>ville</th>
#     </tr>
#     <tr>
#         <td>John</td>
#         <td>30</td>
#         <td>New York</td>
#     </tr>
#     <tr>
#         <td>Alice</td>
#         <td>25</td>
#         <td>Los Angeles</td>
#     </tr>
#     <tr>
#         <td>Bob</td>
#         <td>35</td>
#         <td>Chicago</td>
#     </tr>
# </table>


# %%
import pandas as pd

# Création d'un DataFrame pour stocker des informations sur des planètes
donnees_planetes = pd.DataFrame({
    "Nom": ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"],
    "Diamètre (km)": [4879, 12104, 12742, 6779, 139820, 116460, 50724, 49244],
    "Masse (10^24 kg)": [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102],
    "Distance moyenne au Soleil (millions de km)": [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]
})

# Affichage des données des planètes
print("Informations sur les planètes :\n", donnees_planetes)

# Affichage des informations sur la planète Mars
print("\nInformations sur la planète Mars :\n", donnees_planetes[donnees_planetes["Nom"] == "Mars"])

# Calcul de statistiques sur les données
statistiques = donnees_planetes.describe() 
print("\nStatistiques sur les données des planètes :\n", statistiques)

# Tri des planètes par diamètre décroissant
planetes_triees_par_diametre = donnees_planetes.sort_values(by="Diamètre (km)", ascending=False)
print("\nPlanètes triées par diamètre décroissant :\n", planetes_triees_par_diametre)

# Sélection des planètes dont le diamètre est supérieur à 10 000 km
planetes_grandes = donnees_planetes[donnees_planetes["Diamètre (km)"] > 10000]
print("\nPlanètes dont le diamètre est supérieur à 10 000 km :\n", planetes_grandes)

# Ajout d'une nouvelle colonne pour calculer la densité des planètes (masse / volume)
donnees_planetes["Densité (g/cm^3)"] = donnees_planetes["Masse (10^24 kg)"] / ((4/3) * 3.14159265359 * ((donnees_planetes["Diamètre (km)"]/2) ** 3))
print("\nInformations sur les planètes avec la nouvelle colonne de densité :\n", donnees_planetes)


# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

 
# Chargement des données sur les galaxies depuis un fichier CSV
donnees_etoiles = pd.read_csv("../data/hygdata_v37_propre.csv")

# Affichage des planêtes nommées (proper) et de leur distance (dist) à la Terre
print(donnees_etoiles[['proper','dist']])

#Tri des étoiles par distance croissante
etoiles_triees_par_distance = donnees_etoiles.sort_values(by="dist", ascending=True)

# Affichage des 10 étoiles les plus proches de la Terre
print("\n10 étoiles les plus proches de la Terre :\n", etoiles_triees_par_distance.head(10)[['proper','dist']])

# Création de la figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Sélection des 10 étoiles les plus proches du soleil
etoiles_plus_proches = etoiles_triees_par_distance.head(11)

# Affichage du soleil dans le graphique
leSoleil = etoiles_plus_proches[etoiles_plus_proches['proper'] == 'Sol']
ax.scatter(leSoleil['x'], leSoleil['y'], leSoleil['z'], c='yellow', s=400, alpha=0.7)

# Retirer le soleil de la liste
etoiles_plus_proches = etoiles_plus_proches[etoiles_plus_proches['proper'] != 'Sol']

# Affichage des étoiles dans l'espace 3D
ax.scatter(etoiles_plus_proches['x'], etoiles_plus_proches['y'], etoiles_plus_proches['z'], c='blue', s=50, alpha=0.7)

# Affichage des noms des étoiles et des lignes verticales
offset = 0
for i, txt in enumerate(etoiles_plus_proches['proper']):
    # Ajout d'un décalage pour les 3 premières étoiles pour éviter les superpositions des étiquettes
    if i < 3: 
        offset = 0.3*i
    else: 
        offset = 0

    ax.text(etoiles_plus_proches['x'].iloc[i]-0.2, etoiles_plus_proches['y'].iloc[i], etoiles_plus_proches['z'].iloc[i]-offset, txt, fontsize=8)
    ax.plot([etoiles_plus_proches['x'].iloc[i], etoiles_plus_proches['x'].iloc[i]], 
            [etoiles_plus_proches['y'].iloc[i], etoiles_plus_proches['y'].iloc[i]], 
            [etoiles_plus_proches['z'].iloc[i], -3], 
            color='black', linestyle='--')

# Configuration des étiquettes
ax.set_title("Les 10 étoiles les plus proches du soleil", fontsize=14)  # Titre du diagramme
ax.set_xlabel("X (parsecs)", fontsize=12)  # Nom de l'axe X avec l'unité
ax.set_ylabel("Y (parsecs)", fontsize=12)  # Nom de l'axe Y avec l'unité
ax.set_zlabel("Z (parsecs)", fontsize=12)  # Nom de l'axe Z avec l'unité

ax.set_xlim(-3, 3)  # Modifier les limites X selon vos besoins
ax.set_ylim(-3, 3)  # Modifier les limites Y selon vos besoins
ax.set_zlim(-3, 3)  # Modifier les limites Z selon vos besoins

# Changer l'orientation de la boîte
ax.view_init(elev=30, azim=60)  # Par exemple, vous pouvez changer les angles selon vos préférences

plt.tight_layout()
plt.show()

# %%
