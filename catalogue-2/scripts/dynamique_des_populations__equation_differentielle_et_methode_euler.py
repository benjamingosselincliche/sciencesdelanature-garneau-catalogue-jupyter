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
# # La dynamique des populations
# ---
# <div style="text-align: center;">
#     <div style="display: inline-block; position: relative; width: 350px;">
#         <img src="../img/_da709904-9305-4b95-a50f-3ac37b077133.jpeg" alt="Dessin" style="width: 100%;"/>
#         <p style="text-align: center; margin-top: 5px;">
#             <span style="font-style: italic; font-size: 16px;"> Course et destinée </span><br/>
#             <span style="font-style: italic; font-size: 12px;">Image générée par DALL·E 3, 2024 </span>
#         </p>
#     </div>
# </div>

# %% [markdown]
# ## Mise en contexte:
#
# ### La dynamique des populations:
#
# Pour prédire et comprendre la dynamique des populations, des modèles mathématiques avec équations différentielles sont utilisés. En général, celles-ci dépendent de nombreux facteurs et sont extrêmement complexes à modéliser. 
#
# Cela dit, certaines dynamiques "simples" peuvent être modélisées par des équations différentielles ordinaires (EDO). 
#
# - L'équation logistique de Verhulst: décription de la croissance d'une population en fonction du temps, en prenant en compte les limitations environnementales.
#
# - Les équations de Lotka-Volterra: 
#
#
#
# ### La méthode d'Euler:
# La méthode d'Euler est une technique numérique utilisée pour résoudre des équations différentielles ordinaires (EDO). 
#
# Voici un résumé de la méthode d'Euler :
#
# - Discrétisation du temps : La première étape de la méthode d'Euler consiste à diviser l'intervalle de temps en petits pas, ce qui crée une discrétisation du temps. Plus l'intervalle de temps est petit, plus l'approximation sera précise.
#
# - Condition initiale : la valeur initiale de la variable dépendante à un certain moment, c'est-à-dire la condition initiale, sert de point de départ pour résoudre l'EDO.
#
# - Approximation de la dérivée : À chaque pas de temps, vous approximez la dérivée de la variable dépendante en utilisant la valeur actuelle de la variable et l'EDO. La dérivée approximée est calculée en multipliant le taux de variation local par la taille du pas de temps.
#
# - Mise à jour de la variable dépendante : La nouvelle valeur de la variable dépendante est calculée en ajoutant la dérivée approximée à la valeur actuelle de la variable. Cela correspond à un pas de temps en avant.
#
# - Répétition : Les étapes 3 et 4 sont répétées pour chaque pas de temps jusqu'à ce que la variable atteigne la valeur finale souhaitée ou jusqu'à ce que le processus atteigne un certain nombre prédéfini d'itérations. C'est à cette étape que la technique de la boucle `for` est utilisé.

# %% [markdown]
# ## Objectifs
#
# - Utiliser une boucle `for` pour résoudre l'équation logistique de Verhulst avec la méthode d'Euler.
#
# - Utiliser une boucle `for` pour résoudre les équations de Lotka-Volterra avec la méthode d'Euler.

# %% [markdown]
# # L'équation logistique de Verhulst
# %% [markdown]
# L'équation logistique de Verhulst est un modèle mathématique largement utilisé pour décrire la croissance d'une population en fonction du temps, en prenant en compte les limitations environnementales. Cette équation tire son nom du mathématicien belge Pierre-François Verhulst, qui l'a développée au XIXe siècle pour modéliser la croissance de populations animales, mais elle est également couramment appliquée à d'autres domaines, notamment en écologie et en économie.
#
# L'équation logistique de Verhulst peut être formulée comme suit :
#
# $$
# \frac{dN(t)}{dt} = r \cdot N(t) \cdot \left(1 - \frac{N(t)}{K}\right)
# $$
# où :
# - $ \frac{dN(t)}{dt} $ représente le taux de croissance de la population par rapport au temps ($ t $).
# - $ N(t) $ est la taille de la population à un moment $t$.
# - $ r $ est le taux de croissance intrinsèque de la population, qui dépend des conditions environnementales et des caractéristiques de l'organisme.
# - $ K $ est la capacité de charge de l'environnement, c'est-à-dire la taille maximale que la population peut atteindre en fonction des ressources disponibles.
#
# Cette équation est souvent utilisée pour modéliser des situations où la croissance d'une population est limitée par des facteurs tels que la disponibilité de nourriture, d'espace ou d'autres ressources. Au fur et à mesure que la population ($ N $) augmente, le terme $ \left(1 - \frac{N}{K}\right) $ reflète la réduction de la croissance due à la saturation des ressources disponibles.
#
# Le modèle de Verhulst permet de comprendre comment une population peut atteindre un équilibre où la croissance cesse, car elle atteint sa capacité de charge. Ce modèle est également utile pour prédire les fluctuations de population dans des conditions environnementales changeantes.
#
# La méthode d'Euler utilise une logique itérative:
#
#    - À partir de $t = 0$, on répète les étapes jusqu'à ce que $t$ atteigne la valeur finale $T$:
#    - Calcul de la dérivée approximative $\frac{dN}{dt}$ pour la $n$-ième itération:
#      $$
#      \frac{dN}{dt} \approx r \cdot N_n \cdot \left(1 - \frac {N_n}{K}\right)
#      $$
#    - Mise à jour de $N$ en vue de la $n+1$-ième itération :
#      $$
#      N_{n+1} = N_n + \frac{dN}{dt} \cdot \Delta t
#      $$
#    - Incrémentation du temps : $t_{n+1} = t_n + \Delta t$.
#

