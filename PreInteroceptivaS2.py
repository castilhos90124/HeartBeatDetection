from HB_Detection import HB_Detection

import sys

ESPACOS1=""
ESPACOS2=""
ESPACOS3=""
ESPACOS4=""
ESPACOS5=""
ESPACOS6=""
ESPACOS7=""
ESPACOS8=""
ESPACOS9=""
ESPACOS10=""

class PreInteroceptivaS2(HB_Detection):
    
    hb_pressed_times = []
    hb_play_times = []
    
    def __init__(self):
         #super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
         self.hb_pressed_times = []
         self.hb_play_times = []
    
    def print_instructions(self):
        
        print(ESPACOS1,"Você vai realizar a Etapa 2 agora\n\n")
        print(ESPACOS2,"Instruções:\n\n")
        print(ESPACOS3,"Nesta parte do teste  você vai escutar os batimentos do seu próprio coração\n") 
        print(ESPACOS4,"apertando a tecla ENTER para cada batimento que você sentir.\n\n")
        print(ESPACOS5,"Você não deve guiar as respostas sentindo seu pulso em seus punhos ou\n")
        print(ESPACOS6,"pescoço.\n\n")
        print(ESPACOS7,"Se você não conseguir sentir a sensação dos seus batimentos, você deve\n")
        print(ESPACOS8,"apelar para a sua intuição para tentar responder quando você achar que\n")
        print(ESPACOS9,"houve batimento do seu coração.\n\n")
        print(ESPACOS10,"Para começar pressione ENTER.")
        input()
        
    
    def print_title(self):
        print("Etapa 2")
        