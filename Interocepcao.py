from HB_Detection import HB_Detection

import sys

ESPACOS1="                    "
ESPACOS2="                               "
ESPACOS3=" "
ESPACOS4="       "
ESPACOS5="    "
ESPACOS6="                                 "
ESPACOS7="    "
ESPACOS8="    "
ESPACOS9="                 "
ESPACOS10="  "

class Interocepcao(HB_Detection):
    
    hb_pressed_times = []
    hb_play_times = []
    
    def __init__(self):
         #super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
         self.hb_pressed_times = []
         self.hb_play_times = []
    
    def print_instructions(self,num_etapa):
        
        print("")
        print(ESPACOS1,"Você vai realizar a Etapa "+ num_etapa + " agora\n")
        print(ESPACOS2,"Instruções:\n")
        print(ESPACOS3,"Nesta parte do teste você vai sentir os batimentos do seu próprio coração") 
        print(ESPACOS4,"apertando a tecla ENTER para cada batimento que você sentir.\n")
        print(ESPACOS5,"Você não deve guiar as respostas sentindo seu pulso em seus punhos ou")
        print(ESPACOS6,"pescoço.\n")
        print(ESPACOS7,"Se você não conseguir sentir a sensação dos seus batimentos, você deve")
        print(ESPACOS8,"apelar para a sua intuição para tentar responder quando você achar que")
        print(ESPACOS9,"houve batimento do seu coração.\n")
        print(ESPACOS10,"Quando tiver lido a instrução e estiver pronto para seguir, aperte ENTER")
        input()
        
    
    def print_title(self,num_etapa):
        print("Etapa "+num_etapa)
        print("Etapa iniciada")
        