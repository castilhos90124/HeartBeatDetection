from HB_Detection import HB_Detection

import time
import winsound

DELAY_SECONDS = 1
SOUND_NAME = "teste"


class CondicaoMotoraS1(HB_Detection):
    
    hb_pressed_times = []
    hb_play_times = []
    
    def __init__(self):
         #super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
         self.hb_pressed_times = []
         self.hb_play_times = []
         
        
    
    def print_instructions(self):
        print("Instrucoes Etapa 1: Motor Control Condition\n")
        print("Nesta parte do teste, você vai escutar os batimentos de uma gravação de batimentos cardíacos de uma outra pessoa.")
        print("Você deve seguir cada batimento apertando a tecla Enter no teclado.") 
        print("Não tente antecipar suas respostas adivinhando o ritmo dos batimentos gravados, ao invés disso aperte a tecla Enter o mais rápido que puder assim que você escutar cada batimento.\n")
        input("Pressione Enter se voce compreendeu as instrucoes e esta pronto para iniciar a Etapa 1")
        time.sleep(DELAY_SECONDS)
    
    def play_sound(self):
        winsound.PlaySound(SOUND_NAME, winsound.SND_ASYNC)
        