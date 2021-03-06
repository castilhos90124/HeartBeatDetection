from RestingState import RestingState
from CondicaoMotora import CondicaoMotora
from Performance import Performance

from Interocepcao import Interocepcao
from Feedback import Feedback

from Data import Data

import os
import time

DURATION_motora1 = 131
DURATION_motora2 = 144
DURATION_interocepcao1 = 120
DURATION_feedback = 120
DURATION_interocepcao2 = 120

   
def main():
    
   
    
    os.system("CLS")
    
    name = input("Participante:")
    data = Data(name)
    
    #print(str(1532368217.1612382))
    #print(round(1532368217.1612382, 3))
    
    #instanciando os objetos das etapas
    rest_state = RestingState()
    motora1 = CondicaoMotora()
    motora2= CondicaoMotora()
    performance1 = Performance()
    performance2 = Performance()
    performance3 = Performance()
    performance4 = Performance()
    interocepcao1 = Interocepcao()
    interocepcao2 = Interocepcao()
    interocepcao3 = Interocepcao()
    interocepcao4 = Interocepcao()
    feedback = Feedback()
    
    
    
    
   
    data.day=input("Dia:")
    data.hour=input("Hora:")
    data.initial_unix.append(time.time())
    
    os.system("CLS")
    
    rest_state.print_instructions()
    os.system("CLS")
    rest_state.print_title()
    
    rest_state.rest()
    rest_state.print_conclusion()
    rest_state.wait_fone()
    
    os.system("CLS")
    
    #inicio da etapa 2
    motora1.print_instructions("2")
    os.system("CLS")
    motora1.print_title("2")
    motora1.wait_for_audio_start()
    motora1.set_current_start_time()
    motora1.play_sample()
    motora1.get_responses(DURATION_motora1)
    os.system("CLS")  
                
    motora1.print_conclusion()
    motora1.wait_instructions()
    os.system("CLS")
    
    
    #inicio da etapa 3
    motora2.print_instructions("3")
    os.system("CLS")
    motora2.print_title("3")
    motora2.wait_for_audio_start()
    motora2.set_current_start_time()
    motora2.play_tapping()
    motora2.get_responses(DURATION_motora2)
    os.system("CLS")
    
    motora2.print_conclusion()                  
    motora2.warn_question()
    os.system("CLS")
    
    #inicio da pergunta de performance 1
    performance1.print_instructions()
    os.system("CLS")
    performance1.wait_researcher()
    
    
    os.system("CLS")
   
    #inicio da etapa 4
            
    interocepcao1.print_instructions("4")
    os.system("CLS")
    interocepcao1.print_title("4")
    interocepcao1.wait_for_hb()
    interocepcao1.set_current_start_time()
    interocepcao1.get_responses(DURATION_interocepcao1)
    os.system("CLS")
     
    interocepcao1.print_conclusion()
    interocepcao1.wait_instructions()
    os.system("CLS")
   
     #inicio da etapa 5
    interocepcao2.print_instructions("5")
    os.system("CLS")
    interocepcao2.print_title("5")
    interocepcao2.wait_for_hb()
    interocepcao2.set_current_start_time()
    
    interocepcao2.get_responses(DURATION_interocepcao2)
   # print(interocepcao2.hb_pressed_times)
    os.system("CLS")
   
    interocepcao2.print_conclusion()
    interocepcao2.warn_question()
    os.system("CLS")
    
    #inicio da pergunta de performance 2
    performance2.print_instructions()
    os.system("CLS")
    performance2.wait_put_estetoscopio()
    
    os.system("CLS")
    
    #inicio da etapa 6
    feedback.print_instructions()
    os.system("CLS")
    feedback.print_title()
    feedback.wait_for_hb()
    feedback.set_current_start_time()
    feedback.get_responses(DURATION_feedback)
    os.system("CLS")
           
    feedback.print_conclusion()
    feedback.warn_question()
    os.system("CLS")
   
     #inicio da pergunta de performance 3
    performance3.print_instructions()
   
    os.system("CLS")
    performance3.wait_estetoscopio()
    os.system("CLS")
    
    #inicio da etapa 7
    interocepcao3.print_instructions("7")
    os.system("CLS")
    interocepcao3.print_title("7")
    interocepcao3.wait_for_hb()
    interocepcao3.set_current_start_time()
    interocepcao3.get_responses(DURATION_interocepcao1)
    os.system("CLS")
     
    interocepcao3.print_conclusion()
    interocepcao3.wait_instructions()
    os.system("CLS")
    
    #inicio da etapa 8
    interocepcao4.print_instructions("8")
    os.system("CLS")
    interocepcao4.print_title("8")
    interocepcao4.wait_for_hb()
    interocepcao4.set_current_start_time()
    interocepcao4.get_responses(DURATION_interocepcao1)
    os.system("CLS")
     
    interocepcao4.print_conclusion()
    interocepcao4.warn_question()
    os.system("CLS")
    
    #inicio da pergunta de performance 4
    performance4.print_instructions()
   
    os.system("CLS")
    
    data.write_data_csv(motora1.hb_pressed_times,motora2.hb_pressed_times,interocepcao1.hb_pressed_times,interocepcao2.hb_pressed_times,feedback.hb_pressed_times,interocepcao3.hb_pressed_times,interocepcao4.hb_pressed_times,performance1.escolha,performance2.escolha,performance3.escolha,performance4.escolha)
     
    os.system("CLS")
        
    interocepcao2.print_experiment_end()
          
  
       
     


main()

    