# /********************************************************************************
# * Copyright © 2019, Andreas P. Cuny
# * All rights reserved. This program and the accompanying materials
# * are made available under the terms of the GNU Public License v3.0
# * which accompanies this distribution, and is available at
# * http://www.gnu.org/licenses/gpl
# *
# * Contributors:
# *     Andreas P. Cuny - initial API and implementation
# *******************************************************************************/

from ipywidgets import widgets, GridspecLayout
from IPython.display import Markdown
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

__author__ = 'Andreas P. Cuny & Carole Pauli'

class QuestDruck(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output()
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        
        # Definition Stil des Fragebogens
        style = {'description_width':'initial'}
        
        # Fragen für Fragebogen
        self.druck = ["# Bewertung des wahrgenommenen Drucks", 
                      args[0], 
                      "Haben Sie während dem Gehen Druckstellen an den Unteren Extremitäten gespürt? Wenn ja, zeichnen Sie bitte den Ort/die Orte unten im Bild mit aufsteigenden Nummern ein und bewerten Sie den Druck auf einer Skala von 0-10 (siehe unten). Beim Feld Nummerierung können sie die Zahl zu der entsprechenden Druckstelle eintragen.", 
                      "Nummerierung (Anzahl empfundener Druckstellen, mit den Werten)", 
                      "Skala"]
        
        display(Markdown(self.druck[0]))
        display(Markdown("## " + self.druck[1]))
        display(Markdown(self.druck[2]))
        image1 = mpimg.imread("Druckstellen.png")
        plt.imshow(image1)
        plt.show()
        display(Markdown("## " + self.druck[3]))
        grid_num = GridspecLayout(2,15)
        for i in range(1,15):
            grid_num[0,i-1] = widgets.Label(value=str(i), style=style, layout=widgets.Layout(width='50px'))
            grid_num[1,i-1] = widgets.Text(value='', description='', disabled=False, style=style, layout=widgets.Layout(width='50px'))
        display(grid_num)
        self.druck_num = grid_num
        
        display(Markdown("## " + self.druck[4]))

        image2 = mpimg.imread("DruckSkala.png")
        plt.imshow(image2)
        plt.show()