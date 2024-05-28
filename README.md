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

- boucles.ipynb
- cinematique_derivee_et_difference_finie.ipynb
- dynamique_des_populations_equation_differentielle_et_methode_euler.ipynb
- ges_au_quebec_dataframe.ipynb
- mathematique_symbolique_sympy.ipynb
- modeles_et_donnees_sckitlearn.ipynb
- orbite_widget.ipynb
- roche_papier_ciseaux_apprentissage_machine.ipynb
- structures_de_controle.ipynb
- structures_de_donnees.ipynb

## Structure de fichier:

- **/data**: Ce répertoire contient les données utilisées (.txt, .xlsx, .csv, etc.).

- **/img**: Ce répertoire contient les images.

- **/output**: Ce répertoire contient les fichiers de sortie des codes.

- **/notebook**: Ce répertoire contient les notebooks (.py).

## Configuration des notebooks (.py ou .ipynb?):

Les notebooks sont enregistrés en `.ipynb`. Un fichier `.ipynb` (IPython Notebook) est un format utilisé par Jupyter Notebook pour stocker du code, du texte, des visualisations et d'autres éléments interactifs dans un seul document.  


Les notebooks peuvent être aussi enregistrés en `.py`. Le format `py:percent` permet de spécifier la nature des cellules. La balise `%% [markdown]` est une cellule de texte et la balise `%% [python]` (ou `%%`) est une cellule de code normal. 

Références:
[https://jupytext.readthedocs.io/en/latest/](https://jupytext.readthedocs.io/en/latest/)

## Modifier un notebook

Pour modifier un notebook, suivez les étapes ci-dessous :

### Étapes pour modifier un catalogue

1. **Ouvrir le catalogue**
   - Démarrez JupyterLab en exécutant la commande suivante dans votre terminal :
     ```bash
     jupyter lab
     ```
   - Naviguez vers le répertoire contenant votre catalogue Jupyter et ouvrez le fichier du catalogue (`*.ipynb`).

2. **Modifier les cellules**
   - Les cellules de type Markdown contiennent du texte, tandis que les cellules de type Code contiennent du code Python.
   - Cliquez sur une cellule pour la sélectionner, puis commencez à modifier son contenu.

3. **Exécuter le code**
   - Vous pouvez exécuter une cellule de code en appuyant sur `Shift + Enter`.

4. **Ajouter de nouvelles cellules**
   - Utilisez les boutons de la barre d'outils ou les raccourcis clavier (`a` pour ajouter une cellule au-dessus, `b` pour en ajouter une en dessous).
   - Définissez le type de la nouvelle cellule (Code ou Markdown) en utilisant les options du menu déroulant dans la barre d'outils.

5. **Enregistrer vos modifications**
   - Une fois les modifications terminées, assurez-vous de sauvegarder votre travail en cliquant sur l'icône de disquette dans la barre d'outils ou en utilisant le raccourci `Ctrl + S`.



