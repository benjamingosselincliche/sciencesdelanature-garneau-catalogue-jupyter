# ---
# jupyter:
#   jupytext:
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
# # Modèles et données
# ---

# %% [markdown]
# <div style="text-align: center;">
#     <div style="display: inline-block; position: relative; width: 350px;">
#         <img src="../img/_4c492367-b76e-4fc2-b295-5a1cd0fad49b.jpeg" alt="Dessin" style="width: 100%;"/>
#         <p style="text-align: center; margin-top: 5px;">
#             <span style="font-style: italic; font-size: 16px;"> Fit Global</span><br/>
#             <span style="font-style: italic; font-size: 12px;">Image générée par DALL·E 3, mars 2024 </span>
#         </p>
#     </div>
# </div>
#

# %% [markdown]
# ---
# ## Mise en contexte
#
# ### Principe fondamental 
#
# Un principe fondamental de la science empirique consiste à apposer un modèle $M$ sur un ensemble de données $D$. Classiquement, l'ensemble de données $D$ consiste en un ensemble de données expérimentales, c'est-à-dire des valeurs mesurées, et le modèle $M$ est une fonction mathématique d'une ou plusieurs variables, comprenant un ou plusieurs paramètres. 
#
# L'idée est de déterminer la valeur numérique de chaque paramètres du modèle $M$ qui fait en sorte que celui-ci correspond le mieux à l'ensemble de données $D$. Plus précisement, il s'agit d'appliquer une méthode d'optimisation qui minimise une certaine fonction de coût qui représente les différences entre les valeurs prédites par le modèle et les valeurs réelles des données (généralement appelées les résidus). Une méthode courante est la méthode des moindres carrés. Les paramètres optimaux seront ceux qui minimisent la somme des carrés des résidus.      
#
# Aussi, des méthodes statistiques complexes, impliquant la matrice de covariance, permettent de calculer une incertitude associée à ces paramètres. Il est également possible de calculer des mesures de performance tel que le coefficient de détermination $R^2$. Plus $R^2$ est proche de 1, meilleure est l'adéquation du modèle aux données.
#
# Ayant alors établit ce modèle $M$, celui-ci peut être utilisé pour effectuer des prédictions, tant pour les phénomènes naturels que pour le contrôle technologique. C'est exactement le même principe qui est appliqué dans les algorithmes d'apprentissage machine à la base de l'intelligence artificielle. 
#
# ###  Librairie scipy et la méthode curve_fit
#
# Pour n'importe quel ensemble de donnée de ce notebook, la méthode est la suivante:
#
# 1. **Définition du modèle** :
#    Nous définissons une fonction appelée `modele`. Cette fonction prend $n$ variables ($x$, $y$, $t$, etc.) et $p$ paramètres ($a$, $b$, $alpha$, etc). 
#
# 2. **Générer des données factices** :
#    En principe l'ensemble de données $D$ est importé depuis un fichier. Dans ce notebook, l'ensemble des données est simulé. 
#
# 3. **Ajustement de courbe** :
#    Nous utilisons la fonction `curve_fit` de la bibliothèque Scipy pour ajuster notre modèle aux données. Cette fonction retourne deux valeurs : `popt`, qui contient les paramètres optimaux du modèle, et `pcov`, qui est la matrice de covariance contenant des informations sur les incertitudes sur ces paramètres.
#
# 4. **Paramètres optimaux** :
#    Nous extrayons les paramètres optimaux `a_fit` et `b_fit` à partir de `popt`. Ces valeurs représentent les paramètres optimaux du modèle qui ont été trouvés par l'ajustement du modèle aux données.
#
# 5. **Calcul des incertitudes sur les paramètres optimaux** :
#    Nous calculons les incertitudes sur les paramètres optimaux  à partir de la matrice de covariance `pcov`. Pour ce faire, nous extrayons les écarts types des paramètres de la diagonale de la matrice de covariance en utilisant la fonction `np.sqrt(np.diag(pcov))`.
#
# 6. **Prédiction du modèle** :
#    Nous utilisons les paramètres ajustés `a_fit` et `b_fit` pour prédire les valeurs de `y` en utilisant notre modèle linéaire. Les valeurs prédites sont stockées dans `y_pred`.
#

