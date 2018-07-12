import time


#classe mãe de cada uma das etapas, contém os métodos comuns
class HB_Detection(object):
        
    hb_pressed_times = []
    start_time= 0.0
    
    #def __init__(self):
         #apenas constroi o objeto, sem alterar nenhuma variavel
         
    def get_responses(self,duration_seconds):
        i = 1
        print("pressione Enter quando ouvir um batimento cardíaco")
        
        while self.timeout(duration_seconds) == False:
            input(i)
            self.write_detection(time.time())
            i+=1
        
        
        
    def write_detection(self,unix_time):
        
        self.hb_pressed_times.append(unix_time)
                
    
    def timeout(self,duration_seconds):
        
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time < duration_seconds :
            return False
        
        return True
        
    
