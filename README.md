# Sciences de la Nature - Garneau
![image](https://github.com/Benjamin-GosselinCliche/SciencesDeLaNature_Garneau_Catalogue_Jupyter/assets/21174453/35aebb6d-4c62-41a9-8b3c-a44c2022ae54)


<div style="text-align: center;">
    <div style="display: inline-block; position: relative; width: 350px;">
        <img src="./catalogue-2/img/_68f9688a-19d4-4a3b-97dc-c3ac11ee12f1.jpeg" alt="Dessin" style="width: 100%;"/>
        <p style="text-align: center; margin-top: 5px;">
            <span style="font-style: italic; font-size: 16px;"> Trajectoires</span><br/>
            <span style="font-style: italic; font-size: 12px;">Image générée par DALL·E 3, 2024 </span>
        </p>
    </div>
</div>


## Catalogue Jupyter: 
Démonstrations de python utiles pour les enseignants de Science de la nature.

## Installation de l'environnement virtuel:

```python
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```



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

