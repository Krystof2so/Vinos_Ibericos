# Vinos Ibericos

## 🔶 Énoncé :
El AVE llega esta noche a Madrid y voy a embarcarme en la ruta de los vinos españoles... ¿Pero por dónde empezar? ¿Y si desarrollara mi propia aplicación...?

👉 Cette fois-ci le challenge va nous conduire dans l'univers des interfaces graphiques, à l'aide du module [Tkinter](https://docs.python.org/fr/3/library/tkinter.html). Il s'agira pour ce challenge d'une simple prise en main du module. Mais nous allons tout de même proposer une petite application sympathique qui fera appel à des modules tiers que chacun aura le loisir d'explorer et d'exploiter.

Comme dit en introduction, nous allons donc profiter de ce challenge pour découvrir quelques [régions viticoles espagnoles](https://fr.wikipedia.org/wiki/Viticulture_en_Espagne), en développant une application graphique avec laquelle nous devrons cliquer sur des boutons portant les noms de ces régions viticoles, et dans notre widget central (carte de l'Espagne) apparaîtront des icônes situant exactement l'emplacement de ces régions. Comme vous l'aurez deviné, nous ferons appel aux [coordonnées GPS](https://fr.wikipedia.org/wiki/Global_Positioning_System).

🔹 **Étapes**
1. Création de l'interface graphique (cf. modèle ci-dessous)
2. Utilisation des données (cf. tableau ci-dessous) pour nos boutons
3. Positionnement sur la carte de nos icônes (marqueurs)
4. Utiliser des icônes en rapport avec le thème (cf. les deux fichiers images fournis ci-dessous)

🔹 **Conditions**
* **Utilisation des informations suivantes** (oui, nous sommes sympas, nous vous fournissons les coordonnées GPS):
```py
DO_VINOS = {
    "Alicante": ((38.3436365, -0.4881708), "Tinto"),
    "Calatayud": ((41.3527628, -1.6422977), "Tinto"),
    "Cariñena": ((41.3382122, -1.2263149), "Tinto"),
    "Condado de Huelva": ((37.3382055, -6.5384658), "Blanco"),
    "Jumilla": ((38.4735408, -1.3285417), "Tinto"),
    "La Gomera": ((28.116, -17.248), "Blanco"),
    "Málaga": ((36.7213028, -4.4216366), "Blanco"),
    "Rías Baixas": ((42.459627886165265, -8.722862824636783), "Blanco"),
    "Ribera del Duero": ((41.49232, -3.005), "Tinto"),
    "Rioja": ((42.29993373411561, -2.486288477690506), "Tinto"),
    "Rueda": ((41.4129785, -4.9597533), "Blanco"),
    "Somontano": ((42.0883878, 0.0994041), "Tinto"),
    "Tarragona": ((41.1172364, 1.2546057), "Tinto"),
    "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), "Blanco"),
    "Xérès": ((36.6816936, -6.1377402), "Blanco")
}
```

* **Création de l'interface graphique**:
*frames*, Menus déroulants représentant les noms des régions viticoles (classification: vins blancs et vins rouges), widget avec carte pour y positionner les icônes. Voici une illustration d'un résulat possible :

* *Insertion de l'interface d'exemple*

* **Les icônes**:
Nous utilisons deux fichiers images que nous convertissons en icônes. Un représente une bouteille de vin blanc et l’autre une bouteille de vin rouge. En fait cette distinction apporte un défi supplémentaire puisqu'en fonction de la région (précision avec les données fournies : tinto = rouge, blanco = 🤔 ), l’icône qui s’affiche va représenter l’une ou l’autre des deux images.

* *Insertion des deux fichiers images*

🔹**Et s'il devait y avoir un bonus...**
Libre à chacun d’exploiter les possibilités offertes par les divers modules utilisés… et là c’est sans limite. Proposez-nous vos belles créations...😉