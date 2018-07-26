from CondicaoMotoraS1 import CondicaoMotoraS1
from PreInteroceptivaS2 import PreInteroceptivaS2
from FeedbackS3 import FeedbackS3
from PosInteroceptivaS4 import PosInteroceptivaS4
from Data import Data

import os
#import time

DURATION_STEP1 = 131
DURATION_STEP2 = 120
DURATION_STEP3 = 120
DURATION_STEP4 = 120

   
def main():
    
    run_again = True
    choice = "s"
    
    while (run_again):
    
        
        name = input("Nome do participante:")
        data = Data(name)
        
        #print(str(1532368217.1612382))
        #print(round(1532368217.1612382, 3))
        
        #instanciando os objetos das etapas
        step1 = CondicaoMotoraS1()
        step2 = PreInteroceptivaS2()
        step3 = FeedbackS3()
        step4 = PosInteroceptivaS4()
        
        
        
       
        data.day=input("Dia:")
        data.hour=input("Horario:")
           
        
        #inicio da etapa 1
        step1.print_instructions()
        step1.set_current_start_time()
        step1.play_sound()
      
        step1.get_responses(DURATION_STEP1)
     
              
        
        os.system("PAUSE")
        os.system("CLS")
       
        #inicio da etapa 2
        step2.print_instructions_general()
        step2.print_instructions()
        step2.set_current_start_time()
        step2.get_responses(DURATION_STEP2)
       # print(step2.hb_pressed_times)
       
        os.system("pause")
        os.system("CLS")
       
        #inicio da etapa 3
        step3.print_instructions()
        step3.set_current_start_time()
        step3.get_responses(DURATION_STEP3)
        #print(step3.hb_pressed_times)
       
        os.system("pause")
        os.system("CLS")
       
        #inicio da etapa 4
        step4.print_instructions()
        step4.set_current_start_time()
        step4.get_responses(DURATION_STEP4)
       # print(step4.hb_pressed_times)
       
        
        data.write_data_csv(step1.hb_pressed_times,step1.hb_play_times,step2.hb_pressed_times,step3.hb_pressed_times,step4.hb_pressed_times)
         
        os.system("CLS")
        
    
        choice=input("Dados coletados com sucesso. Deseja realizar outra coleta? (s/n):")
        
        if choice == "s":
            run_again=True
        else:
            run_again=False
        
   
   
       
     


main()

    