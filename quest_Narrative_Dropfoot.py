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

class QuestNarrative(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        # Definition Stil des Fragebogens
        style = {'description_width':'initial'}
        self.q1 = []
        self.screen = args[1]
        
        # Fragen für Fragebogen
        self.q1.append(widgets.HTML(value='', description='<b>1) Generelle Funktion</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Konnte das Gerät wie vorgesehen gestartet werden?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Funktionierte das Gerät während der Testung oder gab es Abstürze (Anzahl Abstürze notieren)?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Falls es einen Absturz gab: Wie lange dauerte es bis das Gerät wieder betriebsbereit war?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Wie aufwendig war es, das Gerät anzuziehen? Wie lange dauerte das An- und Abziehen?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Unterstützte das Gerät die Bewegung während allen Gehstrecken (Beschreibe die Limitierungen)?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Stoppte das Gerät seine Funktion wie vorgesehen (z.B. beim Ausschalten, beim normalen Stehen)?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Textarea(value='', description='Was waren die Hauptgründe, welche die Basisfunktion des Gerätes während dem Gehen einschränkten? ', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Was waren weitere Gründe welche die Basisfunktion des Gerätes während dem Gehen einschränkten? ', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Textarea(value='', description='War das Gerät während der ganzen Messung intakt (notiere Anzahl der Vorkommnisse oder z.B. verlorene/gebrochene Teile wie z.B. Strings)? ', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Textarea(value='', description='Generelle Kommentare:', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.HTML(value='', description='<b>2) Batterie</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q1.append(widgets.Textarea(value='', description='Notiere die Zeit während der das System in Betrieb war und den Verbrauch der Hauptbatterie über die Zeit:', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Falls nötig: Konnte die Hauptbatterie einfach wieder aufgeladen werden?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Kann die Hauptbatterie während dem Laden ersetzt werden mit einer geladenen Batterie?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Wie lange war die Batterie von WLAN-Tools in Betrieb? Mussten diese während dem Messen neu aufgeladen werden?', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', description='Kommentare zu der Batterie und der Betriebsdauer der Batterie:', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        # Zusammensetzen des Fragebogens für Anzeige
        display(Markdown("# Narrative Report"))
        display(Markdown("## " + args[0]))
        
        screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
        grid = GridspecLayout(len(self.q1),1,width=screen_width)
        
        for i, value in enumerate(self.q1):
            grid[i,0] = self.q1[i]
               
        self.narrative = grid
        display(self.narrative)