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

class QuestKlinUntersuch(object):
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
        self.screen = args[0]
        self.q1 = []
        self.q2 = []
        self.q3 = []
        
        # Fragen für Fragebogen
        self.q1.append(widgets.Text(value='', description='Name des Untersuchers/-in:', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Text(value='', description='Ort, Datum:', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.HTML(value='', description='<b>Körperfunktionen/-strukturen</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', placeholder='', description='Anamnese (kurz):', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q1.append(widgets.Textarea(value='', placeholder='', description='Inspektion, ggf. Palpation (Haut, Durchblutung, Alignement) bei Auffälligkeiten', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.HTML(value='', description='<b>rechts</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.HTML(value='', description='<b>links</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='OSG: pROM (DE/PF (20-0-40))', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='OSG: aROM (DE/PF (20-0-40))', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.HTML(value='', description='<b>Muskelfunktion (in MFT Werten)</b>', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='M. tibialis ant (OSG DE)', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='M. triceps surae (OSG PF)', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='M. tibialis posterior (USG Supination/Inversion)', description='Label', style=style, layout=widgets.Layout(width='auto')))
                
        self.q2.append(widgets.Label(value='M. hallucis longus (USG Pronation/Eversion)', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='M. extensor hallucis longus (DIG I Grundgelenk Extension)', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.HTML(value='', description='<b>OSG, Spastik; gemessen an der Modified Ashworth Scale (0-4, 0 keine Einschränkung)</b>', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='Plantarflexion', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q2.append(widgets.Label(value='Dorsalextension', description='Label', style=style, layout=widgets.Layout(width='auto')))
        
        self.q3.append(widgets.Text(value='', description='FAC Score (Anamnestisch) (0-5, 5 unabhängig)', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q3.append(widgets.Text(value='', description='Mini Mental Status (nur bei Auffälligkeiten in Anamnese) (0-30, 30 keine Einschränkung)', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        self.q3.append(widgets.Textarea(value='', description='Bemerkungen', disabled=False, style=style, layout=widgets.Layout(width='auto')))
        
        # Zusammensetzen des Fragebogens für Anzeige
        screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
        self.klinunt1 = widgets.VBox([self.q1[0],self.q1[1],self.q1[2],self.q1[3],self.q1[4]])
        
        grid = GridspecLayout(len(self.q2)-1,3,width=screen_width)
        grid[0,0] = widgets.Label(value='')
        
        for i, value in enumerate(self.q2):
            if i == 0 or i == 1:
                grid[0,i+1] = self.q2[i]
            elif i == 4 or i == 10:
                grid[i-1,0:] = self.q2[i]
            else:
                grid[i-1,0] = self.q2[i]
                grid[i-1,1] = widgets.Text(value='', description='', disabled=False, style=style, layout=widgets.Layout(width='auto'))
                grid[i-1,2] = widgets.Text(value='', description='', disabled=False, style=style, layout=widgets.Layout(width='auto'))
               
        self.klinunt2 = grid
        
        self.klinunt3 = widgets.VBox([self.q3[0],self.q3[1],self.q3[2]])