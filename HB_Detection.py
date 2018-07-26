import time


#classe mãe de cada uma das etapas, contém os métodos comuns
class HB_Detection(object):
        
    
    start_time= 0.0
    
    #def __init__(self):
         #apenas constroi o objeto, sem alterar nenhuma variavel
         
    def get_responses(self,duration_seconds):
        
        i = 0
        unix_time = 0.0
        
        print("Pressione Enter quando ouvir um batimento cardíaco\n")
        
        while self.timeout(duration_seconds) == False:
            input(i)
            unix_time = time.time()
            play_time = unix_time - self.start_time
            
            
            if self.timeout(duration_seconds) == False:
                self.write_detection(unix_time,play_time)
                
                i+=1
        
        
        
    def write_detection(self,unix_time,play_time):
        
        self.hb_pressed_times.append(unix_time)
        self.hb_play_times.append(play_time)
                
    
    def timeout(self,duration_seconds):
        
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time < duration_seconds :
            return False
        
        return True
    
    def print_instructions_general(self):
        print("Instruções para as três condições seguintes [interoceptive condition (intero-pre), feedback condition and second interoceptive condition (intero-post)]:")
        print("Agora você deve seguir os batimentos do seu próprio coração apertando a tecla Enter para cada batimento que você sentir.") 
        print("Você não deve guiar suas respostas sentindo seu pulso em seus punhos ou pescoço.")
        print("Se você não conseguir sentir a sensação dos seus batimentos, você deve apelar para a sua intuição para tentar responder quando você achar que houve batimento do seu coração.")
        
    def set_current_start_time(self):
        self.start_time = time.time()