# %% [markdown]
# ---
# # Objectifs:
# - Comprendre la méthode générale
# - Utiliser la librairie scipy et la méthode curve_fit
#

# %% [markdown]
# ---
# ## Exemple 1: Modèle linéaire
#
# Un grand nombre de phénomène sont représentés par un modèle linéaire simple. Ce modèle est une droite de type $f(x) = ax + b$. La variable indépendante est $x$ et la variable dépendante est $y=f(x)$. L'ensemble des données est donc un tableau $y$ en fonction de $x$. Les paramètres $a$ et $b$ sont respectivement la pente et l'ordonnée à l'origine.    
#
#

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -------------------------------------------------------------------------------------------
# Définition du modèle: 
def modele_lineaire(x, a, b):
    """
    Modèle : 
        f(x) = ax + b
    variable indépendante: 
        x
    variable dépendante: 
        y = f(x) 
    paramètres: 
        a, b 
    """
    return a * x + b

# -------------------------------------------------------------------------------------------
# Génération d'un ensemble de données factices (les valeurs numérique peuvent être changé pour tester la méthode. Par exemple, la variable scale permet de rendre les données de plus en plus bruitées.)
np.random.seed(0)
x_data = np.linspace(.1, 9.8, 50)
y_data = 2 * x_data + 3 + np.random.normal(scale=1, size=x_data.size)  # Ajout de bruit gaussien
incertitude_x = 0.2  # Incertitude sur x_data
incertitude_y = 0.5  # Incertitude sur y_data

# -------------------------------------------------------------------------------------------
# Ajustement du modèle 
popt, pcov = curve_fit(modele_lineaire, x_data, y_data)

# Paramètres optimaux obtenus:
a_fit, b_fit = popt

# -------------------------------------------------------------------------------------------
# Calcul des incertitudes sur les paramètres optimaux
a_uncertainty, b_uncertainty = np.sqrt(np.diag(pcov))

# -------------------------------------------------------------------------------------------
# Calcul du coefficient de détermination
y_pred = modele_lineaire(x_data, a_fit, b_fit) # Prédiction du modèle
y_mean = np.mean(y_data)
r_squared = 1 - np.sum((y_data - y_pred)**2) / np.sum((y_data - y_mean)**2)

# -------------------------------------------------------------------------------------------
# Affichage des résultats
print(f"Paramètres optimaux: a={a_fit}, b={b_fit}")
print(f"Incertitude sur les paramètres optimaux: delta_a={a_uncertainty}, delta_b={b_uncertainty}")
print(f"Coefficient de détermination R²: {r_squared}")

# Visualisation des données et du modèle
plt.errorbar(x_data, y_data, xerr=incertitude_x, yerr=incertitude_y, fmt='o', label='Données')
plt.plot(x_data, modele_lineaire(x_data, a_fit, b_fit), color='red', label='Modèle optimal')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 10)  # Remplacez min_x_value et max_x_value par vos valeurs minimale et maximale pour l'axe X
plt.ylim(0, 25) 
plt.legend()
plt.grid(True)
plt.show()

# %% [markdown]
# ---
# ## Exemple 2: Modèle polynomial
#
# Le modèle linéaire est un polynôme d'ordre 1. La même méthode s'applique pour un polynôme d'ordre quelconque. Nous considérons ici un polynôme d'ordre 2 : $f(x) = ax^2 + bx + c$.    
#

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modele_polynome_ordre_2(x, a, b, c):
    """
    Modèle : 
        f(x) = ax^2 + bx + c
    variable indépendante: 
        x
    variable dépendante: 
        y = f(x) 
    paramètres: 
        a, b, c 
    """
    return a * x**2 + b * x + c

# -------------------------------------------------------------------------------------------
# Génération d'un ensemble de données factices 
np.random.seed(0)
x_data = np.linspace(0, 10, 40)
y_data = 2.5 * x_data**2 - 15 * x_data + 35 + np.random.normal(scale=2, size=x_data.size)
incertitude_x = 0.2  # Incertitude sur x_data
incertitude_y = 10  # Incertitude sur y_data

