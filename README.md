# Grove Chainable LED V1.0

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)]

Bibliothèque et exemple d'utilisation pour [Grove - Chainable RGB LED](https://wiki.seeedstudio.com/Grove-Chainable_RGB_LED/)

## Utilisation

### Matériel nécessaire

- 1 Carte micro:bit
- 1 Shield
- 1 Grove Chainable RGB LED
- Logiciel Mu

### Installation

**Copier** la bibliothèque mb_grove_ChainableLED.py avec l'outil fichier de Mu.

**Flasher** le fichier exemple Chainable_1LED_random.py 

La LED RVB doit être raccordée au port **P16**/P15 du shield, elle change de couleur toute les 2 secondes. Les valeurs RGB de la couleur aléatoire sont visibles avec REPL.

### Fonctions supportées

- Initialisation : DEL = mb_grove_ChainableLED.ChainableLED_grove( _pin clock_ , _pin data_ , _nb leds_ ) 
- Utilisation : DEL.setColorRGB( _numéro led_ , _rouge_ , _vert_ , _bleu_ )

## Ressources

Ecrit en **micropython** à partir de la version C++ _arduino_

[https://github.com/Seeed-Studio/Grove_Chainable_RGB_LED]https://github.com/Seeed-Studio/Grove_Chainable_RGB_LED

## Versions

**Dernière version :** 1.0

Liste des versions : [Cliquer pour afficher](https://github.com/your/project-name/tags)
_(pour le lien mettez simplement l'URL de votre projets suivi de ``/tags``)_

## Auteur

* **F. SAULIN** [FrdSln](https://github.com/FrdSln)

## Licence

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations