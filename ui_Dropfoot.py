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

import os
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pybis import Openbis
from ipywidgets import widgets
from IPython.display import Markdown
from jinja2 import Environment, FileSystemLoader
from win32api import GetSystemMetrics

from study_criteria_Dropfoot import StudyCriteria
from textfields_Dropfoot import Textfields
from validation_subject_Dropfoot import ValidationSubject
from quest_orthese_Dropfoot import QuestOrthese
from quest_KlinUntersuch_Dropfoot import QuestKlinUntersuch
from quest_Narrative_Dropfoot import QuestNarrative
from participant_info_Dropfoot import ParticipantInfo
from study_metadata_Dropfoot import StudyMetadata
from page_funcal_Dropfoot import FunCalPage
from page_ohne_Dropfoot import PageOhne
from page_aktive_Dropfoot import PageAktive
from page_eigene_Dropfoot import PageEigene
from display_studycriteria_Dropfoot import DisplayStudyCriteria
from step_count_Dropfoot import StepCount
from quest_Sensibilität_Dropfoot import QuestSensibilitaet

__author__ = 'Andreas P. Cuny & Carole Pauli'


class UIDropfoot(object):
    """Constructs a UI object"""
    
    output = widgets.Output()
    
    def __init__(self, *args, **kwagrs):
        """Constructs a UI object""" 
        # Pass those as kwargs while object initialization 
        self.textform = Textfields()

        self.wizard_page = 0
        self.end_page = False

        self.screen = GetSystemMetrics # 0 = width, 1 = height
        self.init_study_metadata()
        self.inc_crit = StudyCriteria(self.textform.including_criteria,1, self.screen);
        self.ex_crit = StudyCriteria(self.textform.excluding_criteria,2, self.screen);
        self.init_quest_orthese()
        self.init_participant_info()
        self.init_KlinUntersuch()
        self.init_Sensibilitaet()
        self.init_openbis_login()
        self.init_new_experimental_step()
        self.init_wizard_btn()
        self.init_save_btn()
        self.shoe_result = set()
        
        if self.wizard_page == 0:
            self.questshoe = dict()
    
    def show_study_start(self):
        """Show the study start form to the user"""
        display(Markdown("# " + self.textform.title[0]))
        display(Markdown("## " + self.textform.title[1]))
        display(self.meta.study_metadata)
        display(Markdown(self.textform.declaration))
        display(Markdown("---"))
        self.show_wizard_btn()
        
    def show_form(self):
        """
        Show the rest of the study form to the user, depending on which page one is.
        """
        # Page 1
        if self.wizard_page == 1:
            # Formular Überprüfung Orthese
            display(Markdown("# " + self.textform.pruef_orthese[0]))
            display(self.orth.orthese)
            display(Markdown(self.textform.pruef_orthese[5]))
            # Participant information (Age, etc.)
            display(Markdown("# Teilnehmer spezifische Informationen / Anthropometrische Daten"))
            display(Markdown("---"))
            self.parti.show_grid()
            display(self.parti.erkrankung)
            self.parti.show_grid_fersen()
            display(self.parti.output)
            # Reihenfolge der Messungen
            display(Markdown("# Reihenfolge der Messungen"))
            self.Messungen = widgets.VBox([widgets.Text(value=self.textform.messkonditionen[0], placeholder='', description=str(1), disabled=False, layout=widgets.Layout(width='500px')), 
                                           widgets.Text(value=self.textform.messkonditionen[1], placeholder='', description=str(2), disabled=False, layout=widgets.Layout(width='500px')), 
                                           widgets.Text(value=self.textform.messkonditionen[2], placeholder='', description=str(3), disabled=False, layout=widgets.Layout(width='500px'))])
            display(self.Messungen)
            
        # Page 2
        elif self.wizard_page == 2:
            display(Markdown("# Klinischer Untersuch"))
            display(self.klin.klinunt1)
            display(self.klin.klinunt2)
            display(self.klin.klinunt3)
            
        # Page 3
        elif self.wizard_page == 3:
            # In-/Exclusion criteria
            self.stud_crit = DisplayStudyCriteria(self.textform, self.inc_crit, self.ex_crit)

        # Page 4
        elif self.wizard_page == 4:
            display(Markdown("# Sensibilitäts-Testung"))        
            image = mpimg.imread("Sensibilität.png")
            plt.imshow(image)
            plt.show()
            display(Markdown(self.sens.sens1))
            display(self.sens.sens2)

        # Page 5
        elif self.wizard_page == 5:
            # Functional calibration
            if hasattr(self,'fc'):
                self.fc = FunCalPage(self.textform, self.meta, self.screen, self.fc)
            else:
                self.fc = FunCalPage(self.textform, self.meta, self.screen)
            
        # Page 6
        elif self.wizard_page == 6:
            # Messung ohne Orthese
            if hasattr(self,'ohneOrth'):
                self.ohneOrth = PageOhne(self.textform, self.meta, self.screen, self.ohneOrth)
            else:
                self.ohneOrth = PageOhne(self.textform, self.meta, self.screen)
            
        # Page 7
        elif self.wizard_page == 7:
            # Messung mit aktiver Fussorthese
            if hasattr(self,'aktiveOrth'):
                self.aktiveOrth = PageAktive(self.textform, self.meta, self.ohneOrth.TimeRange, self.screen, self.aktiveOrth)
            else:
                self.aktiveOrth = PageAktive(self.textform, self.meta, self.ohneOrth.TimeRange, self.screen)
                    
        # Page 8
        elif self.wizard_page == 8:
            # Messung mit eigener Orthese
            if hasattr(self,'eigOrth'):
                self.eigOrth = PageEigene(self.textform, self.meta, self.ohneOrth.TimeRange, self.screen, self.eigOrth)
            else:
                self.eigOrth = PageEigene(self.textform, self.meta, self.ohneOrth.TimeRange, self.screen)
                
        # Page 9
        elif self.wizard_page == 9:
            # Narrativer Report
            if self.end_page:
                display(self.questNarrative.narrative)
            else:
                self.init_FeedbackNarrative()
                  
        # Page 10
        elif self.wizard_page == 10:
            # Save form to html and to openBIS
            self.end_page = True
            self.upload_to_openbis()
            display(Markdown("---"))

    ## -------------------------------------------------------------------------------- ##
    ## Initialization ##
    def init_study_metadata(self):
        """ Initialization of study metadata on date, participant id and investigator."""
        self.meta = StudyMetadata()
    
    def init_participant_info(self):
        """Initialization of participant information on age, height and weight."""
        self.parti = ParticipantInfo(self.textform, self.screen)
        
    def init_quest_orthese(self):
        """Initialization of participant information on age, height and weight."""
        self.orth = QuestOrthese(self.textform, self.screen)
        
    def init_KlinUntersuch(self):
        """Initialization of "Lauferfahrung" questionnaire"""
        self.klin = QuestKlinUntersuch(self.screen)
    
    def init_Sensibilitaet(self):
        """Initialization of "Lauferfahrung" questionnaire"""
        self.sens = QuestSensibilitaet(self.screen)
        
    def validate_subject(self):
        """Validation of the participant according to the inclusion and exclusion criteria for the study and the BMI."""
        self.val_subject = ValidationSubject(self.inc_crit, self.ex_crit, self.parti, self.wizard_page)
        
    def validate_percent(self):
        """Validation of the participant according to the inclusion and exclusion criteria for the study and the BMI."""
        self.val_perc = ValidatePercent(self.lauf)
        
    def init_FeedbackNarrative(self,*args):
        self.questNarrative = QuestNarrative(self.textform.messkonditionen[1],self.screen)
    
    ## --------------------------------------------------------------------------- ##
    ## Button functions ##
    
    def init_wizard_btn(self):
        """
        Initialization of the form wizard buttons 'previous', 'next' and 'save'.
        """
        previous_btn = widgets.Button(description='Previous', tooltip='Previous')
        previous_btn.on_click(self.on_previous_clicked)
        next_btn = widgets.Button(description='Next', tooltip='Next')
        next_btn.on_click(self.on_next_clicked)
        save_btn = widgets.Button(description='Save', tooltip='Save')
        save_btn.on_click(self.on_save_clicked)
        funcal_btn = widgets.Button(description='Functional calibration', tooltip='FunCal')
        funcal_btn.on_click(self.on_funcal_clicked)
        report_btn = widgets.Button(description='Narrative Report', tooltip='Report')
        report_btn.on_click(self.on_report_clicked)
        
        self.wizard_btn = widgets.HBox([previous_btn, next_btn, save_btn, funcal_btn, report_btn])
        
    def show_wizard_btn(self):
        """Show form wizard buttons to the user."""
        
        display(self.wizard_btn)
        
    @output.capture(clear_output=True)
    
    def on_previous_clicked(self, *args):
        """Previous button clicked button callback. Defines what should happen when the previous button got clicked."""
        
        if self.wizard_page > 1:
            self.wizard_page -= 1
            self.show_form()
            self.show_wizard_btn()
        else:
            self.show_form()
            self.show_wizard_btn()
            
    @output.capture(clear_output=True)   

    def on_next_clicked(self, *args):
        """Next button clicked button callback. Defines what should happen when the next button got clicked."""
        
        self.wizard_page  += 1
            
        if self.wizard_page != 4: # self.wizard_page != 2 and 
            self.show_form()
            self.show_wizard_btn()
            
        # Validate if subject fulfills in-/exclusion criteria
        if self.wizard_page == 4:
            self.validate_subject()
            if self.val_subject.validator.value == True:
                display(self.val_subject.validator)
                self.show_form()
                self.show_wizard_btn()
            else:
                display(self.val_subject.validator)
                self.show_save_btn()
                self.show_openbis_login()

    @output.capture(clear_output=True)
            
    def on_funcal_clicked(self, *args):
        """Previous button clicked button callback. Defines what should happen when the previous button got clicked."""
        
        self.wizard_page = 5
        self.show_form()
        self.show_wizard_btn()
        
    @output.capture(clear_output=True)
    
    def on_report_clicked(self, *args):
        """Previous button clicked button callback. Defines what should happen when the previous button got clicked."""
        
        self.wizard_page = 9
        self.show_form()
        self.show_wizard_btn()
        
    @output.capture(clear_output=True)
    
    def init_save_btn(self):
        """
        Initialization of the save button.
        """
        self.save_btn = widgets.Button(description='Save', tooltip='Save')
        self.save_btn.on_click(self.on_save_clicked)
    
    def show_save_btn(self):
        """
        Show the save button to the user.
        """
        display(self.save_btn)
    
    @output.capture(clear_output=False)
            
    ## -------------------------------------------------------------------------------- ##
    ## Data Storage ##
    
    def on_save_clicked(self, *args):
        """Save button clicked button callback. Defines what should happen when the save button got clicked."""
        try:
            # Temporary data storage. Initialized empty. Some required fields needed 
            # for saving. Will be used to render html page (to_html, to_pdf, to_openbis)
            
            date = self.meta.study_metadata.children[0].value
            # Daten zu Messdatum & Probandendaten
            for i in range(0,3):
                if self.parti.erkrankung.children[i].value:
                    if i < 2:
                        erkrankung = self.parti.erkrankung.children[i].description
                    elif i == 2:
                        erkrankung = self.parti.erkrankung.children[i+1].value
                        
            project_info = {'title': self.textform.title[0], 
                            'subtitle': self.textform.title[1], 
                            'date': date.strftime('%d/%m/%Y'),
                            'investigator_name': self.meta.study_metadata.children[2].value,
                            'invest_declaration': self.textform.declaration,
                            'subject_id': self.meta.study_metadata.children[1].value, 
                            'subject_age': self.parti.participant0.value,
                            'subject_height': self.parti.participant1.value,  
                            'subject_weight': self.parti.participant2.value,
                            'subject_shoesize': self.parti.participant3.value,
                            'subject_unfall': self.parti.participant4.value,  
                            'subject_erkrankung': erkrankung}
            
            # Fersen-/Zehengang
            for i in range(0, len(self.textform.participant_info_fersengang)):
                ja_nein_f = getattr(self.parti, "fersengang%s" % (i))
                if ja_nein_f.value == 1:
                    ja_nein_f.wert = True
                elif ja_nein_f.value == 2:
                    ja_nein_f.wert = False
                project_info["fersengang_jn%s" % (i)] = ja_nein_f.wert
            
            # Überprüfung Orthese
            for i in range(0,len(self.orth.orthese.children)):
                project_info["orthese_text%s" % (i)] = self.textform.pruef_orthese[i+1]
                if self.orth.orthese.children[i].value == 1:
                    ja_nein_o = True
                elif self.orth.orthese.children[i].value == 2:
                    ja_nein_o = False
                project_info["orthese_jn%s" % (i)] = ja_nein_o
            
            # Messreihenfolge
            for i, value in enumerate(self.textform.messkonditionen):
                project_info["messungen%s" % (i)] = value
            
            # Fragebogen Klinischer Untersuch
            for i in range(0, len(self.klin.klinunt1.children)):
                project_info["klinunt1text%s" % (i)] = self.klin.klinunt1.children[i].description
                project_info["klinunt1value%s" % (i)] = self.klin.klinunt1.children[i].value
                
            for i in range(0, len(self.klin.klinunt2.children)):
                if self.klin.klinunt2.children[i].description == "Label":
                    project_info["klinunt2text%s" % (i)] = self.klin.klinunt2.children[i].value
                else:
                    project_info["klinunt2text%s" % (i)] = self.klin.klinunt2.children[i].description
                    project_info["klinunt2value%s" % (i)] = self.klin.klinunt2.children[i].value
            
            for i in range(0, len(self.klin.klinunt3.children)):
                project_info["klinunt3text%s" % (i)] = self.klin.klinunt3.children[i].description
                project_info["klinunt3value%s" % (i)] = self.klin.klinunt3.children[i].value
                            
            # Einschlusskriterien
            for i, value in enumerate(self.textform.including_criteria):
                project_info["ethicsinc%s" % (i)] = value
                ja_nein = getattr(self.inc_crit, "widget%s" % (i))
                if ja_nein.value == 1:
                    ja_nein.wert = True
                elif ja_nein.value == 2:
                    ja_nein.wert = False
                project_info["ethicsinc_jn%s" % (i)] = ja_nein.wert
            
            # Ausschlusskriterien
            for i, value in enumerate(self.textform.excluding_criteria):
                project_info["ethicsexc%s" % (i)] = value
                ja_nein = getattr(self.ex_crit, "widget%s" % (i))
                if ja_nein.value == 1:
                    ja_nein.wert = True
                elif ja_nein.value == 2:
                    ja_nein.wert = False
                project_info["ethicsexc_jn%s" % (i)] = ja_nein.wert
                
            project_info["inc_exc_komm"] = self.stud_crit.komm_criteria.value
            
            for i in range(0, len(self.sens.sens2.children)):
                if self.sens.sens2.children[i].description == "Label":
                    project_info["senstext%s" % (i)] = self.sens.sens2.children[i].value
                else:
                    project_info["senstext%s" % (i)] = self.sens.sens2.children[i].description
                    project_info["sensvalue%s" % (i)] = self.sens.sens2.children[i].value
                
            # FunCal
            for i in range(0, len(self.textform.funcal_names)):
                if i == 0:
                    project_info["funcalnames%s" % (i)] = self.textform.funcal_names[i][2:]
                elif i == 2 or i == 6 or i == 9:
                    project_info["funcalnames%s" % (i)] = self.textform.funcal_names[i]
                elif i == 3:
                    project_info["funcalnames%s" % (i)] = self.textform.funcal_names[i][1:-1]
                else:
                    project_info["funcalnames%s" % (i)] = self.textform.funcal_names[i][3:]
                
            project_info["funcal1"] = self.fc.FunCal1.get_object_state()
            project_info["funcal2"] = self.fc.FunCal2.get_object_state()
            project_info["funcal3"] = self.fc.FunCal3.get_object_state()
            project_info["funcal4"] = self.fc.FunCal4.get_object_state()
            project_info["funcal5"] = self.fc.FunCal5.get_object_state()
            
            # Messung ohne Orthese
            for i in range(0, len(self.textform.meas_text)):
                if i == 0 or i == 4 or i == 7:
                    project_info["meastext%s" % (i)] = self.textform.meas_text[i][3:]
                elif i == 3 or i == 5 or i == 9:
                    project_info["meastext%s" % (i)] = self.textform.meas_text[i][1:-1]
                else:
                    project_info["meastext%s" % (i)] = self.textform.meas_text[i]
            
            project_info["ohneStat"] = self.ohneOrth.ohneStat.get_object_state()
            project_info["ohneXW"] = self.ohneOrth.xxx_xw.get_object_state()
            
            project_info["gewicht"] = self.ohneOrth.gewicht.value
            project_info["lichtschranken0"] = self.ohneOrth.Lichtschranken.description
            project_info["lichtschranken1"] = self.ohneOrth.Lichtschranken.value
            project_info["timerange0"] = self.ohneOrth.TimeRange.children[0].description
            project_info["timerange1s1"] = self.ohneOrth.TimeRange.children[0].value
            project_info["timerange2"] = self.ohneOrth.TimeRange.children[1].description
            project_info["timerange3s1"] = self.ohneOrth.TimeRange.children[1].value
            
            # Bewertung des wahrgenommenen Druckes
            for i, value in enumerate(self.ohneOrth.druck):
                if i == 0:
                    project_info["druckname%s" % (i)] = value[1:]
                else:
                    project_info["druckname%s" % (i)] = value
            
            for i in range(0, len(self.ohneOrth.druck_num.children)):
                project_info["drucknum%s" % (i)] = self.ohneOrth.druck_num.children[i].value
            
            # Bewertung der empfundenen Anstrengung
            for i, value in enumerate(self.ohneOrth.anstrengung):
                if i == 0:
                    project_info["anstrengungname%s" % (i)] = value[1:]
                else:
                    project_info["anstrengungname%s" % (i)] = value
                    
            for i in range(0, len(self.ohneOrth.anstrengung_num.children)):
                project_info["anstrengungnum%s" % (i)] = self.ohneOrth.anstrengung_num.children[i].value
            
            # Kommentar
            project_info["komm_ohne"] = self.ohneOrth.komm_ohne.value
            
            # Messung mit aktiver Fussorthese
            project_info["aktivStat"] = self.aktiveOrth.aktivStat.get_object_state()
            project_info["asc_xw"] = self.aktiveOrth.asc_xw.get_object_state()
            project_info["asc_fw"] = self.aktiveOrth.asc_fw.get_object_state()
            
            # Bewertung des wahrgenommenen Druckes
            for i in range(0, len(self.aktiveOrth.druck_num.children)):
                project_info["drucknumaktiv%s" % (i)] = self.aktiveOrth.druck_num.children[i].value
            
            # Bewertung der empfundenen Anstrengung     
            for i in range(0, len(self.aktiveOrth.anstrengung_num.children)):
                project_info["anstrengungnumaktiv%s" % (i)] = self.aktiveOrth.anstrengung_num.children[i].value
            
            # System usability scale
            t = 0
            n = 0
            for i in range(0, len(self.aktiveOrth.questUsabilityAktive.usability.children)):
                if len(self.aktiveOrth.questUsabilityAktive.usability.children[i].description) > 1:
                    project_info["usabilitytext%s" % (t)] = self.aktiveOrth.questUsabilityAktive.usability.children[i].description
                    t += 1
                elif len(self.aktiveOrth.questUsabilityAktive.usability.children[i].description) == 1:
                    if self.aktiveOrth.questUsabilityAktive.usability.children[i].value:
                        project_info["usabilitynum%s" % (n)] = self.aktiveOrth.questUsabilityAktive.usability.children[i].description
                        n += 1
                elif len(self.aktiveOrth.questUsabilityAktive.usability.children[i].value) > 1:
                    project_info["usabilitytext%s" % (t)] = self.aktiveOrth.questUsabilityAktive.usability.children[i].value
                    t += 1
            
            # Kommentar
            project_info["komm_aktive"] = self.aktiveOrth.komm_aktive.value
            
            # Messung mit eigener Orthese
            project_info["eigenStat"] = self.eigOrth.eigenStat.get_object_state()
            project_info["esc_xw"] = self.eigOrth.esc_xw.get_object_state()
            project_info["esc_fw"] = self.eigOrth.esc_fw.get_object_state()
            
            # Bewertung des wahrgenommenen Druckes
            for i in range(0, len(self.eigOrth.druck_num.children)):
                project_info["drucknumeigen%s" % (i)] = self.eigOrth.druck_num.children[i].value
            
            # Bewertung der empfundenen Anstrengung     
            for i in range(0, len(self.eigOrth.anstrengung_num.children)):
                project_info["anstrengungnumeigen%s" % (i)] = self.eigOrth.anstrengung_num.children[i].value
            
            # Kommentar
            project_info["komm_eigene"] = self.eigOrth.komm_eigene.value
            
            # Narrative Report
            for i in range(0, len(self.questNarrative.narrative.children)):
                project_info["narrative%s" % (i)] = self.questNarrative.narrative.children[i].description
                project_info["narrativevalue%s" % (i)] = self.questNarrative.narrative.children[i].value
                            
            # root property as identification i.e case or participant id.
            root = os.path.abspath("C:\\Users\\paui\\Documents\\Anaconda\\Jupyter_Beispiele\\CRF_Dropfoot")
            templates_dir = os.path.join(root, 'templates_Dropfoot')
            env = Environment( loader = FileSystemLoader(templates_dir) )
            template = env.get_template('report_template.html')
            
            filename_report = os.path.join(root, 'output_Dropfoot', 'final_report.html')
            with open(filename_report, 'w') as fh:
                fh.write(template.render(project_info))