# %%
# Initialisation des modules nécessaires:
import numpy as np
import matplotlib.pyplot as plt


# Méthode d'Euler: **Initialisation des variables** :

# Paramètres de l'équation logistique de Verhulst
r = 0.1  # Taux de croissance intrinsèque
K = 1000  # Capacité de charge de l'environnement
dt = .1  # Intervalle de temps
T = 200  # Durée de la simulation


# Méthode d'Euler: **Création des listes**

# Initialisation des listes pour stocker les données à chaque itération:
time_points = [0]  # temps initial
population = [10]  # Population initiale

# Méthode d'Euler: **Itération**

# Boucle for pour résoudre l'équation de Verhulst: 
# "for t" : C'est une boucle "for" en Python, qui itère sur une variable "t". À chaque itération, "t" prendra une nouvelle valeur.
# "in" : C'est le mot-clé "in" qui indique que nous allons itérer sur une séquence de valeurs.
# "np.arange(dt, T + dt, dt)" : C'est la séquence de valeurs sur laquelle nous itérons. "np.arange" crée un tableau de valeurs espacées de manière régulière. 
#  Dans ce cas, il génère une séquence de valeurs commençant à "dt" (la première valeur), se terminant à "T + dt" (la dernière valeur), avec un pas de "dt" (l'espacement entre les valeurs).
for t in np.arange(dt, T + dt, dt):
    # dNdt correspond au taux de variation.  
    dN_dt = r * population[-1] * (1 - population[-1] / K)
    N = population[-1] + dN_dt * dt
    time_points.append(t)
    population.append(N)


# Tracé du graphique de l'évolution de la population
plt.figure(figsize=(10, 6))
plt.plot(time_points, population)
plt.xlabel("Temps")
plt.ylabel("Population")
plt.title("Évolution de la population de bactéries (Équation de Verhulst)")
plt.grid()
plt.show()

# %% [markdown]
# # Les équations de Lotka-Volterra
# %%
# Initialisation des modules nécessaires:
import numpy as np
import matplotlib.pyplot as plt

# Paramètres des équations de Lotka-Volterra
r_N = 0.1  # Taux de reproduction intrinsèque des proies
a = 0.02  # Taux de prédation
r_P = 0.3  # Taux de décroissance intrinsèque des prédateurs
b = 0.01  # Efficacité de la prédation

# Conditions initiales
N0 = 40  # Population initiale de proies
P0 = 9   # Population initiale de prédateurs


# Intervalle de temps et nombre d'itérations
dt = 0.1
T = 200
num_iterations = int(T / dt)

# Initialisation des listes pour stocker les données
time_points = [0]
prey_population = [N0]
predator_population = [P0]


# Boucle for pour résoudre les équations de Lotka-Volterra avec la méthode d'Euler
for i in range(num_iterations):
    dN = (r_N * prey_population[-1] - a * prey_population[-1] * predator_population[-1]) * dt
    dP = (-r_P * predator_population[-1] + b * prey_population[-1] * predator_population[-1]) * dt

    N = prey_population[-1] + dN
    P = predator_population[-1] + dP

    time_points.append(time_points[-1] + dt)
    prey_population.append(N)
    predator_population.append(P)


# Tracé du graphique de l'évolution des populations de proies et de prédateurs
plt.figure(figsize=(10, 6))
plt.plot(time_points, prey_population, label='Population proies')
plt.plot(time_points, predator_population, label='Population prédateurs')
plt.xlabel("Temps")
plt.ylabel("Population")
plt.title("Dynamique des populations de proies et de prédateurs (Lotka-Volterra)")
plt.legend()
plt.grid()
plt.show()

# %%

# %%

# %%

# %%

# %%


# %%
