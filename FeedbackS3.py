from HB_Detection import HB_Detection


class FeedbackS3(HB_Detection):
    
    def __init__(self):
         super().__init__()     #chama o construtor da classe mãe (HB_Detection)
    
    def print_instructions(self):
        print("Etapa 3: Feedback Condition")
        print("Nao se esqueca de posicionar o estetoscopio corretamente")
        input("Pressione Enter se voce compreendeu as instrucoes e esta pronto(a) para iniciar a Etapa 3")

    