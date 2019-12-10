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

class QuestUsability(object):
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
        self.q1 = []
        self.screen = args[1]
        
        # Fragen für Fragebogen
        self.q1.append(widgets.HTML(value='', description='<b>Aussage (1 = Trifft gar nicht zu; 5 = Trifft voll zu)</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich denke, dass ich dieses System gerne regelmäßig nutzen würde.', style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich fand das System unnötig komplex.', style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich denke, das System war leicht zu benutzen.', style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich denke, ich würde die  Unterstützung einer fachkundigen Person benötigen, um das System benutzen zu können.', style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich fand, die verschiedenen Funktionen des Systems waren gut integriert.', style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Label(value='Ich halte das System für zu inkonsistent.', style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Label(value='Ich glaube, dass die meisten Menschen sehr schnell lernen würden, mit dem System umzugehen.', style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Label(value='Ich fand das System sehr umständlich zu benutzen.', style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Label(value='Ich fühlte mich bei der Nutzung des Systems sehr sicher.', style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Label(value='Ich musste viele Dinge lernen, bevor ich  mit dem System arbeiten konnte.', style=style, layout=widgets.Layout(width='auto')))
                
        # Zusammensetzen des Fragebogens für Anzeige
        display(Markdown("# System usability scale"))
        display(Markdown("## " + args[0]))
        
        screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
        grid = GridspecLayout(len(self.q1),10,width=screen_width)
        grid[0,0:] = self.q1[0]
        
        for i in range(0, len(self.q1)):
            if i > 0:
                grid[i,:4] = self.q1[i]
                grid[i,5] = widgets.Checkbox(value=False, description=str(1), disabled=False, layout=widgets.Layout(width='auto'))
                grid[i,6] = widgets.Checkbox(value=False, description=str(2), disabled=False, layout=widgets.Layout(width='auto'))
                grid[i,7] = widgets.Checkbox(value=False, description=str(3), disabled=False, layout=widgets.Layout(width='auto'))
                grid[i,8] = widgets.Checkbox(value=False, description=str(4), disabled=False, layout=widgets.Layout(width='auto'))
                grid[i,9] = widgets.Checkbox(value=False, description=str(5), disabled=False, layout=widgets.Layout(width='auto'))
               
        self.usability = grid
        display(self.usability)