# -------------------------------------------------------------------------------------------
# Ajustement du modèle 
popt, pcov = curve_fit(modele_polynome_ordre_2, x_data, y_data)

# Paramètres optimaux obtenus:
a_fit, b_fit, c_fit = popt

# -------------------------------------------------------------------------------------------
# Calcul des incertitudes sur les paramètres optimaux
a_uncertainty, b_uncertainty, c_uncertainty = np.sqrt(np.diag(pcov))

# -------------------------------------------------------------------------------------------
# Calcul du coefficient de détermination
y_pred = modele_polynome_ordre_2(x_data, a_fit, b_fit, c_fit) # Prédiction du modèle
y_mean = np.mean(y_data)
r_squared = 1 - np.sum((y_data - y_pred)**2) / np.sum((y_data - y_mean)**2)

# -------------------------------------------------------------------------------------------
# Affichage des résultats
print(f"Paramètres optimaux: a={a_fit}, b={b_fit}, b={c_fit}")
print(f"Incertitude sur les paramètres optimaux: delta_a={a_uncertainty}, delta_b={b_uncertainty}, delta_c={b_uncertainty}")
print(f"Coefficient de détermination R²: {r_squared}")

# Visualisation des données et du modèle
plt.errorbar(x_data, y_data, xerr=incertitude_x, yerr=incertitude_y, fmt='o', label='Données')
plt.plot(x_data, modele_polynome_ordre_2(x_data, a_fit, b_fit, c_fit), color='red', label='Modèle optimal')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 10)  # Remplacez min_x_value et max_x_value par vos valeurs minimale et maximale pour l'axe X
plt.ylim(0, 150) 
plt.legend()
plt.grid(True)
plt.show()

# %%

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -------------------------------------------------------------------------------------------
def modele_oscillation_amortie(t, A_0, omega, gamma, phi):
    """
    Modèle d'oscillation amortie :  x(t) = A_0 * exp(-gamma/2 * t) * cos(omega * t + phi) 
        Variable indépendante:
            t : temps
        Variable dépendante:
            x : position
        Paramètres:
            A_0 : amplitude initiale
            omega : fréquence angulaire
            gamma : taux d'amortissement
            phi : phase initiale
    """
    return A_0 * np.exp(-gamma/2 * t) * np.cos(omega * t + phi)

# -------------------------------------------------------------------------------------------
# Générer des données factices pour l'oscillation amortie
# -------------------------------------------------------------------------------------------
A_0_true = 5.0
omega_true = 2.0
gamma_true = 0.2
phi_true = np.pi / 4
np.random.seed(0)
t_data = np.linspace(0, 10, 100)
y_data = modele_oscillation_amortie(t_data, A_0_true, omega_true, gamma_true, phi_true) + np.random.normal(scale=0.1, size=t_data.size)

# Générer des incertitudes pour les données temporelles
uncertainty_t = np.abs(np.random.normal(scale=.2, size=t_data.size))  # Incertitude de 0.05 unités de temps

# Générer des incertitudes pour les données d'amplitude
uncertainty_y = np.abs(np.random.normal(scale=.2, size=y_data.size))  # Incertitude de 0.1 sur les données d'amplitude


# -------------------------------------------------------------------------------------------
# Réaliser l'ajustement de courbe en tenant compte des incertitudes sur les données d'amplitude et de temps
popt, pcov = curve_fit(modele_oscillation_amortie, t_data, y_data, sigma=uncertainty_y, absolute_sigma=True, p0=[A_true, omega_true, gamma_true, phi_true])

# Paramètres ajustés
A_fit, omega_fit, gamma_fit, phi_fit = popt

# Incertitudes sur les paramètres
A_uncertainty, omega_uncertainty, gamma_uncertainty, phi_uncertainty = np.sqrt(np.diag(pcov))

# -------------------------------------------------------------------------------------------
# Affichage des résultats
print(f"Paramètres ajustés: A={A_fit}, omega={omega_fit}, gamma={gamma_fit}, phi={phi_fit}")
print(f"Incertitudes sur les paramètres: A={A_uncertainty}, omega={omega_uncertainty}, gamma={gamma_uncertainty}, phi={phi_uncertainty}")

