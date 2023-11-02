# ---
# jupyter:
#   jupytext:
#     formats: py:percent,.//ipynb
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
# # Les gaz à effet de serre au Québec
# ---

# %% [markdown]
# <div style="text-align: center;">
#     <img src="./img/_cc50555b-1857-4a03-a71b-744befcfb323.jpeg" alt="Drawing" style="width: 300px;"/>
# </div>

# %% [markdown]
# Les données de l'inventaire québécois des émissions de gaz à effet de serre, sont disponibles chez [Données Québec](https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre "https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre"):
#
# > L’inventaire des émissions de gaz à effet de serre (GES) produits par l’activité humaine au Québec est tenu à jour annuellement depuis 1990 
# par le ministère de l’Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs. Cet inventaire est établi à partir de données recueillies auprès d’entreprises et d’institutions et se base sur des données obtenues principalement de Statistique Canada, d’Environnement et Changement climatique Canada (ECCC) et de ministères et organismes du Québec. 
#
# Dernière modification du jeux de données de ce notebook : 2022-12-21 

# %% [markdown]
# ---
# ## Objectif:
#
# L'objectif de ce notebook est d'utiliser la fonction groupby relative aux dataframes afin d'obtenir le total des GES émis par secteur d'activité.

# %% [markdown]
# ---
# ## Importation des données

# %% [markdown]
# Afin de lire et d'explorer les données, nous utilisons la librairie pandas avec toutes les fonctionnalités des Dataframes.

# %%
import pandas as pd

# %% [markdown]
# Le fichier csv (coma-separated-value) se nomme "inventaire-ges.csv" 
# et les données sont séparées par des points-virgules (;).
# %%
df = pd.read_csv('./fichiers_input/inventaire-ges.csv',sep = ';')
df


# %% [markdown]
# ---
# ## Informations de base sur le jeu de données:
#
# Pour bien comprendre les données dans un DataFrame pandas, vous devez examiner plusieurs aspects clés pour en tirer le meilleur parti. Voici une liste d'informations de base à prendre en compte :
#
# 1. La structure du DataFrame :
#    - Le nombre de lignes (observations) et de colonnes (variables) dans le DataFrame.
#    - Les noms des colonnes, qui représentent les différentes variables.
#
#
# 2. Les types de données :
#    - Vérifiez les types de données de chaque colonne à l'aide de `dtypes` pour vous assurer qu'ils sont corrects.
#
# 3. Les valeurs uniques :
#    - Pour comprendre la variabilité des données catégoriques, utilisez `unique()` pour obtenir les valeurs uniques d'une colonne.
#
# ```python
# df['colonne'].unique()
# ```
#
# 4. Les données manquantes :
#    - Utilisez `isna()` ou `isnull()` pour identifier les données manquantes dans le DataFrame.
#
# ```python
# df.isna().sum()
# ```
#
# 5. Les statistiques descriptives :
#    - Utilisez `describe()` pour obtenir des statistiques de base sur les données numériques, telles que la moyenne, l'écart-type, les quartiles, etc.
#   
#
#
#
#
# %%
# Le nombre de ligne (rows) et de colonne (columns) est: 
df.shape


# %%
# Le nom des colonnes. Sous forme d'une array numpy. 
df.columns
# %%
# Le nom des colonnes. Sous forme d'une liste normale.
df.columns.tolist()

# %%
# Le types de variables dans chaque colonne: 
df.dtypes

# %%
# L'index du dataframe: 
df.index

# %%
# Pour travailler les éléments d'une seule colonne, il faut travailler avec les Séries:
df['Annee'];


# %%
# Élements uniques de la colonne Secteur. Sous forme d'une liste normale.
df['Secteur'].unique().tolist()
# %%
# Élements uniques de la colonne Sous-secteur. Sous forme d'une liste normale.
df['Sous-secteur'].unique().tolist();
# %%
# Élements uniques de la colonne 'Categorie'. Sous forme d'une liste normale.
df['Categorie'].unique().tolist();

# %%
df.isna().sum()

# %% [markdown]
# ---
# ## Sélection du secteur 'Transports'

# %%
df_transports = df[df['Secteur']=='Transports']
df_transports

# %% [markdown]
# ---
# ## Obtention du total par année:

# %%
df[['Annee','Emissions(t_eq_CO2)']]

# %%
df[['Annee','Emissions(t_eq_CO2)']].groupby('Annee')

# %%
df_total1 = df[['Annee','Emissions(t_eq_CO2)']].groupby('Annee').sum()
df_total1;

# %%
df_total1.columns

# %%
df_total1.plot()

# %%
#Pour les transports seulement
df_transports = df[df['Secteur']=='Transports']
df_total2 = df_transports[['Annee','Emissions(t_eq_CO2)']].groupby('Annee').sum()
df_total2;
# %%
result = pd.merge(df_total1, df_total2,on=["Annee"])
result;
# %%
result = pd.merge(df_total1, df_total2, on=["Annee"])
result.plot()
# %%
# %%
# %%
# %%
# %%




# %% [markdown]
# Texte explicatif image
# ![title0](img/presentation.png)

# %% [markdown]
# Le lien est le suivant [example.com](https://example.com/ "https://example.com/").

# %%
# input 1


