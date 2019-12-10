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

import ipywidgets as widgets
from ipywidgets import widgets, GridspecLayout
import numpy as np

__author__ = 'Andreas P. Cuny'

class StudyCriteria(object):
    """
    Constructs a StudyCriteria object.
    """
     
    def __init__(self, *args):
        """
        Constructs a StudyCriteria object.
        """
        self.input_crit = args[0]
        self.valid_criterion = args[1]
        self.screen = args[2]
        self.grid = self.create_new_grid()
        
    def create_new_grid(self):
        
        style = {'description_width':'initial'}
        
        # Set names of in-/exclusion criteria
        for i, value in enumerate(self.input_crit):
            setattr(self, "label%s" % (i), widgets.Label(value=value, layout=widgets.Layout(width='auto')))
            setattr(self, "widget%s" % (i), widgets.Dropdown(options=[(' ', 0),('Ja', 1), ('Nein', 2)], value=1, description='', style=style, layout=widgets.Layout(width='80px')))
            
        # Construct table for showing in-/exclusion criteria (number irrelevant)
        grid = GridspecLayout(len(self.input_crit), 2)
        
        for r in range(0, len(self.input_crit)):
            grid[r,0] = getattr(self, "label%s" % (r))
            
        for c in range(0, len(self.input_crit)):
            grid[c,1] = getattr(self, "widget%s" % (c))
                
        return grid
    
    def show(self):
        """
        Show the Trial object to the user.
        """
        display(self.grid)
        
    def validate(self):
        """
        Validation of study criteria.
        """
        val_list = []
        for i in range(0, int(len(self.input_crit))):
            w = getattr(self, "widget%s" % (i))
            val_list.append(w.value)
        mean_val = np.mean(val_list)
        return self.checkEqual(mean_val)
            
    def checkEqual(self, lst):
        """
        Equality check.
        """
        if lst == self.valid_criterion:
            res = True
            return res
        else:
            res = False
            return res
#         return not lst or lst.count(self.valid_criterion) == mean(lst)
     
    def get(self):
        """
        Returns the object state as dict.
        """
        return self.__dict__
     