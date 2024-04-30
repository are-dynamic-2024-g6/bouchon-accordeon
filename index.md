@import "{{pages-themes/merlot@v0.2.0}}";

# Bouchon accordéon


Les embouteillages représentent un défi majeur dans la gestion des infrastructures routières urbaines. Comprendre les mécanismes qui les provoquent est essentiel pour élaborer des solutions efficaces. Dans le cadre de ce projet, nous nous sommes penchés sur la création d'un modèle expérimental visant à étudier les facteurs contribuant aux embouteillages, en mettant particulièrement l'accent sur le rôle des bouchons de voitures.
L'objectif principal de cette étude est de déterminer les causes sous-jacentes des embouteillages en simulant un environnement routier contrôlé. Pour ce faire, nous avons mis en place un anneau routier expérimental doté d'une seule voie, permettant d'observer et d'analyser les perturbations de la circulation.

![test](https://vivreparis.fr/wp-content/uploads/2019/06/bouchon-paris.jpg)


## English version
					Accordion stopper :
     
- Traffic jams represent a major challenge in the management of urban road infrastructure. Understanding the mechanisms that cause them is essential to developing effective solutions. As part of this project, we focused on creating an experimental model to study the factors contributing to traffic jams, with a particular emphasis on the role of car traffic jams.
The main objective of this study is to determine the underlying causes of traffic jams by simulating a controlled road environment. To do this, we set up an experimental road ring with a single lane, allowing traffic disruptions to be observed and analyzed.

![result](<img width="640" alt="image" src="https://github.com/are-dynamic-2024-g6/bouchon-accordeon/assets/159928048/5d89d3d4-116f-4117-a0b9-aaeaca3c9fc8">)



## Présentation de l'équipe


|  GHRAB Wassim  |  DERRIDJ Asma  |  CHEN Zeyuan  |  POYET-GENEL Jason  |


## Description synthétique du projet

**Problématique :
Comment certaines caractéristiques des véhicules et des conducteurs, ainsi que les interactions des véhicules entre eux influencent-ils la formation et la propagation des bouchons  ?


**Hypothèses principales :
   + Différence de Vitesse du Véhicule  : 
Lorsqu'une ou plusieurs voitures changent de vitesse de manière significative, cela entraîne la formation de bouchons dans la circulation.

   + Comportement des Conducteurs : 
Les conducteurs peuvent réagir différement fasse à une formation de bouchon, en fonction de leur comportement.



**Hypothèse secondaire :
   +  La densité du traffic :
S'il y a plus ou moins de voitures qui circulent sur la route.
    

**Objectifs :

   - Étudier la formation et la propagation des bouchons de circulation sur un anneau à voie unique, en prenant en compte différents paramètres.



 		![test](![Uploading WhatsApp Image 2024-04-30 à 10.07.42_add9cb60.jpg…]()




**Critère(s) d'évaluation :

* Afin de tester notre code et nos fonctions ,on met en place les paramétres et les métriques suivants :
      
**Les paramètres :

   - la taille du monde .
   - le pourcentage des copieurs .
   - le pourcentage de voitures dans l'anneau .
   - les types des conducteurs .

   
**Les métriques :
      
- Nombre de bouchons formés : Nombre de groupe formés de voitures se suivant et roulant plus lentement qu'une vitesse fixée.

- Distance moyenne entre les véhicules : La distance moyenne entre chaque véhicule de l'anneau routier.

- Pourcentage d'arrêt : Le pourcentage de véhicules complètement arrêté (vitesse 0).



    

## Présentation structurée des résultats
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20nombre%20bouchon%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20nombre%20bouchon%20part%202.png)

On déduit des graphiques ci-dessus que peu importe la densité du traffic (taux de voitures), lorsque que le taux de copieurs est inférieur au taux de prudents (O.4 copieur = 0.6 prudent), il ne s'y formera qu'un seul bouchon car les prudents ne se rattrapent pas assez pour en former plus. Mais dès que le taux de copieurs dépassera celui de prudents (même un peu avant pour le taux de voitures équivalent à 0.8), bien plus de bouchons se formeront car les copieurs eux, rattrapent petit à petit les prudents, de l'ordre de 2 à 6 bouchons différents en fonction de la densité du traffic. Tout ça avant de redescendre jusqu'à un seul et unique bouchon lorsque l'anneau n'est composé que de copieurs car à force de copier les mouvements de celui en face, personne ne rattrapera personne, si ce n'est la voiture spéciale, qui forme donc, en rattrapant la voiture devant elle, le seul bouchon observé.


![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20pourcentage%20arret%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20pourcentage%20arret%20part%202.png)

Encore une fois, il n'y a presque pas de différences en fonction de la densité du traffic, peu importe cette dernière lorsque le taux de copieurs est faible (et qu'il y a donc plus de prudents), le taux d'arrêt a tendance à être très élevé, car en effet les prudents ont tendance àn stopper les copieurs derrière eux, on l'a d'ailleurs conclu plus tôt lors de l'étude de la formation de bouchons en fonction du taux de copieurs (et donc aussi de prudents). Par contre le taux de voitures arrêtées est en baisse constante (ou presque) à partir du moment où le taux de copieur dépassent celui de prudent (on rappelle que 0.5 copieur = 0.5 prudent) et au fur et à mesure que l'on augmente le taux de copieurs, ce qui montre que les copieurs ont une manière de réagir qui encourage les voitures à ne pas s'arrêter. 

![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20distance%20moyennne%20part%201.png)
![alt text](https://github.com/are-dynamic-2024-g6/bouchon-accordeon/blob/master/images/Graphique%20final%20distance%20moyenne%20part%202.png)

Dans ce dernier cas présent ci-dessus, pour une densité de traffic de 0.3 (graph.1), la distance moyenne entre les véhicules est élevée avant que le taux de copieurs ne dépassent 0.8, en effet les prudent laissent beaucoup de distance entre eux et la voiture de devant, et avec une densité de traffic faible, la distance de base entre les voitures est d'office élevée, il n'y a donc que lorsque nous avons 100% de copieurs que la distance moyenne diminue drastiquement. Pour une densité de traffic de 0.5 (garph.2), nous sommes en présence du même cas que pour la densité de 0.3, mais la diminution drastique apparaîtra à partir d'un taux de copieurs à 0.2, car il y a en effet moins d'espace de base entre les voiture en vu de l'augmentation de la densité du traffic. Enfin, pour une densité de 0.8, on observe une courbe bien différente, la distance moyenne reste constante (plus faible que les autres cas en vu de l'augmentation de la densité comme vu précédemment) jusqu'à ce que le taux de copieurs (0.6) dépasse le taux de prudents (0.4), où l'on peut observer un pick avec une distance qui se mulltiplie par 3, on peut en déduire que prudents créent plusieurs petits bouchons à des endroits distants les uns des autres, tout ça avant de redescendre brusquement à partir d'un taux de copieurs de 0.8, car en effet, les copieurs ne peuevent pas augmenter la distance entre eux.



## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :
- Livre : Randal O'Toole,""Gridlock: Why We're Stuck in Traffic and What to Do About It". Cato Institute , 2010 ,  9781930865472.
- Site web : http://www.ifsttar.fr
  
-Article académique : Daganzo, Carlos F. "Fundamentals of transportation and traffic operations." Pergamon Transportation Research Part B: Methodological, 1997, 10.1016/b978-008042993-2/50024-7
**Carte mentale de vos mots-clés, en utilisant** <a href="https://framindmap.org/mindmaps/index.html">Framindmap </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**
