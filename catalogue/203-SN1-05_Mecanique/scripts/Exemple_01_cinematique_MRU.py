# ---
# jupyter:
#   jupytext:
#     formats: ipynb,scripts//py:percent
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
# # Initialisation

# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from sklearn.linear_model import LinearRegression

# %% [markdown]
# <img src="./img/fig2.jpg" alt="Drawing" style="width: 300px;"/>

# %% [markdown]
# # Import data

# %%
# df = pd.read_csv("data/data_MRU.csv",sep = ';')
df = pd.read_excel("./fichiers_input/Exemple_01_cinematique_MRU_data.xlsx")
df

# %%
print('yo')

# %%
df.columns

# %%
df.dtypes

# %%
xdata = list(df["t"])
ydata = list(df["x"])
xdata

# %% [markdown]
# # Graphique 

# %%
# Création de l'objet graphique:
fig, ax = plt.subplots()

# Nuage de point:
ax.scatter(xdata, ydata)

# Titre:
ax.set_title("Position de l'objet en fonction du temps")

# Nom des axes:
ax.set_xlabel("t (s)")
ax.set_ylabel("x (m)")

# Domaine:
ax.set(xlim=(0, 0.7), ylim=(0, 30))

# Dimension de l'image:
width = 5
height = 4
fig.set_size_inches(width, height)

plt.savefig('graph1.pdf')
plt.show()

# %% [markdown]
# # Régression Linéaire

# %%
x = np.array(xdata).reshape((-1, 1))
y = np.array(ydata)

model = LinearRegression().fit(x,y)

a = model.coef_[0]
b = model.intercept_
r_sq = model.score(x, y)

print(f"pente: {a}")
print(f"ordonnée à l'origine: {b}")
print(f"coefficient of détermination R^2: {r_sq}")


# %% [markdown]
# # Analyse des pentes extrêmes

# %%
def fct_delta_a(a, b, x1, x2, delta_x1, delta_x2, delta_y1, delta_y2):
    y1 = a*x1+b
    y2 = a*x2+b
    return abs(a)*((delta_y2+delta_y1)/abs(y2-y1)+(delta_x2+delta_x1)/abs(x2-x1))
 
def fct_delta_b(a, delta_a, x1, delta_x1, delta_y1):
    return delta_y1 + abs(x1)*delta_a + abs(a)*delta_x1


# %%
x1, x2 = 0.05, 0.65
y1, y2 = a*x1+b, a*x2+b
delta_x1, delta_x2 = .01, .01,
delta_y1, delta_y2 = .5, .5

delta_a = fct_delta_a(a, b, x1, x2, delta_x1, delta_x2, delta_y1, delta_y2)
delta_b = fct_delta_b(a, delta_a, x1, delta_x1, delta_y1)

print(f"delta_a: {delta_a}")
print(f"delta_b: {delta_b}")

# %% [markdown] heading_collapsed=true
# # Graphique avec régression linéaire

# %% hidden=true
# Création de l'objet graphique:
fig, ax = plt.subplots()

plt.grid()

# Data:
ax.plot(xdata, ydata, 'o', color='black', markersize=4)

#Modele:
xmin, xmax = 0, 0.7
ax.plot([xmin, xmax], [a*xmin+b, a*xmax+b], 'b--', linewidth=1)

# Titre:
ax.set_title("Position de l'objet en fonction du temps")

# Nom des axes:
ax.set_xlabel("t (s)")
ax.set_ylabel("x (m)")

# Domaine:
ax.set(xlim=(0, 0.7), ylim=(0, 30))

# Dimension de l'image:
width = 5
height = 4
fig.set_size_inches(width, height)


plt.savefig('./fichiers_output/Exemple_01_cinematique_MRU_graphique_1.pdf')
plt.show()

# %% [markdown]
# # Graphique avec régression linéaire et pentes extrêmes 

# %%
# Création de l'objet graphique:
fig, ax = plt.subplots()

plt.grid()

# Nuage de point:
ax.plot([x1, x2], [y1, y2], 'b-', linewidth=1)
ax.plot([x1 + delta_x1, x2 - delta_x2], [y1 - delta_y1, y2 + delta_y2], 'g-', linewidth=1)
ax.plot([x1 - delta_x1, x2 + delta_x2], [y1 + delta_y1, y2 - delta_y2], 'r-', linewidth=1)
ax.plot(xdata, ydata, 'o', color='black', markersize=2)


ax.add_patch(Rectangle((x1 - delta_x1, y1 - delta_y1), 2*delta_x1, 2*delta_y1,
             edgecolor = 'black',
             fill=False,
             lw=1))
ax.add_patch(Rectangle((x2 - delta_x2, y2 - delta_y2), 2*delta_x2, 2*delta_y2,
             edgecolor = 'black',
             fill=False,
             lw=1))

# Titre:
ax.set_title("Position de l'objet en fonction du temps")

# Nom des axes:
ax.set_xlabel("t (s)")
ax.set_ylabel("x (m)")

# Domaine:
ax.set(xlim=(0, 0.7), ylim=(0, 30))

# Dimension de l'image:
width = 5
height = 4
fig.set_size_inches(width, height)


plt.savefig('./fichiers_output/Exemple_01_cinematique_MRU_graphique_2.pdf')
plt.show()

# %% [markdown] heading_collapsed=true
# # Graphique de comparaison

# %% hidden=true
aref = 40 
delta_aref = 1

agraph = a
delta_agraph = delta_a

# %% hidden=true
fig, ax = plt.subplots()
plt.grid()
ax.set_title('Graphique de comparaison')

data = np.array([[aref - delta_aref, agraph - delta_agraph],[aref + delta_aref, agraph + delta_agraph]])
ax.boxplot(data, showfliers=False, vert=False, labels = ["a_ref","a_graph"])

ax.set_xlabel("v (m/s)")


width = 8
height = 4
fig.set_size_inches(width, height)


ax.set(xlim=(35, 45))

plt.savefig('./fichiers_output/Exemple_01_cinematique_MRU_graphique_comparaison.pdf')

# %% hidden=true