# -------------------------------------------------------------------------------------------
# Visualisation des données et de l'ajustement
plt.errorbar(t_data, y_data, yerr=uncertainty_y, xerr=uncertainty_t, fmt='o', label='Données')
plt.plot(t_data, modele_oscillation_amortie(t_data, *popt), 'r-', label='Modèle ajusté')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.legend()
plt.show()



# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Afct(omega, Ae, Q, omega0):
    """
    Modèle d'amplitude en fonction de la fréquence :
    Ae : amplitude de l'oscillateur non forcé
    Q : facteur de qualité
    omega0 : fréquence propre
    omega : fréquence du forçage
    """
    return Ae * (omega0 / omega) / (np.sqrt((omega0 / omega - omega / omega0)**2 + 1 / Q**2))

# Générer des données factices pour l'amplitude en fonction de la fréquence
np.random.seed(0)
omega_data = np.linspace(1, 6, 50)
Ae_true = 1.0
omega0_true = 2.0
Q_true = 10
amplitude_data = Afct(omega_data, Ae_true, Q_true, omega0_true) + np.random.normal(scale=0.1, size=omega_data.size)

# Ajouter des incertitudes sur les données d'amplitude
uncertainty_amplitude = np.abs(np.random.normal(scale=.5, size=omega_data.size))

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(Afct, omega_data, amplitude_data, sigma=uncertainty_amplitude, absolute_sigma=True, p0=[Ae_true, Q_true, omega0_true])

# Paramètres ajustés
Ae_fit, omega0_fit, Q_fit = popt

# Incertitudes sur les paramètres
Ae_uncertainty, omega0_uncertainty, Q_uncertainty = np.sqrt(np.diag(pcov))

# Affichage des résultats
print(f"Paramètres ajustés: Ae={Ae_fit}, omega0={omega0_fit}, Q={Q_fit}")
print(f"Incertitudes sur les paramètres: Ae={Ae_uncertainty}, omega0={omega0_uncertainty}, Q={Q_uncertainty}")


omega_data_fit = np.linspace(1, 6, 200)

# Visualisation des données et de l'ajustement
plt.errorbar(omega_data, amplitude_data, yerr=uncertainty_amplitude, fmt='o', label='Données')
plt.plot(omega_data_fit, Afct(omega_data_fit, *popt), 'r-', label='Modèle ajusté')
plt.xlabel('Fréquence')
plt.ylabel('Amplitude')
plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Définition du modèle de titrage (par exemple, une courbe sigmoïde)
def modele_titrage(volume, Veq, pKa, pH_init, pH_fin):
    """
    Modèle de titrage :
    volume : volume de solution titrante ajoutée
    Veq : volume équivalent
    pKa : pKa de l'acide/base titrée
    pH_init : pH initial
    pH_fin : pH final
    """
    return pH_init + (pH_fin - pH_init) / (1 + 10**(pKa - volume + Veq))

# Générer des données factices pour un titrage
np.random.seed(0)
volume_data = np.linspace(20, 40, 100)
Veq_true = 25.0
pKa_true = 4.0
pH_init_true = 2.0
pH_fin_true = 12.0
pH_data = modele_titrage(volume_data, Veq_true, pKa_true, pH_init_true, pH_fin_true) + np.random.normal(scale=0.1, size=volume_data.size)

# Ajouter des incertitudes sur les données de pH
uncertainty_pH = np.abs(np.random.normal(scale=0.05, size=volume_data.size))

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(modele_titrage, volume_data, pH_data, sigma=uncertainty_pH, p0=[Veq_true, pKa_true, pH_init_true, pH_fin_true])

# Paramètres ajustés
Veq_fit, pKa_fit, pH_init_fit, pH_fin_fit = popt

# Incertitudes sur les paramètres
Veq_uncertainty, pKa_uncertainty, pH_init_uncertainty, pH_fin_uncertainty = np.sqrt(np.diag(pcov))

