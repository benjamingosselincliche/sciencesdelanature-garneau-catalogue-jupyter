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
# # Démonstration Sympy
# ---
#
# <div style="text-align: center;">
#     <div style="display: inline-block; position: relative; width: 350px;">
#         <img src="../img/_f260286f-3f4a-48cb-9dee-93d38a5b43d2.jpeg" alt="Dessin" style="width: 100%;"/>
#         <p style="text-align: center; margin-top: 5px;">
#             <span style="font-style: italic; font-size: 16px;"> Sympy </span><br/>
#             <span style="font-style: italic; font-size: 12px;">Image générée par DALL·E 3, 2024 </span>
#         </p>
#     </div>
# </div>

# %% [markdown]
#
# ## Mise en contexte:
#
# SymPy est une bibliothèque Python pour les mathématiques symboliques. Contrairement aux calculs numériques, où les valeurs sont représentées par des nombres, les mathématiques symboliques manipulent des expressions mathématiques de manière exacte, en conservant les symboles tels quels.
#
# Comme à l'habitude, nous importons d'abors la librairie:
#
# ```python
# import sympy as sp 
# ```
#
# Les variables doivent être instanciées de la manière suivante:
#
# ```python
# x, y, a, b = sp.symbols('x y a b')
# ```
#
# Ici, les variables x, y, a et b seront donc traités symboliquement.
#
#
#

# %%
import sympy as sp

# Définition des variables
x, y, a, b = sp.symbols('x y a b')

# Définition d'une fonction à une variable: f1(x) 
fonction_f1 = sp.Function('f1')(x)

# Définition d'une fonction à deux variable: f2(x, y) 
fonction_f2 = sp.Function('f2')(x, y)

# L'équivalent d'un print pour un affichage symbolique dans Jupyter est la fonction display de IPython.display
from IPython.display import display
display(x)
display(fonction_f1)

#Le dernier élément d'une cellule n'a pas besoin d'un display
fonction_f2

# %%
#
polynomial_degre_4 = 16*x**4 + 96*x**3 + 216*x**2 + 216*x + 81
polynomial_degre_4
racines = sp.roots(polynomial_degre_4)
racines

# %%
polynomial_degre_4.factor()

# %%
#
polynomial_degre_4 = 10*x**4 + 96*x**3 + 216*x**2 + 216*x + 81
# Calcul des racines du polynôme
racines = sp.roots(polynomial_degre_4)
racines

# %%
## Les fonctions


ggg = r'f(a)=\int_\infty^0 \frac{1}{a+2} \mathrm{d}a'

display(Math(ggg))

# %%
# Création de l'expression f(x + a)
fonction_f_with_offset = fonction_f.subs(x, x + b)

# Affichage de f(x + a)
fonction_f_with_offset

# %%
# Calcul de la dérivée
derivative_f1 = sp.diff(fonction_f1, x)

# Calcul de l'intégrale
integral_f1 = sp.integrate(fonction_f1, x)

display(derivative_f1)
display(integral_f1)

# %%
import sympy as sp

# Définition des symboles
x, a, b = sp.symbols('x a b')

# Définition de la fonction F(x)
F = sp.Function('F')(x)

# Définition de l'intégrale définie
integral_eq = sp.Eq(sp.integrate(F.diff(x), (x, a, b)), F.subs(x, b) - F.subs(x, a))

# Affichage de l'équation
integral_eq


# %%
import sympy as sp

# Définition des symboles
x, y = sp.symbols('x y')

# Expression à simplifier
expr = (x**2 + 2*x + 1) / (x + 1)

# Simplification de l'expression
simplified_expr = sp.simplify(expr)

print("Expression simplifiée:", simplified_expr)


# %%
# Equation symbolique
equation = sp.Eq(x**2 + 2*x, 0)

# Résolution de l'équation
solutions = sp.solve(equation, x)

print("Solutions de l'équation:", solutions)


# %%
# Définition d'une fonction symbolique
f = sp.Function('f')(x)

# Calcul de la dérivée
derivative = sp.diff(f, x)

print("Dérivée de f par rapport à x:", derivative)

# Calcul de l'intégrale
integral = sp.integrate(f, x)

print("Intégrale de f par rapport à x:", integral)


# %%
# Simplification d'une expression trigonométrique
expr_trig = sp.sin(x)**2 + sp.cos(x)**2

simplified_trig_expr = sp.simplify(expr_trig)

print("Expression trigonométrique simplifiée:", simplified_trig_expr)


# %%
import scipy.integrate as spi

# Définir la fonction à intégrer
def f(x):
    return x**2

# Intégrer la fonction de 0 à 1
result, error = spi.quad(f, 0, 1)
print("Résultat de l'intégration :", result)

# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Définir l'équation différentielle : dy/dt = -2y
def model(t, y):
    return -2 * y

# Conditions initiales et intervalle de temps
t_span = (0, 5)
y0 = [1]

# Résolution de l'EDO
sol = solve_ivp(model, t_span, y0, t_eval=np.linspace(0, 5, 100))

# Affichage du résultat
plt.plot(sol.t, sol.y[0])
plt.xlabel('Temps')
plt.ylabel('y(t)')
plt.title('Solution de l\'équation différentielle')
plt.grid(True)
plt.show()


# %%
print(sol)

# %%
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

# Données initiales
x = np.linspace(0, 10, 10)
y = np.cos(x)

# Interpolation linéaire
f_linear = interp1d(x, y)
x_new = np.linspace(0, 10, 100)
y_new_linear = f_linear(x_new)

# Interpolation cubique
f_cubic = interp1d(x, y, kind='cubic')
y_new_cubic = f_cubic(x_new)

# Affichage des résultats
plt.plot(x, y, 'o', label='Données initiales')
plt.plot(x_new, y_new_linear, '-', label='Interpolation linéaire')
plt.plot(x_new, y_new_cubic, '--', label='Interpolation cubique')
plt.legend()
plt.title('Interpolation de données')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# %%
import sympy as sp

# Définition des symboles
x, y = sp.symbols('x y')

# Expression à simplifier
expr = (x**2 + 2*x + 1) / (x + 1)

# Simplification de l'expression
simplified_expr = sp.simplify(expr)

# Affichage en LaTeX
sp.latex(simplified_expr)


# %%
# Définition d'une fonction symbolique
f = sp.Function('f')(x)

# Calcul de la dérivée
derivative = sp.diff(f, x)

# Affichage en LaTeX
mip = sp.latex(derivative)

from IPython.display import display, Math
display(Math(mip))


# %%
