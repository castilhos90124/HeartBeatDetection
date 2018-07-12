import os

class Data(object):
    
    subject_name = ""
    filename= ""
    file = 0
    
    def __init__(self,subject_name):
        self.subject_name = subject_name
        self.filename = self.clear_string(self.subject_name) +"_HB_pressed_times" + ".csv" 
        
    def write_data(self):
        try:
            self.file = open("Resultados/" + self.filename, "w")
           
        except:
            os.mkdir("Resultados")
            self.file = open("Resultados/" + self.filename, "w")
            
    def clear_string(self,string):
        clean = string.replace(" ","")
        clean = clean.replace("\t","")
        clean = clean.replace("\n","")

        return clean
