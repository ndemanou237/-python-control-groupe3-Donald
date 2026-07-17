# exercice 1
quand on passe une liste a une fonction la liste de part est affecté par ce changement quand a la passer par reference ie toutes les modification qu'on effectura se repercuteront sur la liste initial.
exemple de la fonction avec les minimum ...

les *args sont appellé argument positionnel variables il rassemble tous les element en surplus sans nom dans un tuple
les *kwargs sont les arguments nommées variable ils rassembles tous les elements en surplus avec un nom ie (cle=valeur) dans un dictionnaire.
l'ordre doit etre classées du plus restrictif au plus flexible.
1.Paramètres positionnels (ex: a, b)

2.Paramètres avec valeur par défaut (ex: c=10)

3.*args (récupère les surplus positionnels)

4.Paramètres keyword-only (paramètres obligatoires placés après *args)

5.**kwargs (récupère les surplus nommés)
Si cette ordre n'est pas respecté alors python affichera une syntaxError par exemple si on place un *args aples les paramètres positionneles python ne saura pas ou classées ces paramètres