#                 fh.append(template.render(participant_info))
    
            filename_data = os.path.join(root, 'output_Dropfoot', 'final_report.json')
            with open(filename_data, 'w') as json_file:
                json.dump(project_info, json_file)
            self.save_btn.button_style='success'
            self.save_btn.description='Successfully saved results!'
            self.save_btn.layout=widgets.Layout(width='200px')
            
        except Exception as e:
            self.save_btn.button_style='danger'
            self.save_btn.description='Saving failed!'
            print(e)
    
    ## --------------------------------------------------------------------------------- ##
    ## Connection to openBIS ##
        
    def init_openbis_login(self):
        """
        Initialization ot the openbis login button.
        """
        # Create login ui
        login_btn = widgets.Button(description='Login to openBIS', tooltip='Login to openBIS')
        login_btn.on_click(self.on_login_clicked)
           
        openbis_instance = widgets.Text(description='openBIS URL:', value='https://openbis-zhaw-gtf.labnotebook.ch/openbis/webapp/eln-lims/?')
        user = widgets.Text(description='Username:')
        pw = widgets.Password(description='Password:')
        self.openbis_login_ui = widgets.VBox([openbis_instance, widgets.HBox([user, pw]), login_btn])
        
    def show_openbis_login(self):
        """Show the openbis login form to the user."""
        
        display(self.openbis_login_ui)
    
    def init_new_experimental_step(self):
        """Initialization of new openbis experiment creation."""
        
        # Create new experiment ui  
        upload_btn = widgets.Button(description='Upload', tooltip='Upload')
        upload_btn.on_click(self.on_upload_clicked)
        
        exp_step_name = widgets.Text(description='New participant name:',  placeholder='PROJECT_SUBJECT', style={'description_width':'initial'})
        exp_name = widgets.Text(description='Experiment:',  placeholder='EXPERIMENT', style={'description_width':'initial'})
        project = widgets.Text(description='Project:',  placeholder='PROJECT')
        space = widgets.Text(description='Space:',  placeholder='SPACE')
        self.new_exp_ui = widgets.VBox([exp_step_name, exp_name, project, space, upload_btn])
    
    def show_new_exp_ui(self):
        """Show the new openbis experiment form to the user."""
        
        display(self.new_exp_ui)

    def upload_to_openbis(self):
        """Show the openbis login form to the user."""
        
        self.show_openbis_login()
    
    @output.capture(clear_output=False)
    
    def on_login_clicked(self, *args):
        """Login button clicked button callback. Defines what should happen when the login button got clicked."""
        
        obj = args[0]
        try:
            self.openbis = Openbis(url=self.openbis_login_ui.children[0].value, verify_certificates=False)
            self.openbis.login(self.openbis_login_ui.children[1].children[0].value, self.openbis_login_ui.children[1].children[1].value)
            self.openbis_login_ui.children[1].value = '' # Security measure.
            obj.button_style='success'
            obj.description='Connected'
            self.show_new_exp_ui()

        except Exception as e:
            self.openbis_login_ui.children[1].value = '' # Security measure.
            obj.button_style='danger'
            obj.description='Login failed. Retry.'

    @output.capture(clear_output=True)
    
    def on_upload_clicked(self, *args):
        """Upload button clicked button callback. Defines what should happen when the upload button got clicked."""
        
        obj = args[0]
        date = self.meta.study_metadata.children[0].value
        try:
            # Create new properties for new subject
            pt = self.openbis.new_property_type(
                code        = 'GEWICHT_KINETIK', 
                label       = 'Gewichtsmessung für Kinetik [kg]', 
                description = 'Gewichtsmessung für Kinetik [kg]',
                dataType    = 'REAL'
            )
            
            # Create new subject in openBIS
            exp_step =  self.openbis.new_sample(
                code = self.new_exp_ui.children[0].value,
                type='EXPERIMENTAL_STEP',
                space=self.new_exp_ui.children[3].value,
                experiment= '/' + self.new_exp_ui.children[3].value + '/' +  self.new_exp_ui.children[2].value + '/' +  self.new_exp_ui.children[1].value,
                props = {"id": str(self.meta.study_metadata.children[1].value), "date": date.strftime('%Y-%m-%d %H:%M'), "investigator": self.meta.study_metadata.children[2].value, "gewicht_kinetik": self.ohneOrth.gewicht.value}
                )
            exp_step.save()
            print(os.getcwd())
            
           # Upload data files to new subject
            ds_new = self.openbis.new_dataset(
                type       = 'ANALYZED_DATA', 
                experiment = '/' + self.new_exp_ui.children[3].value + '/' +  self.new_exp_ui.children[2].value + '/' +  self.new_exp_ui.children[1].value, 
                sample = '/' + self.new_exp_ui.children[3].value + '/' +  self.new_exp_ui.children[2].value + '/' +  self.new_exp_ui.children[1].value + '/' + self.new_exp_ui.children[0].value,
                files      = ['output_Dropfoot\\final_report.html', 'output_Dropfoot\\final_report.json']
            )

            ds_new.save()

            obj.button_style='success'
            obj.description='Upload successfull'

        except Exception as e:
            obj.button_style='danger'
            obj.description='Upload failed. Retry.'
            print(e)
            self.show_new_exp_ui()