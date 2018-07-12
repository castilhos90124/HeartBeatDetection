from CondicaoMotoraS1 import CondicaoMotoraS1
from PreInteroceptivaS2 import PreInteroceptivaS2
from FeedbackS3 import FeedbackS3
from PosInteroceptivaS4 import PosInteroceptivaS4
from Data import Data

import time
import os



   
def main():
   
   
   name = input("Insira o nome do paciente:")
   print("")
   
   data = Data(name)
   
   step1 = CondicaoMotoraS1()
   step2 = PreInteroceptivaS2()
   step3 = FeedbackS3()
   step4 = PosInteroceptivaS4()
   
   #inicio da etapa 1
   step1.print_instructions()
   step1.play_sound()
   step1.get_responses(10)
   
   print(step1.hb_pressed_times)
   
   os.system("cls")
   
   
   
  
   
   
   
       
       
       
     


main()

    