# /********************************************************************************
# * Copyright © 2019, Andreas P. Cuny
# * All rights reserved. This program and the accompanying materials
# * are made available under the terms of the GNU Public License v3.0
# * which accompanies this distribution, and is available at
# * http://www.gnu.org/licenses/gpl
# *
# * Contributors:
# *     Andreas P. Cuny - initial API and implementation
# *     Carole A. Pauli - project specific adaptations and add-ons
# *******************************************************************************/

from ipywidgets import widgets, GridspecLayout
import math
from validate_range_Dropfoot import ValidateRange

__author__ = 'Andreas P. Cuny & Carole Pauli'

class ParticipantInfo(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output()
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        self.part_info = args[0]
        self.screen = args[1]
#         self.participant = dict()
        self.grid = self.create_new_grid()
        self.grid_fersen = self.create_grid_fersen()
#         self.field_filled = self.on_field_filled()
        
        self.erkrankung = widgets.HBox([widgets.Checkbox(value=False, description=self.part_info.participant_info_erkrankung[0], disabled=False), 
                                        widgets.Checkbox(value=False, description=self.part_info.participant_info_erkrankung[1], disabled=False), 
                                        widgets.Checkbox(value=False, description=self.part_info.participant_info_erkrankung[2], disabled=False), 
                                        widgets.Text(value='', placeholder='', description='', disabled=False)], layout=widgets.Layout(width='auto'))
          
    def create_new_grid(self):
        style = {'description_width':'initial'}
        
        for i, value in enumerate(self.part_info.participant_info_name):
            setattr(self, "participant%s" % (i), widgets.Text(value='', placeholder='', description=value, disabled=False, style=style, layout=widgets.Layout(width='500px')))
        
        grid = GridspecLayout(len(self.part_info.participant_info_name),1)
        
        for r, value in enumerate(self.part_info.participant_info_name):
                grid[r,0] = getattr(self, "participant%s" % (r))
        
        return grid
    
    def create_grid_fersen(self):
        style = {'description_width':'initial'}
        
        for j, value in enumerate(self.part_info.participant_info_fersengang):
                setattr(self, "fersengang%s" % (j), widgets.Dropdown(options=[(' ', 0),('möglich', 1), ('unmöglich', 2)], value=0, description=value, style=style, layout=widgets.Layout(width='500px')))
                
        grid_fersen = GridspecLayout(len(self.part_info.participant_info_fersengang),2)
        
        for s, value in enumerate(self.part_info.participant_info_fersengang):
                grid_fersen[s,0] = getattr(self, "fersengang%s" % (s))                                                     
                
        return grid_fersen
    
    def show_grid(self):
        """
        Show the Trial object to the user.
        """
        display(self.grid)
        
    def show_grid_fersen(self):
        display(self.grid_fersen)
        
#     def on_field_filled(self,*args):
        
#         for i, value in enumerate(self.part_info.participant_info_name):
#             if self.part_info.participant_info_name.get(self.participant[i].description)[0] > self.participant[i].value:
#                 widgets.Valid(value=False, description='Der eingegebene Wert ist zu tief',  style={'description_width':'initial'})
#             elif self.part_info.participant_info_name.get(self.participant[i].description)[1] < self.participant[i].value:
#                 widgets.Valid(value=False, description='Der eingegebene Wert ist zu hoch',  style={'description_width':'initial'})
#             else:
#                 widgets.Valid(value=True, description='',  style={'description_width':'initial'})
                
    def get(self):
        """Returns the object state as dict."""
        
        return self.__dict__