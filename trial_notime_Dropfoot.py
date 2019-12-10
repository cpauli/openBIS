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

__author__ = 'Andreas P. Cuny & Carole Pauli'

class TrialNoTime(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output()
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
               
        self.table_rows = []
        self.grid = None
        self.counter = 0
        self.screen = args[2]
        for i in range(0,args[1]):
            value = args[0]
            self.table_rows.append(self.create_new_row(i, value))
        
        self.grid = self.create_new_grid()
        self.show()
        
            
    def create_new_row(self, i, value):
        """
        Creation of a new a Trial row.
        """
        row = [widgets.Text(value=value, placeholder='', description='', disabled=False, layout=widgets.Layout(width='auto')),
                   widgets.Text(layout=widgets.Layout(width='auto'))]
        return row
        
    def create_new_grid(self):
        """
        Creation of a new grid for the Trial representation.
        """

        hlabels = ['Dateiname', 'Kommentare']
        screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
        grid = GridspecLayout(len(self.table_rows)+1, len(hlabels), width=screen_width)

        for r in range(0, len(self.table_rows)+1):
            for c in range(0, len(hlabels)):
                if r == 0:
                    grid[r,c] = widgets.Label(hlabels[c])
                else:
                    grid[r,c] = self.table_rows[r-1][c]
                        
        return grid
    
    def show(self):
        """
        Show the Trial object to the user.
        """
        display(self.grid)

    def get_object_state(self):
        """
        Returns the state of the Trial object as a list i.e. to save the values.
        """
        states = {}
        row_val = []
        for c in range(0, len(self.table_rows[0])):
                row_val.append(self.grid[0,c].value)
                
        states['header'] = row_val
        
        row_list = []
        for r in range(0, len(self.table_rows)):
            row_val = []
            for c in range(0, len(self.table_rows[0])):
                row_val.append(self.grid[r+1,c].value)
            row_list.append(row_val)
            
        states['row_state'] = row_list
        return states