## Couleurs de l'API Google Calendar
Il y a 11 couleurs disponibles pour chaque évènement sur Google Calendar <br>

Celles-ci correspondent à un chiffre (format chaîne de caractère) de 1 à 11. <br>
Un ID différent cause un plantage du programme.

Pour les modifier, il suffit de les ajouter dans le fichier `custom/color_custom.json` : <br>
```json
{
    "courses" : [
        {
            // Ce code est trouvable dans l'emploi du temps
            // en mettant la souris sur la bulle du cours
            "course_code" : "EXAMPLE : T2M6CDAI", 
            // Code de la couleur conformément au tableau ci-dessous
            "color_id" : "FROM 0 TO 11"
        }
    ]
}
```

| Couleur | Code hexadécimal | ID GCalendar | Couleur | Code hexadécimal | ID GCalendar
|:-:|:-:|:-:|:-:|:-:|:-:|
| ![#7986CB](https://via.placeholder.com/15/7986CB/7986CB.png) | #7986CB | 1 | ![#33B679](https://via.placeholder.com/15/33B679/33B679.png) | #33B679 | 2 |
| ![#8E24AA](https://via.placeholder.com/15/8E24AA/8E24AA.png) | #8E24AA | 3 | ![#E67C73](https://via.placeholder.com/15/E67C73/E67C73.png) | #E67C73 | 4 |
| ![#F6BF26](https://via.placeholder.com/15/F6BF26/F6BF26.png) | #F6BF26 | 5 | ![#F4511E](https://via.placeholder.com/15/F4511E/F4511E.png) | #F4511E | 6 |
| ![#039BE5](https://via.placeholder.com/15/039BE5/039BE5.png) | #039BE5 | 7 | ![#616161](https://via.placeholder.com/15/616161/616161.png) | #616161 | 8 |
| ![#3F51B5](https://via.placeholder.com/15/3F51B5/3F51B5.png) | #3F51B5 | 9 | ![#0B8043](https://via.placeholder.com/15/0B8043/0B8043.png) | #0B8043 | 10 |
| ![#D50000](https://via.placeholder.com/15/D50000/D50000.png) | #D50000 | 11 |