from CondicaoMotoraS1 import CondicaoMotoraS1
from PreInteroceptivaS2 import PreInteroceptivaS2
from FeedbackS3 import FeedbackS3
from PosInteroceptivaS4 import PosInteroceptivaS4
from Data import Data

import os
#import time

DURATION_STEP1 = 5     #131
DURATION_STEP2 = 5     #120
DURATION_STEP3 = 5     #120
DURATION_STEP4 = 5     #120

   
def main():
    
    run_again = True
    choice = "s"
    
    while (run_again):
    
        os.system("CLS")
        
        name = input("Participante:")
        data = Data(name)
        
        #print(str(1532368217.1612382))
        #print(round(1532368217.1612382, 3))
        
        #instanciando os objetos das etapas
        step1 = CondicaoMotoraS1()
        step2 = PreInteroceptivaS2()
        step3 = FeedbackS3()
        step4 = PosInteroceptivaS4()
        
        
        
       
        data.day=input("Dia:")
        data.hour=input("Hora:")
           
        os.system("CLS")
        
        #inicio da etapa 1
        step1.print_instructions()
        os.system("CLS")
        step1.print_title()
        step1.set_current_start_time()
        step1.play_sound()
        step1.get_responses(DURATION_STEP1)
                          
        step1.print_conclusion()
        os.system("CLS")
       
        #inicio da etapa 2
                
        step2.print_instructions()
        os.system("CLS")
        step2.print_title()
        step2.set_current_start_time()
        step2.get_responses(DURATION_STEP2)
            
        step2.print_conclusion()
        os.system("CLS")
       
        #inicio da etapa 3
        step3.print_instructions()
        os.system("CLS")
        step3.print_title()
        step3.set_current_start_time()
        step3.get_responses(DURATION_STEP3)
               
        step3.print_conclusion()
        os.system("CLS")
       
        #inicio da etapa 4
        step4.print_instructions()
        os.system("CLS")
        step4.print_title()
        step4.set_current_start_time()
        
        step4.get_responses(DURATION_STEP4)
       # print(step4.hb_pressed_times)
       
        step4.print_conclusion()
        os.system("CLS")
        
        data.write_data_csv(step1.hb_pressed_times,step1.hb_play_times,step2.hb_pressed_times,step3.hb_pressed_times,step4.hb_pressed_times)
         
        os.system("CLS")
        
    
        choice=input("Dados coletados com sucesso. Deseja realizar outra coleta? (s/n):")
        
        if choice == "s":
            run_again=True
        else:
            run_again=False
        
   
  
       
     


main()

    