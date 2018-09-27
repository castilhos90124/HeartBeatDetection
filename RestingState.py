from HB_Detection import HB_Detection

import time


REST_TIME_SECONDS = 420 #7min

ESPACOS1="                               "
ESPACOS2="        "
ESPACOS3="        "
ESPACOS4="        "
ESPACOS5="          "
ESPACOS6=""
ESPACOS7=" "
ESPACOS8="                          "
ESPACOS9="                       "


class RestingState(HB_Detection):
    
    
    def __init__(self):
         super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
        
        
    
    def print_instructions(self):
                        
        print("\n\n")
        print(ESPACOS1,"Instruções:")
        print(ESPACOS2,"Este teste possui 8 etapas. Agora você vai realizar a Etapa 1.\n")
        print(ESPACOS3,"Nesta parte do teste você vai permanecer em descanso sem se mexer ") 
        print(ESPACOS4,"muito e tentará não pensar em nada em especial por alguns minutos.\n")
        print(ESPACOS5,"Você será avisado quando esta etapa for concluída.\n")
        
        print(ESPACOS9,"Para começar pressione ENTER.")
        input()
        #time.sleep(DELAY_SECONDS)
    
    def rest(self):
        time.sleep(REST_TIME_SECONDS)
        
    def print_title(self):
        print("Etapa 1")