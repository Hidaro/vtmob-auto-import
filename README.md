# VTMOB UPHF Auto Import

## Prérequis :
Une version de Python 3 avec pip d'installé est requise afin de faire fonctionner ce programme.

Un environnement virtuel est nécessaire : 
```bash
python3 -m venv venv
source "./venv/bin/activate"
pip install -r requirements.txt
```

## Utilisation : 
### Import simple du fichier .ics
1. Suivre les documentations <br>
a. `documentation/help_credentials` (sans la partie Google Calendar) <br>
b. `documentation/help_custom_color`<br>
c. `documentation/help_custom_title` <br>
2. Exécuter la commande suivante dans le répertoire "code" : ```python3 main.py```
3. Le fichier .ics est disponible au chemin suivant : `result/result.ics`
4. Quitter le programme en entrant "N"

### Import dans Google Calendar
1. Suivre les documentations <br>
a. `documentation/help_credentials` <br>
b. `documentation/help_custom_color`<br>
c. `documentation/help_custom_title` <br>
d. `documentation/fetch_calendarid` <br>
2. Exécuter la commande suivante dans le répertoire "code" : ```python3 main.py```
3. Le fichier .ics est disponible au chemin suivant : `result/result.ics`
4. Continuer le programme en entrant "Y"
5. Si c'est la première fois, valider l'accès de votre application (API) sur le navigateur
6. L'import s'effectue et une confirmation est envoyée à l'utilisateur.