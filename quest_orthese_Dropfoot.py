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

__author__ = 'Andreas P. Cuny & Carole Pauli'

class QuestOrthese(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        self.textform = args[0]
        self.screen = args[1]
        
        if self.screen(0) < 500:
            width = self.screen(0)
        else:
            width = 500
            
        style = {'description_width':'initial'}
        
        self.orthese = widgets.VBox([widgets.Dropdown(options=[(' ', 0),('Ja*', 1), ('Nein', 2)], value=0, description=self.textform.pruef_orthese[1], style=style, layout=widgets.Layout(width=(str(width) + 'px'))), 
                                      widgets.Dropdown(options=[(' ', 0),('Ja', 1), ('Nein*', 2)], value=0, description=self.textform.pruef_orthese[2], style=style, layout=widgets.Layout(width=(str(width) + 'px'))), 
                                      widgets.Dropdown(options=[(' ', 0),('Ja', 1), ('Nein*', 2)], value=0, description=self.textform.pruef_orthese[3], style=style, layout=widgets.Layout(width=(str(width) + 'px'))), 
                                      widgets.Dropdown(options=[(' ', 0),('Ja', 1), ('Nein*', 2)], value=0, description=self.textform.pruef_orthese[4], style=style, layout=widgets.Layout(width=(str(width) + 'px')))])                        