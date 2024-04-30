#                 Bouchon accordéon


Les embouteillages représentent un défi majeur dans la gestion des infrastructures routières urbaines. Comprendre les mécanismes qui les provoquent est essentiel pour élaborer des solutions efficaces. Dans le cadre de ce projet, nous nous sommes penchés sur la création d'un modèle expérimental visant à étudier les facteurs contribuant aux embouteillages, en mettant particulièrement l'accent sur le rôle des bouchons de voitures.
L'objectif principal de cette étude est de déterminer les causes sous-jacentes des embouteillages en simulant un environnement routier contrôlé. Pour ce faire, nous avons mis en place un anneau routier expérimental doté d'une seule voie, permettant d'observer et d'analyser les perturbations de la circulation.

![test](https://vivreparis.fr/wp-content/uploads/2019/06/bouchon-paris.jpg)



![result](<img width="640" alt="image" src="https://github.com/are-dynamic-2024-g6/bouchon-accordeon/assets/159928048/5d89d3d4-116f-4117-a0b9-aaeaca3c9fc8">)



## Présentation de l'équipe


|  GHRAB Wassim  |  DERRIDJ Asma  |  CHEN Zeyuan  |  POYET-GENEL Jason  |


## Description synthétique du projet

### Problématique :
Comment certaines caractéristiques des véhicules et des conducteurs, ainsi que les interactions des véhicules entre eux influencent-ils la formation et la propagation des bouchons  ?


### Hypothèses principales :
   + Différence de Vitesse du Véhicule  : 
Lorsqu'une ou plusieurs voitures changent de vitesse de manière significative, cela entraîne la formation de bouchons dans la circulation.

   + Comportement des Conducteurs : 
Les conducteurs peuvent réagir différement fasse à une formation de bouchon, en fonction de leur comportement.


### Hypothèse secondaire :
   +  La densité du traffic :
S'il y a plus ou moins de voitures qui circulent sur la route.
    

### Objectifs :

   - Étudier la formation et la propagation des bouchons de circulation sur un anneau à voie unique, en prenant en compte différents paramètres.



 		![test](![Uploading WhatsApp Image 2024-04-30 à 10.07.42_add9cb60.jpg…]()


### Critère(s) d'évaluation :

* Afin de tester notre code et nos fonctions ,on met en place les paramétres et les métriques suivants :
      
### Les paramètres :

   - la taille du monde .
   - le pourcentage des copieurs ( 40% de copieur = 60% de prudent).
   - le pourcentage de voitures dans l'anneau ( .
   - les types des conducteurs .

   
### Les métriques :
      
- Nombre de bouchons formés : Nombre de groupe formés de voitures se suivant et roulant plus lentement qu'une vitesse fixée qui est ici 1.

- Distance moyenne entre les véhicules : La distance moyenne entre chaque véhicule de l'anneau routier.

- Pourcentage d'arrêt : Le pourcentage de véhicules complètement arrêté ( c'est a dire vitesse = 0).

### Modéle :




## Présentation structurée des résultats

Pour la présentation des résultats, nous avons choisi de fixer certaines métriques étant donné la multitude de données. Ainsi, la taille du monde a été fixée à 50. Nous avons ensuite généré des graphiques en fonction des différents taux de voiture : 0.3, 0.5 et 0.8. Chaque graphique présente une métrique spécifique en ordonnée, tandis que le taux de copieurs dans le monde est représenté sur l'axe des abscisses.


### Interprétation des graphique du nombre de bouchon 

![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20nombre%20bouchon%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20nombre%20bouchon%20part%202.png)

Les graphiques ci-dessus révèlent une tendance intéressante : quelle que soit la densité du trafic (exprimée en taux de voitures), lorsque le taux de conducteurs copieurs est inférieur à celui des conducteurs prudents (par exemple, 0.4 copieurs = 0.6 prudents), il se forme généralement un seul bouchon. Cela s'explique par le fait que les conducteurs prudents ne créent pas suffisamment de ralentissements pour engendrer plusieurs bouchons.

Cependant, dès que le taux de conducteurs copieurs dépasse celui des conducteurs prudents (même légèrement avant, comme observé pour un taux de voitures équivalent à 0.8), le nombre de bouchons augmente considérablement. Les conducteurs copieurs commencent progressivement à rattraper les conducteurs prudents, ce qui entraîne la formation de plusieurs bouchons différents, généralement entre 2 et 6, en fonction de la densité du trafic.

Cette tendance est suivie d'une diminution du nombre de bouchons jusqu'à ce qu'il n'en reste qu'un seul lorsque l'anneau est principalement composé de conducteurs copieurs. En effet, en imitant les mouvements du conducteur en face d'eux, les conducteurs copieurs finissent par se stabiliser, et ainsi personne ne rattrape personne, à l'exception de la voiture spéciale. Celle-ci, en rattrapant la voiture devant elle, forme donc le seul bouchon observable dans ce scénario.

### Interprétation des graphique du pourcentage d'arrêt

![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20pourcentage%20arret%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20pourcentage%20arret%20part%202.png)

Dans ces graphiques peu importe la densité du trafic, lorsque le taux de conducteurs copieurs est faible (ce qui signifie qu'il y a plus de conducteurs prudents), le taux d'arrêt des véhicules tend à être très élevé. En effet, les conducteurs prudents ont la tendance à freiner et à arrêter les conducteurs copieurs qui les suivent, comme nous l'avons précédemment conclu lors de notre étude sur la formation de bouchons en fonction du taux de conducteurs copieurs (et donc aussi des conducteurs prudents).

Cependant, dès que le taux de conducteurs copieurs dépasse celui des conducteurs prudents (par exemple, 0.5 de conducteurs copieurs = 0.5 de conducteurs prudents), le taux de véhicules arrêtés diminue de manière constante, voire presque constante. Cette tendance se maintient à mesure que le taux de conducteurs copieurs augmente, ce qui suggère que les conducteurs copieurs adoptent un comportement qui incite les autres véhicules à ne pas s'arrêter.

### Interpretation des graphiques de la distance moyenne

![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20distance%20moyennne%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20distance%20moyenne%20part%202.png)

Dans le premier graphique où la densité de trafic est de 0.3, la distance moyenne entre les véhicules reste élevée tant que le taux de copieurs reste inférieur à 0.8. Cela s'explique par le comportement prudent des conducteurs qui maintiennent une distance de sécurité conséquente entre leurs véhicules, d'autant plus que la densité de trafic est faible. Cependant, une fois que le taux de copieurs atteint 100%, la distance moyenne diminue drastiquement.

Dans le troisième graphique, avec une densité de trafic de 0.5, le schéma est similaire mais la diminution drastique de la distance moyenne se produit à partir d'un taux de copieurs de 0.2. Cette diminution intervient plus tôt en raison de la densité de trafic plus élevée, réduisant ainsi l'espace initial entre les véhicules.

Dans le deuxième graphique, avec une densité de trafic de 0.8, la distance moyenne reste relativement constante (bien que plus faible que dans les autres cas en raison de la densité plus élevée) jusqu'à ce que le taux de copieurs dépasse celui des prudents (0.4). À ce stade, on observe un pic où la distance entre les véhicules se multiplie par trois. Cela indique que les conducteurs prudents créent plusieurs petits bouchons à des endroits distants les uns des autres. Cependant, une fois que le taux de copieurs atteint 0.8, la distance moyenne diminue brusquement, car les conducteurs copieurs ne peuvent pas maintenir une distance de sécurité suffisante entre eux.

Ces graphiques mettent en lumière certaines causes de la formation des bouchons dans notre système. On observe que les bouchons peuvent survenir soit en raison d'une saturation de l'anneau, soit lorsque le nombre de types de voitures est équilibré dans un monde relativement peu saturé. En raison de la diversité entre les voitures, notamment en ce qui concerne les comportements des conducteurs, des bouchons peuvent se former en raison des écarts de vitesse entre les différentes classes de conducteurs. Ainsi, lorsque la classe prudent ralentit ou anticipe plus tôt que les autres, cela peut entraîner la formation de bouchons.

## Conclusion et limite du sytème



## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :
- Livre : Randal O'Toole,""Gridlock: Why We're Stuck in Traffic and What to Do About It". Cato Institute , 2010 ,  9781930865472.
- Site web : http://www.ifsttar.fr
  
-Article académique : Daganzo, Carlos F. "Fundamentals of transportation and traffic operations." Pergamon Transportation Research Part B: Methodological, 1997, 10.1016/b978-008042993-2/50024-7
**Carte mentale de vos mots-clés, en utilisant** <a href="https://framindmap.org/mindmaps/index.html">Framindmap </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**
