from HB_Detection import HB_Detection

import time

DELAY_SECONDS = 1

class CondicaoMotoraS1(HB_Detection):
    
    
    
    
    def __init__(self):
         super().__init__()     #chama o construtor da classe mãe (HB_Detection)
        
    
    def print_instructions(self):
        print("Instrucoes Etapa 1:")
        print("bla bla bla")
        input("pressione Enter para iniciar a Etapa 1")
        time.sleep(DELAY_SECONDS)
    
    def play_sound(self):
        self.start_time = time.time()
        print("inicio do som tocando")