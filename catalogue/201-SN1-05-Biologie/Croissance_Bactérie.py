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
# # La dynamique des populations BLA
# ---

# %%
import numpy as np
import matplotlib.pyplot as plt


# %% [markdown]
# # L'équation logistique de Verhulst
# %%
# Paramètres de l'équation logistique de Verhulst
r = 0.1  # Taux de croissance intrinsèque
K = 1000  # Capacité de charge de l'environnement
dt = 0.1  # Intervalle de temps
T = 200  # Durée de la simulation

# %%
# Initialisation des listes pour stocker les données
time_points = [0]
population = [10]  # Population initiale

# %%
# Boucle for pour résoudre l'équation de Verhulst avec la méthode d'Euler
for t in np.arange(dt, T + dt, dt):
    dN = r * population[-1] * (1 - population[-1] / K)
    N = population[-1] + dN * dt
    time_points.append(t)
    population.append(N)

# %%
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
# Paramètres des équations de Lotka-Volterra
r_N = 0.1  # Taux de reproduction intrinsèque des proies
a = 0.02  # Taux de prédation
r_P = 0.3  # Taux de décroissance intrinsèque des prédateurs
b = 0.01  # Efficacité de la prédation

# %%
# Conditions initiales
N0 = 40  # Population initiale de proies
P0 = 9   # Population initiale de prédateurs

# %%
# Intervalle de temps et nombre d'itérations
dt = 0.1
T = 200
num_iterations = int(T / dt)

# %%
# Initialisation des listes pour stocker les données
time_points = [0]
prey_population = [N0]
predator_population = [P0]

# %%
# Boucle for pour résoudre les équations de Lotka-Volterra avec la méthode d'Euler
for i in range(num_iterations):
    dN = (r_N * prey_population[-1] - a * prey_population[-1] * predator_population[-1]) * dt
    dP = (-r_P * predator_population[-1] + b * prey_population[-1] * predator_population[-1]) * dt

    N = prey_population[-1] + dN
    P = predator_population[-1] + dP

    time_points.append(time_points[-1] + dt)
    prey_population.append(N)
    predator_population.append(P)

# %%
# Tracé du graphique de l'évolution des populations de proies et de prédateurs
plt.figure(figsize=(10, 6))
plt.plot(time_points, prey_population, label='Proies')
plt.plot(time_points, predator_population, label='Prédateurs')
plt.xlabel("Temps")
plt.ylabel("Population")
plt.title("Dynamique des populations de proies et de prédateurs (Lotka-Volterra)")
plt.legend()
plt.grid()
plt.show()

