from CondicaoMotoraS1 import CondicaoMotoraS1
from PreInteroceptivaS2 import PreInteroceptivaS2
from FeedbackS3 import FeedbackS3
from PosInteroceptivaS4 import PosInteroceptivaS4
from Data import Data

import os

DURATION_STEP1 = 15
DURATION_STEP2 = 2
DURATION_STEP3 = 2
DURATION_STEP4 = 2

   
def main():
   
   
   name = input("Insira o nome do paciente:")
   print("")
   
   data = Data(name)
  
    #instanciando os objetos das etapas
   step1 = CondicaoMotoraS1()
   step2 = PreInteroceptivaS2()
   step3 = FeedbackS3()
   step4 = PosInteroceptivaS4()
   
   #inicio da etapa 1
   step1.print_instructions()
   step1.set_current_start_time()
   step1.play_sound()
   step1.get_responses(DURATION_STEP1)
     
   print(step1.hb_pressed_times)
   
     
  # os.system("pause")
   #os.system("CLS")
   
   #inicio da etapa 2
   step2.print_instructions_general()
   step2.print_instructions()
   step2.set_current_start_time()
   step2.get_responses(DURATION_STEP2)
   print(step2.hb_pressed_times)
   
  # os.system("pause")
   #os.system("CLS")
   
   #inicio da etapa 3
   step3.print_instructions()
   step3.set_current_start_time()
   step3.get_responses(DURATION_STEP3)
   print(step3.hb_pressed_times)
   
   #os.system("pause")
   #os.system("CLS")
   
    #inicio da etapa 4
   step4.print_instructions()
   step4.set_current_start_time()
   step4.get_responses(DURATION_STEP4)
   print(step4.hb_pressed_times)
   
   
   data.write_data()
   
   
   
       
     


main()

    