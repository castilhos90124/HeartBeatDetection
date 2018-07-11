
#classe mãe de cada uma das etapas, contém os métodos comuns
class HB_Detection(object):
    
    KB_KEY = 10
    
    hb_pressed_times = []
    
    def write_detection(self,elapsed_time):
        
        hb_pressed_times.append(elapsed_time)
                
    
    
