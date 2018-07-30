from HB_Detection import HB_Detection

import time
import winsound

DELAY_SECONDS = 1
SOUND_NAME = "sampleecg"

ESPACOS1=""
ESPACOS2=""
ESPACOS3=""
ESPACOS4=""
ESPACOS5=""
ESPACOS6=""
ESPACOS7=""
ESPACOS8=""
ESPACOS9=""


class CondicaoMotoraS1(HB_Detection):
    
    hb_pressed_times = []
    hb_play_times = []
    
    def __init__(self):
         #super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
         self.hb_pressed_times = []
         self.hb_play_times = []
         
        
    
    def print_instructions(self):
                        
        print(ESPACOS1,"Instruções\n")
        print(ESPACOS2,"Este teste possui 4 etapas. Agora você vai realizar a Etapa 1.\n\n")
        print(ESPACOS3,"Nesta parte do teste  você vai escutar os batimentos de uma gravação de\n") 
        print(ESPACOS4,"batimentos cardíacos de uma outra pessoa.\n\n")
        print(ESPACOS5,"Você deve seguir cada batimento apertando a tecla ENTER no teclado.\n\n")
        print(ESPACOS6,"Não tente antecipar suas respostas adivinhando o ritmo dos batimentos gravados,\n")
        print(ESPACOS7,"ao invés disso, aperte a tecla ENTER o mais rápido que puder assim que você\n")
        print(ESPACOS8,"escutar o batimento.\n\n")
        print(ESPACOS9,"Para começar pressione ENTER.")
        input()
        #time.sleep(DELAY_SECONDS)
    
    def play_sound(self):
        winsound.PlaySound(SOUND_NAME, winsound.SND_ASYNC)
        
    def print_title(self):
        print("Etapa 1")