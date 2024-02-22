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
#     <img src="./img/bannerStructures.jpg" alt="Drawing"/>
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
