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

class StudyMetadata(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Constructs a Trial object.
        """
        self.study_metadata = widgets.VBox([widgets.DatePicker(description='Datum', disabled=False, style={'description_width':'initial'}),
                      widgets.Text(value='', placeholder='Subject ID eingeben', description='Subject ID:',disabled=False),
                      widgets.Text(value='', placeholder='Name Investigator', description='Investigator',disabled=False, style={'description_width':'initial'})])