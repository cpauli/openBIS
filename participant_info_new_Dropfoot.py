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
from .validate_range import ValidateRange

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
        self.part_rows = []
        self.grid_part = None

        for i, description in enumerate(self.part_info.participant_info_name):
            self.part_rows.append(self.create_part(i, description))
            
        self.grid_part = self.create_grid_part()
        self.field_filled = self.on_field_filled()
        self.show()
        
    def create_part(self, *args):
        part = widgets.Text(value='', placeholder='', description=args[1], disabled=False)
        part.observe(self.on_field_filled)
        
    def create_grid_part(self):
    
        grid_part = GridspecLayout(len(self.part_info.participant_info_name),1)
        
        for r in range(0, len(self.part_info.participant_info_name)):
                grid_part[r,0] = self.part_rows[r][0]
        
        return grid_part
    
    def show(self):
        """
        Show the Trial object to the user.
        """
        display(self.grid_part)
        
    def on_field_filled(self,*args):
        
        for i, value in enumerate(self.part_info.participant_info_name):
            if self.part_info.participant_info_name.get(self.participant[i].description)[0] > self.participant[i].value:
                widgets.Valid(value=False, description='Der eingegebene Wert ist zu tief',  style={'description_width':'initial'})
            elif self.part_info.participant_info_name.get(self.participant[i].description)[1] < self.participant[i].value:
                widgets.Valid(value=False, description='Der eingegebene Wert ist zu hoch',  style={'description_width':'initial'})
            else:
                widgets.Valid(value=True, description='',  style={'description_width':'initial'})
                
    def get(self):
        """Returns the object state as dict."""
        
        return self.__dict__