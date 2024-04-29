## Travail effectué 

=> Description hebdomadaire du travail effectué (variez les auteurs !)

### Semaine 1  ### Semaine 2

Durant ces deux semaines initiales, nous avons entamé le processus de sélection du thème de notre projet. Tout d'abord, nous avons organisé des sessions de brainstorming en groupe afin de générer des idées sur des problèmes liés aux embouteillages urbains. Après une discussion approfondie et après le thème des perturbations des transports en commun que nous avions présenté la première semaine, plus précisement le 27 février, et qui n'a pas été validé par notre prof, nous avons décidé de nous concentrer sur le phénomène des embouteillages, qui ressemble au thème précédent, mais qui est plus simple à modéliser, ces derniers sont causés par les bouchons en voitures, également connus sous le nom d'embouteillages accordéon. Une fois notre thème choisi, nous avons préparé une présentation détaillée que nous avons ensuite soumise au professeur pour validation. Après examen, le professeur a approuvé notre choix de thème, lançant ainsi officiellement notre projet.
### Semaine 3

Au cours des cinq semaines suivantes, nous avons commencé à donner vie à notre projet en développant un modèle expérimental afin d'étudier les embouteillages accordéon. Notre première étape a été de mener une recherche bibliographique approfondie sur les embouteillages urbains et les modèles de simulation de la circulation existants.
### semaine 4

Cette recherche nous a permis d'identifier les variables clées à prendre en compte dans notre modèle, et on en a déduit que pour comprendre les causes des embouteillages urbains, nous allions devoir créer des bouchons.
Nos recherches se sont basées sur des livres et des vidéos tels que:
"Gridlock: Why We're Stuck in Traffic and What to Do About It" par Randal O'Toole - Ce livre examine les multiples facteurs qui contribuent aux embouteillages, notamment l'aménagement urbain, les politiques de transport, l'économie et les comportements des conducteurs , et le deuxième livre sur lequel nous nous sommes basés pour comprendre efficacement les causes et les aspects de ces embouteillages est le suivant :
"Traffic: Critical Studies of Key Issues" édité par Lisa Dorn - Ce livre rassemble des contributions d'experts dans le domaine de la circulation routière, abordant divers aspects des embouteillages, y compris les causes sous-jacentes telles que la capacité des routes, la congestion aux intersections et les comportements des conducteurs.
Après toutes ces recherches, on a donc dû commencer à rédiger notre code et préciser toutes les fonctions dont on aura besoin tout du long de ce projet, et bien évidement, la premiére fonction à coder était "Créer le monde", afin de générer notre monde dans lequel nous allions créer nos bouchons, cette dernière ne nous a pas pris beaucoup de temps et puis on avait précise les fonctions restantes qu'on aura besoin au cours de la réalisation du projet et qui sont :
1-Créer le monde .
2- Déplacement .
3-Simulation .
4- Générer séquence vitesse .

### semaine 5
- Le développement du code de simulation a été une étape cruciale de notre projet. En utilisant l'environnement de programmation Spider, nous avons écrit le code nécessaire pour créer un modèle réaliste de la circulation routière, en mettant l'accent sur la formation et la propagation des embouteillages accordéon. Nous avons procédé à des tests rigoureux pour valider notre modèle, en ajustant les paramètres selon les besoins  et en comparant nos résultats à des données réelles lorsque cela était possible.
Les paramétres que nous avons pris en compte sont :
   - la taille du monde .
   - les types des conducteurs .
   - le pourcentage de copieurs (qui est un type de comportement des conducteurs).
   - le pourcentage de voitures dans l'anneau .

Durant cet étude nous avons affronter plusieurs difficultés commençant par la fonction fondamentale "créer le monde" car on a du faire plusieurs modifications (prendre en compte un espace égal entre chaque voiture sinon on aura toujours des bouchons dés qu'on commence la simulation et puis on a rajouté un espacement dépendant de la taille du monde ,mélanger la classe des conducteurs en ajoutant les éléments au monde), ensuite on avait redmarqué que les automates posaient quelques difficultés car il fallait vraiment trouver des calculs cohérents afin que les bons couples de valeurs en ressortent, et puis on a commencé ensemble à s'occuper de la fonction "déplacement", qui sert à effectuer les mouvements réalisés par les voitures en fonction de nos paramètres dans le monde, au début cette fonction n'a pas posé de problèmes  mais on s'est rendu compte finalement qu'il y avait des voitures qui se dépassaient entre elles ensuite on a commencé à revoir le code et à la fin que v0(la voiture spéciale celle dont la vitesse varie ) était le probléme vue  qu'elle prenait pas en compte les voitures devant elle , ce qui provoquait des dépassements de sa part, or nous voulions créer une moide sans dépassements pour cela on devait modifier le code en prenant en compte la distance et en conséquence elle modifie sa vitesse en dependant des voitures devant elle autrement dit soit elle serait une copieuse ou une prudente et puis on teste ça en appelant la fonction déplassement la itesse est supérieure à la distance avec la voiture devant elle là la voiture va au maximum qu'elle peut aller et puis les voitures deriéres elle elles vont s'adapter toutes seules .

### semaine 6
Bonjour à tous. Le stress inhérent à toute fin de projets m’oblige aujourd’hui à plus de sobriété dans ce compte rendu. En effet, la présentation approchant à grands pas, il ne nous reste que peu de temps pour tout mettre au point. Deux semaines, pour être précis. En d’autres termes, la rigolade, c’est terminé . Cette semaine on a fait des appels discord afin de compléter le code et valider les métriques finaux (nombres de bouchons formés ,équart type entre les voitures  pour qu'on puisse représebnter nos résultats en graphiques donc  on avait fini


<a href="index.html"> Retour à la page principale </a>
