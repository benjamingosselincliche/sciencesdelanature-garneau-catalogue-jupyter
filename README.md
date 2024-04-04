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

