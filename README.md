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

Le format `py:percent` permet de spécifier la nature des cellules. La balise `%% [markdown]`
 


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

