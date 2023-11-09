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
# Démonstration sur les structures de contrôle avec Python
# ---
#
#

# %% [markdown]
# ## Objectifs:
# - Utiliser les structures de contrôle `if` `else` `elif`
# - Utiliser les opérateurs logiques booléens `and` `or` `True` `False` `not`
# - Utiliser les opérateurs de comparaison `>` `<` `<=` `>=` `==`  
#  Ce, afin de créer des programmes qui s'adaptent aux données et instructions fournies.
#
# ---
# Point d'ébullition de l'eau en fonction de l'altitude
# <div style="text-align: center; margin-top: 20px;">
#     <img src="./img/banner.webp" alt="Drawing" style="width: 300px;"/>
# </div>
# ---

# %% [markdown]
# ---
# ### Opérateurs de comparaison (`>` `<` `<=` `>=` `==`)
# Vous pouvez utiliser les opérateurs ci-haut pour comparer des valeurs dans des conditions.
# - `>` : Plus grand que
# - `<` : Plus petit que
# - `>=` : Plus grand ou égal à
# - `<=` : Plus petit ou égal à
# - `==` : Égal à

# %% [markdown]
# ### Structures de contrôle (`if` `else` `elif`)

# %% [markdown]
# Entrez l'altitude en mètres.  
# Ici, on utilise la fonction **Float()** pour transformer le texte entré par l'usager en donnée numérique

# %%
# Point d'ébullition de l'eau au niveau de la mer (en degrés Celsius)
ebullition_niveau_mer = 100 
altitude = 900  # Altitude en mètres

# %% [markdown]
# Pour exécuter du code de façon conditionnelle (dans un cas précis seulement) 
# vous pouvez utiliser le mot clé **If**.  
# Ici par exemple, le message d'erreur ne s'affiche que si l'altitude entrée est inférieur à 0.


# %%
# Changez la valeur de l'altitude et réévaluez cette cellule.
if altitude < 0:
    print("Erreur: L'altitude ne peut pas être négative.")

# %% [markdown]
# Pour gérer plus d'un cas possible, on utilise le mot clé **elif** pour else if (sinon si) 

# %%
# Changez la valeur de l'altitude pour 0 et réévaluez cette cellule
if altitude < 0:
    print("Erreur: L'altitude ne peut pas être négative.")
elif altitude == 0:
    print(f"Au niveau de la mer, l'eau bout à {ebullition_niveau_mer}°C.")

# %% [markdown]
# Pour gèrer les cas restant (ceux auxquel aucun condition ne s'applique) vous pouvez utiliser le mot clé **else**

# %%
# Changez la valeur de l'altitude pour 0 et réévaluez cette cellule
if altitude < 0:
    print("Erreur: L'altitude ne peut pas être négative.")
elif altitude == 0:
    print(f"Au niveau de la mer, l'eau bout à {ebullition_niveau_mer}°C.")
else:
    # Calcul du point d'ébullition
    # Le point d'ébullition de l'eau diminue d'environ 1 degré tous les 300 mètres d'altitude
    reduction_temp = altitude / 300
    point_ebullition = ebullition_niveau_mer - reduction_temp
    print(f"À une altitude de {altitude} mètres, l'eau bout à {point_ebullition:.2f}°C.")

# %% [markdown]
# ### Opérateurs booléens (`and` `or` `True` `False` `not`)

# %%
# Supposons que nous avons des conditions spéciales pour des expériences scientifiques
temperature_ideale = 97  # Température idéale pour une expérience
altitude_ideale_min = 901  # Altitude minimale idéale
altitude_ideale_max = 2500  # Altitude maximale idéale

# %% [markdown]
# Pour vérifier si deux conditions sont vraies en même temps, on utilise l'opérateur booléen **and**

# %%
# Il faut obligatoirement que les deux conditions soient évaluées comme vraies pour entrer dans le 'if'
if (altitude_ideale_min <= altitude <= altitude_ideale_max) and (point_ebullition <= temperature_ideale):
    print("L'altitude est idéale pour l'expérience scientifique.")
else:
    print("L'altitude n'est pas idéale pour l'expérience.")

# %% [markdown]
# Pour vérifier si **au moins une** des conditions est vraie, on utilise l'opérateur booléen **or**

# %%
# Tant qu'une des deux conditions est vraie, on entre dans le 'if'
if (point_ebullition == temperature_ideale) or (altitude == 0):
    print("Les conditions sont parfaites pour l'ébullition standard de l'eau ou une expérience idéale.")

# %% [markdown]
# Pour vérifier si une condition est fausse, on utilise l'opérateur booléen **not**

# %%
# Si la condition est évaluée à False, on entre dans le 'if'
if not (altitude_ideale_min <= altitude <= altitude_ideale_max):
    print("L'altitude est soit trop basse, soit trop haute pour effectuer des expériences.")

# %% [markdown]
# Toute expression booléenne peut être évaluée à `True` ou `False` (Vrai ou Faux).  
# Il est possible d'assigner ces valeurs à des variables ou de les utiliser directement dans des conditions.

# %%
# Assignation de valeurs booléennes à des variables
volcanAProximite = True
humiditeElevee = False
surUneMontagne = altitude >= 800

# Calculer le point d'ébullition de base en fonction de l'altitude
reduction_temp = altitude / 300
point_ebullition = ebullition_niveau_mer - reduction_temp

# %% [markdown]
# Comme ces valeurs sont des expressions booléennes, elles peuvent être utilisées directement dans des conditions.

# %%
# Ajuster le point d'ébullition en fonction des conditions spéciales
if volcanAProximite:
    # Près d'un volcan, le point d'ébullition pourrait être affecté par des gaz géothermiques
    point_ebullition += 1  # Hypothétique: Augmenter le point d'ébullition de 1 degré

if humiditeElevee and surUneMontagne:
    # Haute altitude combinée avec une humidité élevée pourrait augmenter le point d'ébullition
    point_ebullition += 0.5  # Hypothétique: Augmenter le point d'ébullition de 0.5 degré

# Changez les valeurs des conditions spéciales et réévaluez cette cellule
print(f"À une altitude de {altitude} mètres, l'eau bout à {point_ebullition:.2f}°C.")

# %%
