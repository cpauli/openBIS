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

class ValidateRange(object):
    """
    Constructs a Trial object.
    """
    
     
    def __init__(self, *args):
        """Constructs a Trial object."""
        
        self.input_value = args[0]
        self.range_min = args[1]
        self.range_max = args[2]
                
    def validate(self):
        """Validation of value range"""
        
        if self.input_value != '':
            if int(self.input_value) < self.range_min:
                self.val_part = false
            elif int(self.input_value) > self.range_max:
                self.val_part = false
            else:
                self.val_part = true
    
    def get(self):
        """Returns the object state as dict."""
        
        return self.__dict__