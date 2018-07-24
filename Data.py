

import os

class Data(object):
    
    subject_name = ""
    filename= ""
    file = None
    day = ""
    hour= ""
    
    def __init__(self,subject_name):
        self.subject_name = subject_name
        self.filename = self.clear_string(self.subject_name) +"_HB_pressed_times" + ".csv" 
        
    def write_data_csv(self,step1_pressed_times):#,step2_pressed_times,step3_pressed_times,step4_pressed_times):
        try:
            self.file = open("Resultados/" + self.filename, "w")
           
        except:
            os.mkdir("Resultados")
            self.file = open("Resultados/" + self.filename, "w")
        
        self.write_subject_name()
        self.write_time_info()
        
        #etapa1
        self.new_line()
        self.file.write("Etapa 1: Condição Motora;")
        self.new_line()
        
        self.file.write("Resposta:;")
        self.write_data(step1_pressed_times)
        self.new_line()
        
        self.file.write("TR:;")
        self.new_line()
        
        self.file.write("Acerto:;")
        self.new_line()
        
        #etapa2
        self.new_line()
        self.file.write("Etapa 2: Condição Interoceptiva (Pré);")
        self.new_line()
        
        #etapa3
        self.new_line()
        self.file.write("Etapa 3: Condição de Feedback (Estetoscópio);")
        self.new_line()
        
        #etapa4
        self.new_line()
        self.file.write("Etapa 4: Condição Interoceptiva (Pós);")
        self.new_line()
    
    def write_data(self,hb_pressed_times):
        i = 0
        while(i < len(hb_pressed_times)):
            txt_dot_number = str(round(hb_pressed_times[i],3))
            txt_coma_number = self.dot_to_coma(txt_dot_number)
            self.file.write(txt_coma_number)
            self.file.write(";")
            i+=1
        
    def clear_string(self,string):
        clean = string.replace(" ","")
        clean = clean.replace("\t","")
        clean = clean.replace("\n","")

        return clean
    
    def new_line(self):
        self.file.write("\n")
    
    def write_subject_name(self):
        self.file.write("Participante:;" + self.subject_name + ";")
        self.new_line()
        
    def write_time_info(self):
        self.file.write("Dia:;" + self.day + ";")
        self.new_line()
        self.file.write("Hora:;" + self.hour + ";")
        self.new_line()
        
    def dot_to_coma(self,string):
        replaced = string.replace(".",",")
        return replaced
        
    
    
        
        
