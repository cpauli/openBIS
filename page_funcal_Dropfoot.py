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
from trial_notime_Dropfoot import TrialNoTime

__author__ = 'Andreas P. Cuny & Carole Pauli'

class FunCalPage(object):
    """
    Constructs a Trial object.
    """
         
    def __init__(self, *args):
        """
        Initialization of FunCal trial.
        """
        if len(args) == 4:
            self.fc = args[3];
        
        self.textform = args[0];
        self.meta = args[1];
        self.screen = args[2]
        
        part_ID = str(self.meta.study_metadata.children[1].value)
        
        display(Markdown(self.textform.funcal_names[0]))
        display(Markdown(self.textform.funcal_names[1]))
        display(Markdown(self.textform.funcal_names[2]))
        display(Markdown(self.textform.funcal_names[3]))
        if len(args) == 4:
            self.FunCal1 = self.fc.FunCal1
            self.FunCal1.show()
        else:
            self.FunCal1 = TrialNoTime(part_ID + '_xxx_static', 3, self.screen)
            display(self.FunCal1.output)
        display(Markdown("---"))
        display(Markdown(self.textform.funcal_names[4]))
        display(Markdown(self.textform.funcal_names[6]))
        if len(args) == 4:
            self.FunCal2 = self.fc.FunCal2
            self.FunCal2.show()
        else:
            self.FunCal2 = TrialNoTime(part_ID + '_xxx_kne_flexex_L_', 4, self.screen)
            display(self.FunCal2.output)
        display(Markdown("---"))
        display(Markdown(self.textform.funcal_names[5]))
        display(Markdown(self.textform.funcal_names[6]))
        if len(args) == 4:
            self.FunCal3 = self.fc.FunCal3
            self.FunCal3.show()
        else:
            self.FunCal3 = TrialNoTime(part_ID + '_xxx_kne_flexex_R_', 4, self.screen)
            display(self.FunCal3.output)
        display(Markdown("---"))
        display(Markdown(self.textform.funcal_names[7]))
        display(Markdown(self.textform.funcal_names[9]))
        if len(args) == 4:
            self.FunCal4 = self.fc.FunCal4
            self.FunCal4.show()
        else:
            self.FunCal4 = TrialNoTime(part_ID + '_xxx_hip_circumd_L_', 4, self.screen)
            display(self.FunCal4.output)
        display(Markdown("---"))
        display(Markdown(self.textform.funcal_names[8]))
        display(Markdown(self.textform.funcal_names[9]))
        if len(args) == 4:
            self.FunCal5 = self.fc.FunCal5
            self.FunCal5.show()
        else:
            self.FunCal5 = TrialNoTime(part_ID + '_xxx_hip_circumd_R_', 4, self.screen)
            display(self.FunCal5.output)
        display(Markdown("---"))