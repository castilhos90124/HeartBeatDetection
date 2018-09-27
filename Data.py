

import os

PRECISION = 3

class Data(object):
    
    
    subject_name = ""
    filename= ""
    file = None
    day = ""
    hour= ""
    initial_unix = []
    
    def __init__(self,subject_name):
        #reinicializa variaveis
        self.subject_name = ""
        self.filename= ""
        self.file = None
        self.day = ""
        self.hour= ""
        
        self.subject_name = subject_name
        self.filename = self.clear_string(self.subject_name) + "_HB" + ".csv" 
        
    def write_data_csv(self,motora1_pressed_times,motora2_pressed_times,interoceptiva1_pressed_times,interoceptiva2_pressed_times,feedback_pressed_times,interoceptiva3_pressed_times,interoceptiva4_pressed_times,performance1_escolha,performance2_escolha,performance3_escolha,performance4_escolha):
        try:
            self.file = open("Resultados/" + self.filename, "w")
           
        except:
            os.mkdir("Resultados")
            self.file = open("Resultados/" + self.filename, "w")
        
        self.write_subject_name()
        self.write_time_info()
        
        #etapa1
        
        self.new_line()
        self.file.write("Etapa 1: Estado de Repouso;")
        self.new_line()
        self.file.write("Status: OK;")
        self.new_line()
        
        self.new_line()
        
        #etapa2
        self.file.write("Etapa 2: Primeira Condição Motora-auditiva (audio sampleecg.wav);")
        self.new_line()
        self.file.write("MotorAudio1_onset_time:;")
        self.new_line()
        self.file.write("MotorAudio1_RT:;")
        self.write_data(motora1_pressed_times)
        self.new_line()
        self.file.write("MotorAudio1_Resp_acc:;")
        self.new_line()
        
        self.new_line()
        
        #etapa3
        self.file.write("Etapa 3: Segunda Condição Motora-auditiva (audio tapping_.wav);")
        self.new_line()
        self.file.write("MotorAudio2_onset_time:")
        self.new_line()
        self.file.write("MotorAudio2_RT:;")
        self.write_data(motora2_pressed_times)
        self.new_line()
        self.file.write("MotorAudio2_Resp_acc:;")
        self.new_line()
        
        self.new_line()
        
            
        #etapa4
                
        self.new_line()
        self.file.write("Etapa 4: Primeira Condição Interoceptiva (Pre);")
        self.new_line()
        
        self.file.write("InteroPre1_R-Peak:;")
        self.new_line()
        
        self.file.write("InteroPre1_RT:;")
        self.write_data(interoceptiva1_pressed_times)
        self.new_line()
        
        self.file.write("InteroPre1_Resp_acc:;")
        self.new_line()
        
        #etapa5
        self.new_line()
        self.file.write("Etapa 5: Segunda Condição Interoceptiva (Pre);")
        self.new_line()
        
        self.file.write("InteroPre2_R-Peak:;")
        self.new_line()
        
        self.file.write("InteroPre2_RT:;")
        self.write_data(interoceptiva2_pressed_times)
        self.new_line()
        
        self.file.write("InteroPre2_Resp_acc:;")
        self.new_line()
        
        #etapa6
        self.new_line()
        self.file.write("Etapa 6: Condição de Feedback (Estetoscópio);")
        self.new_line()
        
        self.file.write("Feedback_R-Peak:;")
        self.new_line()
        
        self.file.write("Feedback_RT:;")
        self.write_data(feedback_pressed_times)
        self.new_line()
        
        self.file.write("Feedback_Resp_acc:;")
        self.new_line()
        
        #etapa7
        self.new_line()
        self.file.write("Etapa 7: Terceira Condição Interoceptiva (Pos);")
        self.new_line()
        
        self.file.write("InteroPos1_R-Peak:;")
        self.new_line()
        
        self.file.write("InteroPos1_RT:;")
        self.write_data(interoceptiva3_pressed_times)
        self.new_line()
        
        self.file.write("InteroPos1_Resp_acc:;")
        self.new_line()
        
        #etapa8
        self.new_line()
        self.file.write("Etapa 8: Quarta Condição Interoceptiva (Pos);")
        self.new_line()
        
        self.file.write("InteroPos2_R-Peak:;")
        self.new_line()
        
        self.file.write("InteroPos2_RT:;")
        self.write_data(interoceptiva4_pressed_times)
        self.new_line()
        
        self.file.write("InteroPos2_Resp_acc:;")
        self.new_line()
        
        #pergunta 1
        self.new_line()
        self.file.write("Pergunta 1;")
        self.new_line()
        self.file.write("Q1_Conf_level:;")
        self.file.write(performance1_escolha)
        self.new_line()
        
        #pergunta 2
        self.new_line()
        self.file.write("Pergunta 2;")
        self.new_line()
        self.file.write("Q2_Conf_level:;")
        self.file.write(performance2_escolha)
        self.new_line()
        
        #pergunta 3
        self.new_line()
        self.file.write("Pergunta 3;")
        self.new_line()
        self.file.write("Q3_Conf_level:;")
        self.file.write(performance3_escolha)
        self.new_line()
        
        #pergunta 4
        self.new_line()
        self.file.write("Pergunta 4;")
        self.new_line()
        self.file.write("Q4_Conf_level:;")
        self.file.write(performance4_escolha)
        self.new_line()
        
        
        
        self.file.close()
    
    def write_data(self,data_array):
        i = 0
        while(i < len(data_array)):
            txt_dot_number = str(round(data_array[i],PRECISION))
            txt_coma_number = self.dot_to_coma(txt_dot_number)
            self.file.write(txt_coma_number)
            self.file.write(";")
            i+=1
    
    def s_to_ms(self,data_array):
        i = 0
        while(i < len(data_array)):
            data_array[i] = data_array[i] * 1000
            
            i+=1
    
    def float_to_int(self,data_array):
        i = 0
        while(i < len(data_array)):
            data_array[i] = int(data_array[i])
            
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
        self.file.write("Unix de Inicio:;")
        self.write_data(self.initial_unix)
        self.new_line()
        
    def dot_to_coma(self,string):
        replaced = string.replace(".",",")
        return replaced
        
    
    
        
        
