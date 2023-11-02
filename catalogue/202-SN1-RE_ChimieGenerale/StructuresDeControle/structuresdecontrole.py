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
# # Point d'ébullition de l'eau
# Démonstration sur les structures de contrôle avec Python
# ---

# %% [markdown]
# <div style="text-align: center;">
#     <img src="./img/banner.webp" alt="Drawing" style="width: 300px;"/>
# </div>

# %% [markdown]
# ---
# ## Objectifs:
# - Utiliser les structures de contrôle `if` `else` `elif`
# - Utiliser les opérateurs logiques booléens `and` `or` `True` `False` `not`
# - Utiliser les opérateurs de comparaison `>` `<` `<=` `>=` `==`  
#  Ce, afin de créer des programmes qui s'adaptent aux données et instructions fournies.

# ---
# ## Démo Python : Point d'ébullition de l'eau en fonction de l'altitude
# ---
# ### Structures de contrôle (`if` `else` `elif`)

# %% [markdown]
# Entrez l'altitude en mètres.  
# Ici, on utilise la fonction **Float()** pour transformer le texte de l'usager en donnée numérique

# %%
# Point d'ébullition de l'eau au niveau de la mer (en degrés Celsius)
ebullition_niveau_mer = 100 
altitude = float(input("Entrez l'altitude en mètres (au-dessus du niveau de la mer): "))

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
# ---
# ### Opérateurs booléens (`and` `or` `True` `False` `not`)

# %%
# Supposons que nous avons des conditions spéciales pour des expériences scientifiques
temperature_ideale = 95  # Température idéale pour une expérience
altitude_ideale_min = 1500  # Altitude minimale idéale
altitude_ideale_max = 2500  # Altitude maximale idéale

