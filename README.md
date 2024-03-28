# Sciences de la Nature - Garneau
![image](https://github.com/Benjamin-GosselinCliche/SciencesDeLaNature_Garneau_Catalogue_Jupyter/assets/21174453/35aebb6d-4c62-41a9-8b3c-a44c2022ae54)


## Catalogue Jupyter
Ce projet vise � fournir une multitude de d�monstrations python utiles pour les enseignants de science de la nature.

## Installation
Vous aurez besoin d'utiliser le logiciel gratuit 'Jupyter' pour consulter les d�montrations. 
Celles-ci sont aussi disponibles sous forme de fichier python (.py) directement dans le dossier 'scripts'.

## Liste des notebooks:




## Notes aux d�veloppeurs:

### Paired notebooks

Afin de lier le fichier filename.ipynb � un fichier filename.py (de type percent):

1) dans le m�me r�pertoire:
```
jupytext --to py:percent filename.ipynb
```

2) dans sous-r�pertoire scripts:
```
jupytext --set-formats ipynb,scripts//py:percent --sync filename.ipynb
```

