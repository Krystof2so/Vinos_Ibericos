# Todo : Docstrings + explication des paramètres de Tkinter

import tkinter as tk  # Pour créer l'interface graphique
from dataclasses import dataclass  # 'dataclasses' et 'enum' pour les données
from enum import StrEnum

from PIL import Image, ImageTk  # Pour transformer les images en icônes
from tkintermapview import TkinterMapView  # Pour la carte, avec gestion des coordonnées GPS

# Constantes (Données possiblement insérables dans un fichier externe)
GPS_MADRID = 40.416705, -3.703582
TINTO, BLANCO = True, False
AOC_WINE = {  # {Nom région viticole : (coordonnées GPS), type de vin sous forme d'un booléen}
    "Alicante": ((38.3436365, -0.4881708), TINTO),
    "Calatayud": ((41.3527628, -1.6422977), TINTO),
    "Cariñena": ((41.3382122, -1.2263149), TINTO),
    "Condado de Huelva": ((37.3382055, -6.5384658), BLANCO),
    "Jumilla": ((38.4735408, -1.3285417), TINTO),
    "La Gomera": ((28.116, -17.248), BLANCO),
    "Málaga": ((36.7213028, -4.4216366), BLANCO),
    "Rías Baixas": ((42.459627886165265, -8.722862824636783), BLANCO),
    "Ribera del Duero": ((41.49232, -3.005), TINTO),
    "Rioja": ((42.29993373411561, -2.486288477690506), TINTO),
    "Rueda": ((41.4129785, -4.9597533), BLANCO),
    "Somontano": ((42.0883878, 0.0994041), TINTO),
    "Tarragona": ((41.1172364, 1.2546057), BLANCO),
    "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), BLANCO),
    "Xérès": ((36.6816936, -6.1377402), BLANCO)
}


@dataclass
class UISettings:
    """Ensemble des données numériques pour les paramètres de l'interface."""
    APP_HEIGHT = 770  # Hauteur fenêtre
    APP_WIDTH = 900  # Largeur fenêtre
    BD_WID = 3  # Épaisseur bordure widgets
    ICON_RESIZE = 40
    MAP_HEIGHT = 600
    MAP_WIDTH = 800
    PAD_X_MENU = 120  # Espacement horizontal des menus déroulants
    PAD_Y_MENU = 10   # Vertical
    PADXY_MAP_FRAME = 10
    PADXY_MENU_FRAME = 20
    ZOOM_MAP = 6  # Niveau de zoom sur la carte par défaut
    ZOOM_MAP_WITH_ICON = 7  # Niveau de zoom sur la carte lors du placement de l'icône


class DatasText(StrEnum):
    """Ensemble des données textuelles : Affichage et paramètres interfaces."""
    BLA = "Blanco"  # Label
    COLOR_BG = "#D2B48C"
    COLOR_WID = "#808000"
    COLOR_TEXT = "#FFD700"
    GEOMETRY = f"{UISettings.APP_WIDTH}x{UISettings.APP_HEIGHT}"  # Taille application
    PNG_B = "blanco.png"  # Les deux noms des fichiers images
    PNG_T = "tinto.png"
    TIN = "Tinto"  # Label
    TITLE_APP = "Vinos Ibericos"


class WineDatas:
    """Gestion des informations sur les vins et leur emplacement."""
    def __init__(self):
        self.aoc_wine: dict[str, tuple[tuple[float, float], bool]] = AOC_WINE

    def get_wine_info(self, region: str) -> tuple:
        """
        Récupération des informations de la région donnée en paramètres.

        :param region: (str) Le nom de la région viticole sélectionnée.
        :return: Un tuple contenant les coordonnées GPS de la région sous forme de tuple de deux float et le
                 type de vin produit dans la région sous forme de booléen (True pour le vin rouge, False pour le vin
                 blanc).
        """
        return self.aoc_wine.get(region)


class WineController:
    """Gestion de l'interaction entre 'WineDatas' et 'WineUI'."""
    def __init__(self, model, view):
        self.model = model  # Instance de 'WineDatas'
        self.view = view  # Instance de 'WineUI'

    def locate_region(self, region: str) -> None:
        """
        Méthode appelée lorsqu'une région est sélectionnée dans l'un des menus déroulants.

        :param region: (str) Le nom de la région viticole sélectionnée.
        :return: None

        Cette méthode définit la position de la carte sur les coordonnées GPS de la région sélectionnée, affiche un
        marqueur à cette position avec l'icône appropriée, définit le niveau de zoom de la carte et définit la variable
        StringVar associée au menu déroulant de la vue en fonction du type de vin de la région sélectionnée.
        """
        x, y = self.model.get_wine_info(region)[0]  # Récupère les données GPS
        icon = self.view.wine_icon(region)  # Récupère l'icône
        self.view.set_position(x, y, marker=True, icon=icon)  # Définit l'emplacement du marqueur (icône)
        self.view.set_zoom(UISettings.ZOOM_MAP_WITH_ICON)  # Le niveau de zoom
        self.view.tinto_var.set(region) if self.model.get_wine_info(region)[1] == TINTO \
            else self.view.blanco_var.set(region)  # Mise à jour de la variable 'StringVar' en fonction du type de vin


