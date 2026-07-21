# exercice 1
quand on passe une liste a une fonction la liste de part est affecté par ce changement quand a la passer par reference ie toutes les modification qu'on effectura se repercuteront sur la liste initial.
exemple de la fonction avec les minimum ...

les *args sont appellé argument positionnel variables il rassemble tous les element en surplus sans nom dans un tuple
les *kwargs sont les arguments nommées variable ils rassembles tous les elements en surplus avec un nom ie (cle=valeur) dans un dictionnaire.
l'ordre doit etre classées du plus restrictif au plus flexible.
1. Paramètres positionnels (ex: a, b)
2. Paramètres avec valeur par défaut (ex: c=10)
3. *args (récupère les surplus positionnels)
4. Paramètres keyword-only (paramètres obligatoires placés après *args)
5. **kwargs (récupère les surplus nommés)

Si cette ordre n'est pas respecté alors python affichera une syntaxError par exemple si on place un *args aples les paramètres positionneles python ne saura pas ou classées ces paramètres

# exercice 2
la ligne if __name__ == "__main__": permet de controler l'execution des fichier ie le bloc situer a l'interieur de cette condition ne va etre executé ssi on execute le fichier main.py
si je fais ça le fichiers utils.py s'executera directement après importation du fichier

# nb
built in function : celle qu'on est pas obliger d'importer exemple (max,min,input,abs,print)

# exercice 3
L'encapsulation est un principe de la poo qui consiste a regrouper les classes et les methodes dans une meme classe et empecher les utilisation a l'exterieur(grace aux underscore exple dans notre code _balance)
L'heritage nous a permis de ne pas reecrire un meme code inutilement 

# exercice 4
EXPLIXATIONS 
Voici la différence entre ces trois modes d'ouverture de fichiers en Python, ainsi que les raisons d'utiliser le gestionnaire de contexte with open(...).

### 1. Différence entre les modes 'r', 'w' et 'a'

* **'r' (Read / Lecture) :**
  * Ouvre le fichier uniquement en lecture.
  * **Comportement :** Le curseur est placé au début du fichier. Le fichier doit exister ; si ce n'est pas le cas, Python déclenche une erreur (`FileNotFoundError`). Il est impossible d'écrire ou de modifier le fichier dans ce mode.

* **'w' (Write / Écriture) :**
  * Ouvre le fichier en écriture.
  * **Comportement :** Si le fichier n'existe pas, Python le crée. S'il existe déjà, son contenu est entièrement effacé (écrasé) dès l'ouverture. Le curseur est au début du fichier.

* **'a' (Append / Ajout) :**
  * Ouvre le fichier en écriture, mais en mode ajout.
  * **Comportement :** Si le fichier n'existe pas, Python le crée. S'il existe, le contenu existant est conservé et le curseur est automatiquement placé à la fin du fichier. Tout ce que vous écrivez s'ajoute à la suite.

---

### 2. Pourquoi utiliser with open(...) plutôt que open() et close() ?

On utilise `with open(...)` (appelé gestionnaire de contexte ou context manager) pour deux raisons principales :

1. **La fermeture automatique du fichier :**
   Avec un `open()` classique, vous devez penser à appeler `file.close()` à la fin du traitement. Si une erreur survient au milieu du script (par exemple, un problème de format de données ou une division par zéro) avant d'atteindre le `close()`, le fichier reste ouvert en mémoire. 
   Avec le bloc `with`, le fichier est automatiquement fermé dès que le code sort du bloc indenté, peu importe ce qui s'est passé (même en cas de plantage ou d'exception).

2. **La libération des ressources système :**
   Laisser des fichiers ouverts inutilement consomme des descripteurs de fichiers au niveau du système d'exploitation. Cela peut provoquer des fuites de mémoire ou empêcher d'autres programmes (ou le système lui-même) de modifier ou supprimer le fichier tant que le script tourne. Le `with` garantit une gestion propre et sécurisée des ressources.

# NB
methode d'instance(__init__), methode de classe (def mamethode(cls)) , les methodes statique (@static method def math(..)) et les methodes magiques