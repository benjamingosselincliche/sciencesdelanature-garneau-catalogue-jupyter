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
# # Les gaz à effet de serre au Québec
# ---
#
# <div style="text-align: center;">
#     <div style="display: inline-block; position: relative; width: 350px;">
#         <img src="../img/_cc50555b-1857-4a03-a71b-744befcfb323.jpeg" alt="Dessin" style="width: 100%;"/>
#         <p style="text-align: center; margin-top: 5px;">
#             <span style="font-style: italic; font-size: 16px;"> Solution simple </span><br/>
#             <span style="font-style: italic; font-size: 12px;">Image générée par DALL·E 3, 2024 </span>
#         </p>
#     </div>
# </div>
#
#

# %% [markdown]
# Les données de l'inventaire québécois des émissions de gaz à effet de serre, sont disponibles chez [Données Québec](https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre "https://www.donneesquebec.ca/recherche/dataset/inventaire-quebecois-des-emissions-de-gaz-a-effet-de-serre"):
#
# > "L’inventaire des émissions de gaz à effet de serre (GES) produits par l’activité humaine au Québec est tenu à jour annuellement depuis 1990 
# par le ministère de l’Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs. Cet inventaire est établi à partir de données recueillies auprès d’entreprises et d’institutions et se base sur des données obtenues principalement de Statistique Canada, d’Environnement et Changement climatique Canada (ECCC) et de ministères et organismes du Québec." 
#
# Dernière modification du jeux de données pour ce notebook : 2022-12-21 

# %% [markdown]
# ---
# # Objectifs:
#
# L'objectif de ce notebook est d'utiliser la méthode `groupby`
#  relative aux dataframes afin d'obtenir le total des GES émis par secteur d'activité.

# %% [markdown]
# ---
# # Importation des données

# %% [markdown]
# Afin de lire et d'explorer les données, nous utilisons la librairie pandas avec toutes les fonctionnalités des Dataframes. 

# %%
# Initialisation de la librairie Pandas.
import pandas as pd

# Importation des données. Le fichier csv (coma-separated-value) se nomme "inventaire-ges.csv" 
# et les données sont séparées par des points-virgules (;).
df = pd.read_csv('./fichiers_input/inventaire-ges.csv',sep = ';')
df

# %%
# Le nombre de ligne (rows) et de colonne (columns) est: 
df.shape


# %%
# Le nom des colonnes, sous forme d'une array numpy. 

df.columns
# %%
# Le nom des colonnes, sous forme d'une liste normale.

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
secteurs = df['Secteur'].unique().tolist()
secteurs
# %%
# Élements uniques de la colonne Sous-secteur. Sous forme d'une liste normale.
df['Sous-secteur'].unique().tolist();
# %%
# Élements uniques de la colonne 'Categorie'. Sous forme d'une liste normale.
df['Categorie'].unique().tolist();

# %%
# Élements absents
df.isna().sum()

# %%
df.isnull().sum()

# %% [markdown]
# ---
# # Constructions de la nouvelle dataframe: 
#
# Les étapes pour construire df_secteurs_total sont:

# %% [markdown]
# ---
# ## Construction 1: obtention du total par année:

# %%
df[['Annee','Emissions(t_eq_CO2)']]

# %%
df[['Annee','Emissions(t_eq_CO2)']].groupby('Annee')

# %%
df_total = df[['Annee','Emissions(t_eq_CO2)']].groupby('Annee').sum()
df_total;

# %%
df_total.columns

# %%
df_total = df_total.rename(columns={"Emissions(t_eq_CO2)": "Emissions(t_eq_CO2)-Total"})

# %%
df_total.describe()

# %%
df_total.plot()

# %% [markdown]
# ---
# ## Construction 2: obtention du total par année pour le secteur 'Transports':

# %%
#Pour les transports seulement
df_transports = df[df['Secteur']=='Transports']
df_transports_total = df_transports[['Annee','Emissions(t_eq_CO2)']].groupby('Annee').sum()
df_transports_total = df_transports_total.rename(columns={"Emissions(t_eq_CO2)": "Emissions(t_eq_CO2)-Transports"})
df_transports_total;
# %%
df_merge = pd.merge(df_total, df_transports_total, on=["Annee"])
# df_merge
# %%
df_merge = df_total.merge(df_transports_total,on=["Annee"])
# df_merge

# %% [markdown]
# ---
# ## Construction 3: obtention du total par année pour tous les secteurs:

# %%
secteurs

# %%
# Initialisation du DataFrame résultant avec le premier DataFrame
df_secteurs_total = df_total

for secteur in secteurs:
    df_secteur = df[df['Secteur']==secteur]
    df_secteur_total = df_secteur[['Annee','Emissions(t_eq_CO2)']].groupby('Annee').sum()
    df_secteur_total = df_secteur_total.rename(columns={"Emissions(t_eq_CO2)": f'Emissions(t_eq_CO2)-{secteur}'})
    df_secteurs_total = df_secteurs_total.merge(df_secteur_total, on=["Annee"])

df_secteurs_total  

# %%
df_secteurs_total.plot()

# %% [markdown]
# ---
# # Exportation de la nouvelle dataframe:
# %%
df_secteurs_total.to_excel("./fichiers_output/df_secteurs_total.xlsx",sheet_name='Emissions(t_eq_CO2) par secteur') 
# %%
df_secteurs_total.to_csv("./fichiers_output/df_secteurs_total.csv") 


# %% [markdown]
#

# %% [markdown]
#

# %%


