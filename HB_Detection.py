

#classe mãe de cada uma das etapas, contém os métodos comuns
class HB_Detection(object):
        
    hb_pressed_times = []
    
    #def __init__(self):
         #apenas constroi o objeto, sem alterar nenhuma variavel
         
        
    def write_detection(self,elapsed_time):
        
        self.hb_pressed_times.append(elapsed_time)
                
    
    
