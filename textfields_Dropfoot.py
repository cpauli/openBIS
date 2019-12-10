# /********************************************************************************
# * Copyright © 2019, Carole A. Pauli
# *
# * Contributors:
# *     Carole A. Pauli - initial API and implementation
# *******************************************************************************/

import ipywidgets as widgets
import random

__author__ = 'Carole A. Pauli'

class Textfields(object):
    """
    Constructs a Textfields object.
    """
     
    def __init__(self):
        """
        Initialization of text blocks for Case report form
        """
        
        ## Project information
        self.title = ["Case Report Form",""]
        self.declaration = "The collected data are correct and complete. They have been collected according to the current study protocol. The cantonal ethics commission denied jurisdiction for this project. The participant gave informed consent prior to inclusion in this study."
        
        ## Participant information and inclusion criteria
        self.incex_title = ["# Ein- /Ausschlusskriterien", 
                            "## Einschlusskritierien", 
                            "*falls eine Antwort **Nein** ist, wird der Proband ausgeschlossen*", 
                            "## Ausschlusskritierien", 
                            "*falls eine Antwort **Ja** ist, wird der Proband ausgeschlossen*"];
        # Inclusion criteria
        self.including_criteria = ["Wurde der «Informed consent» unterschrieben?", 
                                   "Alter zwischen 18 und 85 Jahren?", 
                                   "Einseitiger oder beidseitiger Fallfuss welcher auf mindestens einer Seite bereits mit einer Fussheberorthese versorgt wurde?", 
                                   "Keine bis milde Spastik im OSG (Modified Ashworth Scale <=2)", 
                                   "Passive ROM OSG mindestens DE/PF 0/0/25",
                                   "FAC score 3-5?"];
        # Exclusion criteria
        self.excluding_criteria = ["Akute muskuloskelettale Erkrankung?", 
                                   "Akute kardiopulmonale Erkrankung?", 
                                   "Akute neurologische Erkrankung?",
                                   "Amputationen an der UE?",
                                   "Akute Beschwerden jeglicher Art welche das Tragen der Orthese oder die Mobilität beeinträchtigen?",
                                   "Schmerzen >3 auf einer Numeric Pain Rating Scale (NPRS)?",
                                   "Punktezahl Mini Mental Status <24"];
        
        # Required participant information
#         self.participant_info_name = {"Alter:": [18,65],
#                                       "Grösse [m]:": [1,2.4], 
#                                       "Gewicht [kg]:": [40,120]};
        self.participant_info_name = ["Alter:",
                                      "Grösse (ohne Schuhe) [m]:", 
                                      "Gewicht [kg]", 
                                      "Schuhgrösse",
                                      "Unfall Datum (für Schlaganfallpatienten):"]
    
        self.participant_info_erkrankung = ["Hirnblutung", 
                                            "Schlaganfall", 
                                            "andere Erkrankung:"]
    
        self.participant_info_fersengang = ["Fersengang rechts", "Fersengang links",
                                            "Zehengang rechts", "Zehengang links"]
        
        ## Kinematics
        # Functional calibration
        self.funcal_names = ["# Funktionelle Kalibrierung", 
                             "## Referenzversuch", 
                             "Stand auf ebener Fläche", 
                             "*Versuch Labeln um sicher zu gehen, dass alle Marker vorhanden sind*",
                             "## Knie Flexion / Extension links (Vorzeigen)", 
                             "## Knie Flexion / Extension rechts (Vorzeigen)",
                             "Stellen Sie sich aufrecht hin. Heben Sie das linke / rechte Bein vom Boden und ziehen Sie den Unterschenkel nach hinten oben zum Oberschenkel hoch. Sie dürfen sich am Stock festhalten, um das Gleichgewicht besser halten zu können.",
                             "## Hüft Zirkumduktion links (Vorzeigen)", 
                             "## Hüft Zirkumduktion rechts (Vorzeigen)",
                             "Stellen Sie sich aufrecht hin. Heben Sie das linke / rechte Bein vom Boden und kreisen Sie das gestreckte Bein um die Hüfte. Sie dürfen sich am Stock festhalten, um das Gleichgewicht besser halten zu können."]
        
        # Measurement text
        self.meas_text = ["## Referenzversuch", 
                          "Stand auf ebener Fläche",
                          "Gewichtsmessung für Kinetik [kg]",
                          "*Wichtig das Patienten/Patientinnen sich hier kurz nicht festhalten! Reset offset KMPs; Patienten auf 1 KMP stehen lassen*",
                          "## Normales Gehen mit selbstgewählter Geschwindigkeit (min. 3 gültige Versuche pro Seite)",
                          "*Für einen gültigen Versuch muss der Proband mit der betroffenen Seite sauber auf der Kraftmessplatte gelandet sein und von der Geschwindigkeit im 10 Prozent Rahmen sein.*",
                          "Gehen sie mit ihrer gewohnten Geschwindigkeit. Stellen Sie sich vor, Sie gehen zur Bushaltestelle oder zum Laden. Sie sind nicht im Stress, haben aber ein Ziel.",
                          "## Normales Gehen selbe Geschwindigkeit wie ohne Orthese (min. 3 gültige Versuche pro Seite)", 
                          "Gehen sie mit derselben Geschwindigkeit wie vorher ohne Orthese. Wenn Sie zu schnell oder zu langsam gehen, werden wir Sie darauf aufmerksam machen und Sie bitten die Geschwindigkeit anzupassen.", 
                          "*Wenn Probanden körperlich genug fit sind, sollen Sie nach den 3 gültigen Versuchen gerne noch zwei Versuche mit selbstgewählter Geschwindigkeit laufen (muss nicht mehr im 10 Prozent Rahmen liegen). So kann ein Einfluss auf die Gehgeschwindigkeit erkannt werden.*"]
        
        self.meas_step_count = {"links": 3,
                                "rechts": 3}
        
        ## Project specific fields
        # Fragen Überprüfung Orthese
        self.pruef_orthese = ["Überprüfungen an der Orthese",
                              "Haben die Strings Abriebspuren?",
                              "Ist die richtige Seite für den Patienten eingestellt (li/re)?",
                              "Ist die richtige Sohlengrösse gewählt?",
                              "Ist die Zugplatte am Schuh richtig montiert?",
                              "*Wenn eine Frage mit 'Stern' beantwortet wird, muss dies vor der Messung angepasst werden!*"]
        
        # Namen Messkonditionen
        self.messkonditionen = ["Messung ohne Orthese",
                                "Messung mit aktiver Fussorthese",
                                "Messung mit eigener Orthese"]
        
        
    def get(self):
        """
        Returns the object state as dict.
        """
        return self.__dict__