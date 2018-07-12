from CondicaoMotoraS1 import CondicaoMotoraS1
from PreInteroceptivaS2 import PreInteroceptivaS2
from FeedbackS3 import FeedbackS3
from PosInteroceptivaS4 import PosInteroceptivaS4
from Data import Data

import time
import os

   
def main():
   
   print("Insira o nome do ""paciente"":")
   name = input()
   
   data = Data(name)
   
   print(data.subject_name)
       
       
       
     


main()

    