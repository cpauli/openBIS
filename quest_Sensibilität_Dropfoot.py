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

__author__ = 'Andreas P. Cuny & Carole Pauli'

class QuestSensibilitaet(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output()
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
#         self.BildSens = Image.open("Sensibilität.png");

        # Definition Stil des Fragebogens
        style = {'description_width':'initial'}
        self.q2 = []
        self.screen = args[0]
        
        # Fragen für Fragebogen
        self.sens1 = "Info: Die Messungen werden im Sinne einer Neurologischen Standard-Testung zirkulär an beiden unteren Extremitäten durchgeführt. Es wird eine Light Touch und eine Sharp-Dull Messung durchgeführt. Die Nummer 5 wird rein anamnestisch erfragt."
        
        self.q2.append(widgets.HTML(value='', description='<b>Messpunkt</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.HTML(value='', description='<b>Light-Touch*</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.HTML(value='', description='<b>Sharp-Dull*</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.HTML(value='', description='<b>Anmerkungen</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='1 Fuss re', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='2 Unterschenkel re', description='Label', style=style, layout=widgets.Layout(width='auto')))
                        
        self.q2.append(widgets.Label(value='3 Knie re', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='4 Oberschenkel re', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='5 (anamnestisch, Becken und Gesässbereich)', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='6 Oberschenkel li', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='7 Knie li', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='8 Unterschenkel li', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='9 Fuss li', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        # Zusammensetzen des Fragebogens für Anzeige     
        screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
        grid = GridspecLayout(len(self.q2)-3,4,width=screen_width)
        
        for i, value in enumerate(self.q2):
            if 0 <= i <= 3:
                grid[0,i] = self.q2[i]
            else:
                grid[i-3,0] = self.q2[i]
                grid[i-3,1] = widgets.Checkbox(value=False, description='', disabled=False, style=style, layout=widgets.Layout(width='auto'))
                grid[i-3,2] = widgets.Checkbox(value=False, description='', disabled=False, style=style, layout=widgets.Layout(width='auto'))
                grid[i-3,3] = widgets.Text(value='', description='', disabled=False, style=style, layout=widgets.Layout(width='auto'))
               
        self.sens2 = grid