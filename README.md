<img src="https://github.com/Benjamin-GosselinCliche/SciencesDeLaNature_Garneau_Catalogue_Jupyter/assets/21174453/35aebb6d-4c62-41a9-8b3c-a44c2022ae54" alt="Sciences de la Nature - Garneau" width="350">

# Sciences de la Nature - Garneau - Catalogue Jupyter

Démonstrations de python utiles pour les enseignants de Science de la nature.

## Installation de l'environnement virtuel:

```python
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Liste des notebooks:

- cinematique__derivee_et_difference_finie.py
- dynamique_des_populations__equation_differentielle_et_methode_euler.py
- lesBoucles.py
- les_ges_au_quebec__dataframe.py
- mathematique_symbolique__scipy.ipynb
- modeles_et_donnees__sckitlearn.ipynb
- structuresDeDonnes.py
- structuresdecontrole.py

## Structure de fichier:

- **/data**: Ce répertoire contient les données utilisées (.txt, .xlsx, .csv, etc.).

- **/img**: Ce répertoire contient les images.

- **/output**: Ce répertoire contient les fichiers de sortie des codes.

- **/scripts**: Ce répertoire contient les notebooks (.py).

## Configuration des notebooks (.py ou .ipynb?):

Les notebooks sont enregistrés en `.py`. Pour être reconnu en notebook, ceux-ci contiennent une entête de métadonnées pour être reconnu par Jupytext.

```python
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
```

Le format `py:percent` permet de spécifier la nature des cellules. La balise `%% [markdown]` est une cellule de texte et la balise `%% [python]` (ou `%%`) est une cellule de code normal. 

Les notebooks peuvent être aussi enregistrés en `.ipynb`. Il s'agit d'un format de fichier directement reconnu comme un notebook, mais il est moins polyvalent. 

Références:
[https://jupytext.readthedocs.io/en/latest/](https://jupytext.readthedocs.io/en/latest/)


## Notes aux développeurs:

### Paired notebooks

Afin de lier le fichier filename.ipynb à un fichier filename.py (de type percent):

1) dans le même répertoire:
```
jupytext --to py:percent filename.ipynb
```

2) dans sous-répertoire scripts:
```
jupytext --set-formats ipynb,scripts//py:percent --sync filename.ipynb
```

