# /********************************************************************************
# * Copyright © 2019, Andreas P. Cuny
# * All rights reserved. This program and the accompanying materials
# * are made available under the terms of the GNU Public License v3.0
# * which accompanies this distribution, and is available at
# * http://www.gnu.org/licenses/gpl
# *
# * Contributors:
# *     Carole A. Pauli - initial API and implementation
# *******************************************************************************/

from ipywidgets import widgets

__author__ = 'Carole A. Pauli'

class StepCount(object):
         
    def __init__(self, *args):
        """ Initialization of step counting box. """
        
        treffer_links = 0
        treffer_rechts = 0
        
        for i in range(0,len(args[0].shoeOF.table_rows)):
            if args[0].shoeOF.table_rows[i][2].value == True:
                treffer_links += 1
                
            if args[0].shoeOF.table_rows[i][3].value == True:
                treffer_rechts += 1
        
        if treffer_links >= args[1].meas_step_count["links"]:
            style_name_links = 'lightgreen'
        elif treffer_links < args[1].meas_step_count["links"]:
            style_name_links = 'danger'
            
        if treffer_rechts >= args[1].meas_step_count["rechts"]:
            style_name_rechts = 'lightgreen'
        elif treffer_rechts < args[1].meas_step_count["rechts"]:
            style_name_rechts = 'danger'

        self.StepCount = widgets.HBox([
            widgets.Button(description="Linke Schritte: " + str(treffer_links), button_style=style_name_links),
            widgets.Button(description="Rechte Schritte: " + str(treffer_rechts), button_style=style_name_rechts)])