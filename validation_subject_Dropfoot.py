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

__author__ = 'Andreas P. Cuny & Carole Pauli'

class ValidationSubject(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
               
        inc = args[0].validate()
        ex = args[1].validate()
        wizard_page = args[3]
        
        ## Validate In-/Exclusion criteria ##
        if wizard_page == 4:
            if inc and ex == True:
                self.validator = widgets.Valid(value=True, description='Subject ist geeignet für die Studie',  style={'description_width':'initial'})
            else:
                self.validator = widgets.Valid(value=False, description='Subject ist nicht geeignet für die Studie',  style={'description_width':'initial'})
                self.wizard_page = 100
    
        ## Validate BMI ##
#         if wizard_page == 2:
            
#             bmi = float(args[2].participant2.value) / ((float(args[2].participant1.value))**2)
#             if bmi >= 18 and bmi <= 28:
#                 self.validator2 = widgets.Valid(value=True, description='BMI ist im vorgegebenen Bereich',  style={'description_width':'initial'})
#             elif bmi < 18:
#                 self.validator2 = widgets.Valid(value=False, description='BMI ist zu tief',  style={'description_width':'initial'})
#             elif bmi > 28:
#                 self.validator2 = widgets.Valid(value=False, description='BMI ist zu hoch',  style={'description_width':'initial'})
#                 self.wizard_page = 100
                
            