# Les commandes de bases de Github


## Première étape : initailiser un repo

* Créez dans Github, un nouveau repository
* Nommez comme vous le souhaitez
* Vous pouvez choisir sa visibilité
    * Public : si vous souhaitez que tout le monde puisse avoir y avoir accès
    * Private : Si voius souhaitez être le seul à y acceder 

* La description est optionelle : Remplissez-la si vous le souhaitez
* Allez en bas de page, cliquez sur " Create Repository"

Votre repository est maintenant créé, vous allez pouvoir faire votre premier commit

## Faire son premier commit

Vous allez cous rendre compte su'il y a un petit encadré nommé "Quick setup" qui vous propose deux posibilités:
HTTPS et SSH.

si ce n'est pas fait par défault, choisissez HTTPS.

### Initilisation de Github sur votre machine
sur Visual Studio Code : 

* Ouvrez un terminal
 * menu affichage > Terminal 
 * CTRL + ù 
 * En bas à gauche, vous avez une icone triangulaire et rond. Cliquez dessus

Initialisez Github sur le dossier qui est ouvert : 
avec la commande ``git init``
une fois que git est initialisé, vous allez devoir indiquer quel(s) fichier(s) vous souhaitez envoyer sur github.
Pour cela : 

* ``git add`` pour ajouter TOUS les fichiers 
* ``git add nomDuFichier`` pour ajouter UN fichier en particulier.

Pour info, vous ne devez pas enter vous même le nom complet du dossier ou du fichier,
ça augmente le risque d'erreur. Au lieu d'écrire le nom complet vous-mêmes, vous devez écrire seulement la ou les premières lettre
et appuyer sur la touche ``Tab``

Dans le cas ou il existe plusieurs fichiers ou il y a plusieurs fichiers commençant par les mêmes lettres,
il suffit de continuer d'appuyer sur ``Tab`` jusqu'au bon fichier.

Si vous avez plusieurs fichiers à ajouter mais que vous ne souhaitez pas ajouter tous les fichiers qui se trouvent dans votre dossier de travail,
vous pouvez faire plusieurs fois : ``git add NomDuFichier``

#### En résumé 

* ``git init`` pour initialiser le repo Github
* `` git add NomDuFichier`` - Pour ajouter un fichier

## Exercice 

* Initisalisez le repo Github sur VSCode
* ajoutez le fichier readme


### faire la laison avec le repo distant

vous venez d'initialiser git sur votre machine mais il ne sait pas encore qu'il doitr être lier a votre repository distant
pour cela vous allez devoir connectez l'origine à votre repository distant

commençons par ajouter un petit message qui précise les modifications/ajout/suppresion

* ``git commit -m "explication du commit"``
* ``git commit -m "Ajout du fichier readme"``

Une fois que le message de commit est défini, on va choisir la branche sur laquelle on va travailler.


Lorsque vous souhaitez stockers vos fichiers sur Github, si vous le souhaitez, vous pouvez stocker différentes versions de vos fichiers.
Cela s'appelle des branches.

La branche principale sur laquelle vos fichiers sont enregistrès s'appelle "main".

* ``git branch -m main``

Cette commande indique qu'on sélectionne la branche "main"

Il est maintentant temps de connecter votre repo local (votre machine) à votre repo distant (github). Pour cela utilisez la commande :

`` git remote add origin LIEN_DE_VOTRE_REPO``

Exemple : 

``git remote add origin``
``https://github.com/EvolutionZ19/rockpaperscisors.git``


Maintenant que le repo local et distant sont connectés, iol reste à envoyer les fichiers sur Gihub avec la commande :

``git push -u origin main``

## En résumé 

voici les commandes a lancer : 

* ``git init`` pour initialiser le repo Github
* `` git add NomDuFichier`` pour ajouter un fichier
* ``git commit -m "Nom du commit"`` pour ajouter une description de la modification/ajout
* `` git branch -m main`` pour choisir la branche principal
* ``git remote add origin URL_REPO_GITHUB``pour connecter le repo local
* ``git push -u origin main`` pour envoyer les modifications a Github


## Informations :

Les commandes ``git init``, ``git branch``et ``git remote add origin`` sont à lancer UNE SEULE FOIS  au moment de l'initialisation du repo.

Une fois que ces commandes ont été faites, pendant le reste du développement de votre projet, vous pouvez utiliser les commandes suivantes:

``git add NomDuFicherModifié``, ``git commit -m "message de modifications"`` et ``git push``

C'est ces trois commandes que vous utiliserez à chaque fois : 
* ``git add NomDuFicherModifié``
* ``git commit -m "message de modifications"``
* ``git push``


# Ecrire un bon message de commit 

Ecrire un bonn message de commit est essentiel pour la maintenance et la compréhension d'un projet.
Cela aide à suivre l'évolution du projet et à comprendre les raisons derrière chaque modification.

Voici une norme généralement acceptée pour rédiger des messages de commit

## Structure d'un message de commit 

Un message de commit se compose généralement de deux parties : 

* Un titre (ou en-tête) : C'est une brève description des modifications.
Il doit être concis et ne pas dépasser les 50 caractères. Il doiit commencer par une Majuscule.

* un corps : il donne des détails supplémentaires sur les modifications. Il est séparé du titre par une ligne blanche.

```
Titre court et description

Corps du message : ici, on explique en détail le pourquoi et le comment
des changements si nécéssaires. Essayez de garder chaque ligne à moins
de 72 caractères.

```

## Conseils pour un bon message de commit 


* Utilisez l'impératif : le titre doit idéalement être écrit à la voie impérative
( ex : Ajoute, Refactorise...)
* Titre clair et concis : Doit être court et descriptif
* Séparez les sujets : Si vous avez plusieurs modifications qui n'ont pas de rapports en elles, envisagez de les séparer en plusieurs commit
* Expliquez le pourquoi, le Comment : Le code lui-même montre comment une certaine chose a été faite. Ce qui n'est pas toujours clair ,
c'est pourquoi cette modification a été apportéz.
* Evitez les messages vagues "correction diverse" ou "Mise à jour" faut que se soit utile.
* Utilisez des références aux issues/tracker : Si votre commit fait référence à une issue ou à un ticker, ajoutez cette référence.
* Respectez les conventions de l'équipe, Si votre équipe a des conventions spécifiques pour les messages de commit, suivez-les.


### Exemple d'un bon message de commit 

```
Ajoute une fonctionnalité de recherche

La page d'acceuil avait besoin d'une fonctionnalité de
recherche pour aider les utilisateurs à trouver des contenues
spécifiques.
Cette modifications ajoute un moteur de recherche et utilise
L'API de recherche pour récupérer les résultats.

Relatif à l'issue #123

```

# En savoir plus sur le langage markdown
Pour la rédaction de vos fichiers Readme, n'hésitez pas à vous pencher sur la documentation markdown. Voici un lien pour vous aider :
[Lien pour apprendre le markdown](https://programminghistorian.org/fr/lecons/debuter-avec-markdown)