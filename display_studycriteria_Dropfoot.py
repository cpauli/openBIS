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

class DisplayStudyCriteria(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        self.textform = args[0];
        self.inc_crit = args[1];
        self.ex_crit = args[2];
        
        display(Markdown(self.textform.incex_title[0]))
        display(Markdown(self.textform.incex_title[1]))
        display(Markdown(self.textform.incex_title[2]))
        display(self.inc_crit.show())
        display(Markdown(self.textform.incex_title[3]))
        display(Markdown(self.textform.incex_title[4]))
        display(self.ex_crit.show())
        display(Markdown("# Kommentare / Anmerkungen"))
        self.komm_criteria = widgets.Textarea(value='', description='', disabled=False, style={'description_width':'initial'}, layout=widgets.Layout(width='auto'))
        display(self.komm_criteria)