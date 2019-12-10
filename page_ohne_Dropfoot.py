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
from trial_withtime_Dropfoot import TrialWithTime
from trial_notime_Dropfoot import TrialNoTime

__author__ = 'Andreas P. Cuny & Carole Pauli'

class PageOhne(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        self.textform = args[0];
        self.meta = args[1];
        self.screen = args[2]
        if len(args) == 4:
            self.tr = args[3];
            
        if len(args) == 4:
            self.Lichtschranken = self.tr.Lichtschranken
            self.TimeRange = self.tr.TimeRange
            self.druck_num = self.tr.druck_num
            self.anstrengung_num = self.tr.anstrengung_num
        else:
            self.init_Lichtschranken()
            self.init_TimeRange()
            
        part_ID = str(self.meta.study_metadata.children[1].value)
        
        display(Markdown("# " + self.textform.messkonditionen[0]))
        display(Markdown(self.textform.meas_text[0]))
        display(Markdown(self.textform.meas_text[1]))
        if len(args) == 4:
            self.gewicht = self.tr.gewicht
        else:
            self.gewicht = widgets.Text(value='', description=self.textform.meas_text[2], disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='600px'))
        display(self.gewicht)
        display(Markdown(self.textform.meas_text[3]))
        if len(args) == 4:
            self.ohneStat = self.tr.ohneStat
            self.ohneStat.show()
        else:
            self.ohneStat = TrialNoTime(part_ID + '_xxx_static', 3, self.screen)
            display(self.ohneStat.output)
        display(Markdown(self.textform.meas_text[4]))
        display(self.Lichtschranken)
        display(self.TimeRange)
        display(Markdown(self.textform.meas_text[5]))
        display(Markdown(self.textform.meas_text[6]))
        if len(args) == 4:
            self.xxx_xw = self.tr.xxx_xw
            self.xxx_xw.show()
        else:
            self.xxx_xw = TrialWithTime(part_ID + '_xxx_xw', 10, True, self.textform, self.screen)
            display(self.xxx_xw.output)
            
        ## Questionnaire Feedback Druck
        # Definition Stil des Fragebogens
        style = {'description_width':'initial'}
        
        # Fragen für Fragebogen
        self.druck = ["# Bewertung des wahrgenommenen Drucks", 
                      self.textform.messkonditionen[0], 
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
        if len(args) == 4:
            display(self.druck_num)
        else:
            screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
            grid_num = GridspecLayout(2,15,width=screen_width)
            for i in range(1,15):
                grid_width = (str(int((self.screen(0)-(0.1*self.screen(0))) / 14)) + 'px')
                grid_num[0,i-1] = widgets.Label(value=str(i), style=style, layout=widgets.Layout(width=grid_width))
                grid_num[1,i-1] = widgets.Text(value='', description='', disabled=False, style=style, layout=widgets.Layout(width=grid_width))
            display(grid_num)
            self.druck_num = grid_num
        
        display(Markdown("## " + self.druck[4]))

        image2 = mpimg.imread("DruckSkala.png")
        plt.imshow(image2)
        plt.show()
        
        ## Questionnaire Feedback Anstrengung
        # Fragen für Fragebogen
        self.anstrengung = ["# Bewertung der empfundenen Anstrengung", 
                            self.textform.messkonditionen[2], 
                            "Wie angestrengt fühlten sich Ihre Beine während der Aufgabe an? Könnten Sie Ihre wahrgenommene Anstrengung während der gerade erledigten Aufgabe bewerten?", 
                            "<b>Aufgabe</b>", 
                            "<b>Anstrengung</b>",
                            self.textform.meas_text[7][3:-36]]
                
        style = {'description_width':'initial'}
        
        display(Markdown(self.anstrengung[0]))
        display(Markdown("## " + self.anstrengung[1]))
        display(Markdown(self.anstrengung[2]))
        
        if len(args) == 4:
            display(self.anstrengung_num)
        else:
            screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
            grid_num = GridspecLayout(2,2,width=screen_width)
            for i, value in enumerate(self.anstrengung):
                if i > 2:
                    if i % 2 == 0:
                        grid_num[0,1] = widgets.HTML(value=self.anstrengung[i], style=style, layout=widgets.Layout(width='auto'))
                    else:
                        grid_num[int((i-3)/2),0] = widgets.HTML(value=self.anstrengung[i], style=style, layout=widgets.Layout(width='auto'))
                    
            grid_num[1,1] = widgets.Text(value='', description='', style=style, layout=widgets.Layout(width='auto'))
            display(grid_num)
            self.anstrengung_num = grid_num
        
        image = mpimg.imread("AnstrengungSkala.png")
        plt.imshow(image)
        plt.show()
        
    
        display(Markdown("---"))
        display(Markdown("# Kommentare / Anmerkungen"))
        if len(args) == 4:
            self.komm_ohne = self.tr.komm_ohne
            display(self.komm_ohne)
        else:
            self.komm_ohne = widgets.Textarea(value='', description='', disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='auto'))
            display(self.komm_ohne)
            
    def init_Lichtschranken(self):
        """ Initialization of Lichtschranken. """
        self.Lichtschranken = widgets.BoundedFloatText(value=0, min=0.5, max=6, step=0.01, description='Distanz der Lichtschranken [m]', disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='300px'))
    
    def init_TimeRange(self):
        """ Initialization of Time Range. """
        self.TimeRange = widgets.HBox([widgets.BoundedFloatText(value=0, min=0, max=10, step=0.01, description='Zeit range [s]', disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='300px')), widgets.BoundedFloatText(value=0, min=0, max=10, step=0.01, description=' - ', disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='200px'))])