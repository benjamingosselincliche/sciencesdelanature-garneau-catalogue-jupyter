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
# # Cinematique 1D
#
# Dans cet exemple, nous avons un enregistrement d'une position en fonction du temps. À partir de cet enregistrement, nous pouvons calculer la vitesse et l'accélération à l'aide la méthode des différences finies


# %% [markdown]
# ## Vitesse et accélération : définition analytique
#
# La vitesse $v$ d'un objet en mouvement, en fonction du temps $t$, est définie comme la dérivée première de sa position $s$ par rapport au temps. Mathématiquement, cela s'exprime comme suit :
#
# $$ v(t) = \frac{ds(t)}{dt} $$
#
# Cette équation indique que la vitesse instantanée à un instant donné $t$ est égale à la dérivée de la position $s$ par rapport au temps $t$. En d'autres termes, la vitesse représente la variation de la position par rapport au temps.
#
# L'accélération $a$, en fonction du temps $t$, est définie comme la dérivée première de la vitesse $v$ par rapport au temps. Mathématiquement, cela s'exprime comme suit :
#
# $$ a(t) = \frac{dv(t)}{dt} $$
#
# Cette équation indique que l'accélération instantanée à un instant donné $t$ est égale à la dérivée de la vitesse $v$ par rapport au temps $t$. En d'autres termes, l'accélération représente la variation de la vitesse par rapport au temps.
#
# # Vitesse et accélération : approximation numérique
#
# Les différences finies constituent une méthode numérique couramment utilisée pour approximer  les dérivées. Cette approche repose sur la discrétisation des grandeurs. 
#
# Considérons une séquence discrète de positions $s_i$ enregistrées à des instants $t_i$. La vitesse $v_i$ à l'instant $t_i$ peut être estimée en utilisant la différence finie centrale pour la dérivée première. La formule associée à cette estimation est la suivante :
#
# $$ v_i = \frac{s_{i+1} - s_{i-1}}{t_{i+1} - t_{i-1}} $$
#
# Cette formule exprime la pente du segment reliant les points $s_{i-1}$ et $s_{i+1}$. En utilisant cette méthode, la vitesse au point $t_i$ est ainsi calculée.
#
# Pour estimer l'accélération $a_i$ à l'instant $t_i$, la différence finie centrale peut être appliquée une nouvelle fois à la séquence des vitesses $v_i$ obtenues précédemment. La formule correspondante est la suivante :
#
# $$ a_i = \frac{v_{i+1} - v_{i-1}}{t_{i+1} - t_{i-1}} $$
#
# En d'autres termes, l'accélération est calculée comme la variation de la vitesse par rapport au temps, en prenant en compte les points voisins. 
#
# Il convient de souligner que l'efficacité de cette méthode dépend de la qualité des données expérimentales et de la finesse de la discrétisation temporelle. Des intervalles de temps trop grands peuvent introduire des erreurs significatives, tandis qu'une discrétisation fine peut augmenter la précision des résultats au prix d'une augmentation de la charge de calcul.
#
#

# %%
temps = []
position = []

# %%
with open("fichiers_input/Cinematique-1D-accandstop.txt", 'r') as fichier:

    for i in range(7):
        fichier.readline()

    lignes = fichier.readlines()
    for ligne in lignes:
        # Supprimez les caractères de nouvelle ligne et divisez la ligne en colonnes
        colonnes = ligne.strip().split()

        temps.append(float(colonnes[0]))
        position.append(float(colonnes[1]))


# %%
def derivee_premiere_difference_finie(liste_temps, liste_variable):

    derivee_premiere = []
    
    # Calcul de la dérivée première à l'aide de la différence finie
    for i in range(1, len(liste_temps)-1):
        delta_temps = liste_temps[i+1] - liste_temps[i-1]
        delta_variable = liste_variable[i+1] - liste_variable[i-1]

        derivee_premiere.append(delta_variable/delta_temps)

    return derivee_premiere

# %%
vitesse = derivee_premiere_difference_finie(temps, position)

# %%
print(len(vitesse))



# %%
import matplotlib.pyplot as plt
# Tracer le graphique
plt.plot(temps, position, label='Position en fonction du temps')
plt.xlabel('Temps')
plt.ylabel('Position')
plt.title('Graphique de la position en fonction du temps')
plt.legend()
plt.show()

# Tracer le graphique
plt.plot(temps[1:-1], vitesse, label='Vitesse en fonction du temps')
plt.xlabel('Temps')
plt.ylabel('Position')
plt.title('Graphique de la vitesse en fonction du temps')
plt.legend()
plt.show()


# %%
acceleration = derivee_premiere_difference_finie(temps[1:-1], vitesse)

# plt.plot(temps[2:-2], acceleration, label='Acceleration en fonction du temps')
# plt.xlabel('Temps')
# plt.ylabel('Position')
# plt.title("'Graphique de l'accélération en fonction du temps'")
# plt.legend()
# plt.show()


# %%
def moyenne_mobile(liste, fenetre):

    moyenne_mobile_tab = []

    for i in range(len(liste) - fenetre + 1):
        moyenne = sum(liste[i:i+fenetre]) / fenetre
        moyenne_mobile_tab.append(moyenne)

    return moyenne_mobile_tab

# %%
fenetre = 10
acceleration_lisse = moyenne_mobile(acceleration, fenetre)

# %%
print(len(acceleration))
print(len(acceleration_lisse))


# %%
plt.plot(acceleration_lisse, label='Acceleration en fonction du temps')
plt.show()

# %%
