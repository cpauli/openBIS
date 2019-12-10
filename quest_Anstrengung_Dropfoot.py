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

class QuestAnstrengung(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output()
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        
        # Fragen für Fragebogen
        self.anstrengung = ["# Bewertung der empfundenen Anstrengung", 
                            args[0], 
                            "Wie angestrengt fühlten sich Ihre Beine während der Aufgabe an? Könnten Sie Ihre wahrgenommene Anstrengung während der gerade erledigten Aufgabe bewerten?", 
                            "<b>Aufgabe</b>", 
                            "<b>Anstrengung</b>",
                            args[1][3:-36]]
                
        style = {'description_width':'initial'}
        
        display(Markdown(self.anstrengung[0]))
        display(Markdown("## " + self.anstrengung[1]))
        display(Markdown(self.anstrengung[2]))
        
        grid_num = GridspecLayout(2,2)
        for i, value in enumerate(self.anstrengung):
            if i > 2:
                if i % 2 == 0:
                    grid_num[0,1] = widgets.HTML(value=self.anstrengung[i], style=style, layout=widgets.Layout(width='400px'))
                else:
                    grid_num[int((i-3)/2),0] = widgets.HTML(value=self.anstrengung[i], style=style, layout=widgets.Layout(width='400px'))
                    
        grid_num[1,1] = widgets.Text(value='', description='', style=style, layout=widgets.Layout(width='400px'))
        display(grid_num)
        self.anstrengung_num = grid_num
        
        image = mpimg.imread("AnstrengungSkala.png")
        plt.imshow(image)
        plt.show()
        
    def show(self):
        display(self.anstrengung_num)