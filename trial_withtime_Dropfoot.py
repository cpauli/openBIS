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

class TrialWithTime(object):
    """
    Constructs a Trial object.
    """
    
    output = widgets.Output(clear_output = True)
     
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
               
        self.table_rows = []
        self.grid = None
        self.counter = 0
        self.has_time = args[2]
        self.screen = args[4]
        if self.has_time:
            self.textform = args[3]
        
        for i in range(0,args[1]):
            value = args[0]
            self.table_rows.append(self.create_new_row(i, value))
            
        if self.has_time:
            self.stepcount = self.count_steps()
        
        self.grid = self.create_new_grid()
        self.show()
            
    def create_new_row(self, i, value):
        """
        Creation of a new a Trial row.
        """
        if self.has_time:
            
            row = [widgets.Text(value=value, placeholder='', description='', disabled=False, layout=widgets.Layout(width='auto')),
                   widgets.Text(value='', layout=widgets.Layout(width='auto')),
                   widgets.Checkbox(value=False, description='L', indent=False, layout=widgets.Layout(width='auto')),
                   widgets.Checkbox(value=False, description='R', indent=False, layout=widgets.Layout(width='auto')),
                   widgets.Text(layout=widgets.Layout(width='auto'))]
            row[2].observe(self.count_steps)
            row[3].observe(self.count_steps)
        else:
            row = [widgets.Text(value=value, placeholder='', description='', disabled=False, layout=widgets.Layout(width='auto')),
                   widgets.Text(layout=widgets.Layout(width='auto'))]
        return row
        
    def create_new_grid(self):
        """
        Creation of a new grid for the Trial representation.
        """
        if self.has_time:
            hlabels = ['Dateiname', 'Zeit', 'Treffer links', 'Treffer rechts', 'Kommentare']
            screen_width = (str(self.screen(0)-(0.05*self.screen(0))) + 'px')
            grid = GridspecLayout(len(self.table_rows)+2, len(hlabels), width=screen_width)

            for r in range(0, len(self.table_rows)+1):
                for c in range(0, len(hlabels)):
                    if r == 0:
                        grid[r,c] = widgets.Label(hlabels[c], layout=widgets.Layout(width='auto'))
                    else:
                        grid[r,c] = self.table_rows[r-1][c] 
        else:
            hlabels = ['Dateiname', 'Kommentare']
            grid = GridspecLayout(len(self.table_rows)+1, len(hlabels))

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

    def showo(self):
        """
        Show the Trial object output to the user.
        """
        display(self.output)
    
    @output.capture(clear_output = True, wait = True)
    
    def count_steps(self, *args):
        if self.has_time:
            treffer_links = 0
            treffer_rechts = 0
            for i in range(0, len(self.table_rows)):
                if self.table_rows[i][2].value == True:
                    treffer_links += 1
                
                if self.table_rows[i][3].value == True:
                    treffer_rechts += 1
        
            if treffer_links >= self.textform.meas_step_count["links"]:
                style_name_links = 'success'
            elif treffer_links < self.textform.meas_step_count["links"]:
                style_name_links = 'danger'
            
            if treffer_rechts >= self.textform.meas_step_count["rechts"]:
                style_name_rechts = 'success'
            elif treffer_rechts < self.textform.meas_step_count["rechts"]:
                style_name_rechts = 'danger'
            StepCount = widgets.HBox([
            widgets.Button(description="Linke Schritte: " + str(treffer_links), button_style=style_name_links),
            widgets.Button(description="Rechte Schritte: " + str(treffer_rechts), button_style=style_name_rechts)])
            self.stepcount = StepCount
            display(self.stepcount)
            return StepCount
        
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