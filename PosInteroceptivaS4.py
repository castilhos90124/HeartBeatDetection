from HB_Detection import HB_Detection


class PosInteroceptivaS4(HB_Detection):
    
    hb_pressed_times = []
    hb_play_times = []
    
    def __init__(self):
         #super().__init__()     #chama o construtor da classe mãe (HB_Detection)
         
         #reinicializa as variaveis
         self.hb_pressed_times = []
         self.hb_play_times = []
    
    def print_instructions(self):
        print("Etapa 4: Second Interoceptive Condition (Intero-Post)")
        input("Pressione Enter se voce compreendeu as instrucoes e esta pronto(a) para iniciar a Etapa 4")
    