# Affichage des résultats
print(f"Paramètres ajustés: Veq={Veq_fit}, pKa={pKa_fit}, pH_init={pH_init_fit}, pH_fin={pH_fin_fit}")
print(f"Incertitudes sur les paramètres: Veq={Veq_uncertainty}, pKa={pKa_uncertainty}, pH_init={pH_init_uncertainty}, pH_fin={pH_fin_uncertainty}")

# Visualisation des données et de l'ajustement
plt.errorbar(volume_data, pH_data, yerr=uncertainty_pH, fmt='o', label='Données')
plt.plot(volume_data, modele_titrage(volume_data, *popt), 'r-', label='Modèle ajusté')
plt.xlabel('Volume de solution titrante ajoutée')
plt.ylabel('pH')
plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Définition du modèle pour le courant dans la bobine d'induction
def modele_courant(t, I0, tau):
    """
    Modèle de courant dans la bobine d'induction :
    t : temps
    I0 : courant initial
    tau : constante de temps
    """
    return I0 * np.exp(-t / tau)

# Générer des données factices pour le courant dans la bobine d'induction
np.random.seed(0)
t_data = np.linspace(0, 10, 100)
I0_true = 5.0
tau_true = 2.0
courant_data = modele_courant(t_data, I0_true, tau_true) + np.random.normal(scale=0.1, size=t_data.size)

# Ajouter des incertitudes sur les données de courant
uncertainty_courant = np.abs(np.random.normal(scale=0.05, size=t_data.size))

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(modele_courant, t_data, courant_data, sigma=uncertainty_courant, p0=[I0_true, tau_true])

# Paramètres ajustés
I0_fit, tau_fit = popt

# Incertitudes sur les paramètres
I0_uncertainty, tau_uncertainty = np.sqrt(np.diag(pcov))

# Affichage des résultats
print(f"Paramètres ajustés: I0={I0_fit}, tau={tau_fit}")
print(f"Incertitudes sur les paramètres: I0={I0_uncertainty}, tau={tau_uncertainty}")

# Visualisation des données et de l'ajustement
plt.errorbar(t_data, courant_data, yerr=uncertainty_courant, fmt='o', label='Données')
plt.plot(t_data, modele_courant(t_data, *popt), 'r-', label='Modèle ajusté')
plt.xlabel('Temps')
plt.ylabel('Courant')
plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Définition du modèle pour l'allumage de la bobine
def modele_allumage(t, I0, tau):
    """
    Modèle d'allumage de la bobine :
    t : temps
    I0 : intensité lumineuse initiale
    tau : constante de temps
    """
    return I0 * (1 - np.exp(-t / tau))

# Générer des données factices pour l'allumage de la bobine
np.random.seed(0)
t_data = np.linspace(0, 10, 100)
I0_true = 5.0
tau_true = 2.0
intensite_data = modele_allumage(t_data, I0_true, tau_true) + np.random.normal(scale=0.1, size=t_data.size)

# Ajouter des incertitudes sur les données d'intensité lumineuse
uncertainty_intensite = np.abs(np.random.normal(scale=0.05, size=t_data.size))

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(modele_allumage, t_data, intensite_data, sigma=uncertainty_intensite, p0=[I0_true, tau_true])

# Paramètres ajustés
I0_fit, tau_fit = popt

# Incertitudes sur les paramètres
I0_uncertainty, tau_uncertainty = np.sqrt(np.diag(pcov))

# Affichage des résultats
print(f"Paramètres ajustés: I0={I0_fit}, tau={tau_fit}")
print(f"Incertitudes sur les paramètres: I0={I0_uncertainty}, tau={tau_uncertainty}")

# Visualisation des données et de l'ajustement
plt.errorbar(t_data, intensite_data, yerr=uncertainty_intensite, fmt='o', label='Données')
plt.plot(t_data, modele_allumage(t_data, *popt), 'r-', label='Modèle ajusté')
plt.xlabel('Temps')
plt.ylabel('Intensité lumineuse')
plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Définition du modèle d'apprentissage machine
def modele_M(xy, a, b, c, d, e, f):
    """
    Modèle d'apprentissage machine dépendant de deux variables (x, y):
    xy : tuple contenant les variables x et y
    a, b, c, d, e, f : paramètres du modèle
    """
    x, y = xy
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