class WineUI:
    """Gestion de l'interface graphique, à l'aide de 'Tkinter'."""
    def __init__(self, window, controller):
        self.controller = controller  # Instance de 'WineController'
        # Création de nos icônes :
        # Création d'une instance de la classe PhotoImage du module ImageTk de PIL, en passant l'image redimensionnée à
        # son constructeur (Cf. https://pillow.readthedocs.io/en/stable/reference/ImageTk.html#PIL.ImageTk.PhotoImage)
        self.tinto_icon = ImageTk.PhotoImage(
            Image.open(DatasText.PNG_T).resize((UISettings.ICON_RESIZE, UISettings.ICON_RESIZE)))
        self.blanco_icon = ImageTk.PhotoImage(
            Image.open(DatasText.PNG_B).resize((UISettings.ICON_RESIZE, UISettings.ICON_RESIZE)))

        # FENETRE DE L'APPLICATION :
        self.window = window
        self.window.title(DatasText.TITLE_APP)
        self.window.geometry(DatasText.GEOMETRY)  # Taille de la fenêtre principale
        self.window.configure(bg=DatasText.COLOR_BG)  # Couleur de fond de l'application
        # Créer le cadre principal :
        self.main_frame = tk.Frame(self.window, bg=DatasText.COLOR_BG)
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Positionnement sur tout l'espace disponible

        # AJOUT DE LA CARTE DE L'ESPAGNE :
        self.map_frame = tk.Frame(self.main_frame, width=UISettings.MAP_WIDTH, height=UISettings.MAP_HEIGHT)
        self.map_frame.pack(side=tk.TOP, padx=UISettings.PADXY_MAP_FRAME, pady=UISettings.PADXY_MAP_FRAME)
        # À l'aide du module 'TkinterMapView' :
        self.map_widget = TkinterMapView(self.map_frame, width=UISettings.MAP_WIDTH, height=UISettings.MAP_HEIGHT,
                                         bd=UISettings.BD_WID, bg=DatasText.COLOR_WID)
        self.map_widget.set_position(GPS_MADRID[0], GPS_MADRID[1])  # Centrée sur Madrid par défaut
        self.map_widget.set_zoom(UISettings.ZOOM_MAP)
        self.map_widget.pack()

        # AJOUT DES MENUS DÉROULANTS :
        # Cadre des menus déroulants :
        self.menu_grid = tk.Frame(self.main_frame, highlightbackground=DatasText.COLOR_WID,
                                  highlightthickness=UISettings.BD_WID)
        self.menu_grid.pack(pady=10)
        # Menu déroulant pour les vins rouges (Label + menu déroulant) :
        self.tinto_label = tk.Label(self.menu_grid, text=DatasText.TIN, fg=DatasText.COLOR_TEXT)
        list_tinto = [region for region, (pos, wine_type) in self.controller.model.aoc_wine.items()
                      if wine_type == TINTO]  # Liste des éléments pour le menu déroulant
        # Variable (StringVar) pour stocker la valeur sélectionnée dans le menu déroulant :
        self.tinto_var = tk.StringVar(self.menu_grid, list_tinto[0])
        # Définition du menu et appel de la méthode 'locate_region' du controller :
        self.tinto_list_menu = tk.OptionMenu(self.menu_grid, self.tinto_var, *list_tinto,
                                             command=self.controller.locate_region)
        # Menu déroulant pour les vins blancs (Label + menu déroulant insérés dans un même frame) :
        self.blanco_label = tk.Label(self.menu_grid, text=DatasText.BLA, fg=DatasText.COLOR_TEXT)
        blanco_list = [region for region, (pos, wine_type) in self.controller.model.aoc_wine.items()
                       if wine_type == BLANCO]
        self.blanco_var = tk.StringVar(self.menu_grid, blanco_list[0])
        self.blanco_list_menu = tk.OptionMenu(self.menu_grid, self.blanco_var, *blanco_list,
                                              command=self.controller.locate_region)
        # Positionner les labels et les menus déroulants dans la grille :
        self.tinto_label.grid(row=0, column=0, padx=UISettings.PAD_X_MENU, pady=UISettings.PAD_Y_MENU)
        self.blanco_label.grid(row=0, column=1, padx=UISettings.PAD_X_MENU, pady=UISettings.PAD_Y_MENU)
        self.tinto_list_menu.grid(row=1, column=0, padx=UISettings.PAD_X_MENU, pady=UISettings.PAD_Y_MENU)
        self.blanco_list_menu.grid(row=1, column=1, padx=UISettings.PAD_X_MENU, pady=UISettings.PAD_Y_MENU)

    def set_position(self, x: float, y: float, marker: bool, icon) -> None:
        """
        Positionne la carte sur les coordonnées GPS spécifiées et affiche un marqueur avec l'icône spécifiée.

        :param x: (float) La coordonnée GPS de longitude.
        :param y: (float) La coordonnée GPS de latitude.
        :param marker: Un booléen indiquant si un marqueur doit être affiché sur la carte à la position spécifiée.
        :param icon: (PhotoImage) L'icône à afficher sur le marqueur.
        :return: None
        """
        self.map_widget.set_position(x, y, marker=marker, icon=icon)

    def set_zoom(self, zoom: int) -> None:
        """
        Pour zoomer sur la carte.

        :param zoom: (int) Niveau de zoom.
        :return: None
        """
        self.map_widget.set_zoom(zoom)

    def wine_icon(self, region: str):
        """
        Retourne l'icône appropriée selon le type de vin pour son affichage.

        :param region: (str) Le nom de la région viticole sélectionnée.
        :return: (PhotoImage) L'icône à afficher.
        """
        wine_type = self.controller.model.get_wine_info(region)[1]
        return self.tinto_icon if wine_type == TINTO else self.blanco_icon


if __name__ == "__main__":
    root = tk.Tk()
    data = WineDatas()
    control = WineController(data, None)
    app = WineUI(root, control)
    control.view = app
    root.resizable(False, False)  # Fixe la taille de l'application
    root.mainloop()