# Générer des données factices pour x et y
np.random.seed(0)
x_data = np.random.uniform(0, 10, 100)
y_data = np.random.uniform(0, 10, 100)

# Générer des données factices pour le modèle
a_true = 2.0
b_true = -1.0
c_true = 0.5
d_true = 1.0
e_true = -2.0
f_true = 3.0
modele_data = modele_M((x_data, y_data), a_true, b_true, c_true, d_true, e_true, f_true) + np.random.normal(scale=1.0, size=x_data.size)

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(modele_M, (x_data, y_data), modele_data)

# Paramètres ajustés
a_fit, b_fit, c_fit, d_fit, e_fit, f_fit = popt

# Affichage des résultats
print(f"Paramètres ajustés: a={a_fit}, b={b_fit}, c={c_fit}, d={d_fit}, e={e_fit}, f={f_fit}")

# Visualisation des données et de l'ajustement
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_data, y_data, modele_data, label='Données')
x_fit, y_fit = np.meshgrid(np.linspace(0, 10, 50), np.linspace(0, 10, 50))
modele_fit = modele_M((x_fit, y_fit), a_fit, b_fit, c_fit, d_fit, e_fit, f_fit)
ax.plot_surface(x_fit, y_fit, modele_fit, color='r', alpha=0.5, label='Modèle ajusté')
ax.set_xlabel('X Data')
ax.set_ylabel('Y Data')
ax.set_zlabel('Modèle Data')
plt.legend()
plt.show()


# %%
import numpy as np
import ipyvolume as ipv
from scipy.optimize import curve_fit

# Définition du modèle d'apprentissage machine
def modele_M(xy, a, b, c, d, e, f):
    """
    Modèle d'apprentissage machine dépendant de deux variables (x, y):
    xy : tuple contenant les variables x et y
    a, b, c, d, e, f : paramètres du modèle
    """
    x, y = xy
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

# Générer des données factices pour x et y
np.random.seed(0)
x_data = np.random.uniform(0, 10, 100)
y_data = np.random.uniform(0, 10, 100)

# Générer des données factices pour le modèle
a_true = 2.0
b_true = -1.0
c_true = 0.5
d_true = 1.0
e_true = -2.0
f_true = 3.0
modele_data = modele_M((x_data, y_data), a_true, b_true, c_true, d_true, e_true, f_true) + np.random.normal(scale=1.0, size=x_data.size)

# Réaliser l'ajustement de courbe
popt, pcov = curve_fit(modele_M, (x_data, y_data), modele_data)

# Paramètres ajustés
a_fit, b_fit, c_fit, d_fit, e_fit, f_fit = popt

# Affichage des résultats
print(f"Paramètres ajustés: a={a_fit}, b={b_fit}, c={c_fit}, d={d_fit}, e={e_fit}, f={f_fit}")

# Visualisation des données et de l'ajustement avec ipyvolume
x_fit, y_fit = np.meshgrid(np.linspace(0, 10, 50), np.linspace(0, 10, 50))
modele_fit = modele_M((x_fit, y_fit), a_fit, b_fit, c_fit, d_fit, e_fit, f_fit)
ipv.figure()
ipv.plot_surface(x_fit, y_fit, modele_fit, color='red')
ipv.scatter(x_data, y_data, modele_data, color='blue', size=2)
ipv.xlabel('X Data')
ipv.ylabel('Y Data')
ipv.zlabel('Modèle Data')
ipv.show()



# %%
from tabulate import tabulate

# Données des paramètres ajustés et des incertitudes
parametres = [
    ["Ae", 4.7277682605640905, 0.011991769622067454],
    ["omega", 2.0027307499175366, 0.00094044868866963],
    ["gamma", 0.19826682889546587, 0.0014223412651209158],
    ["phi", 0.7845555630172037, 0.001472170894839975]
]

# Affichage du tableau
print(tabulate(parametres, headers=["Paramètres", "Ajusté", "Incertitude"], tablefmt="fancy_grid"))


# %%
