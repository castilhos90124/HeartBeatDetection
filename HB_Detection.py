import time


ESPACOS1="                             "
ESPACOS2="                       "
ESPACOS3="                          "


#classe mãe de cada uma das etapas, contém os métodos comuns
class HB_Detection(object):
        
    
    start_time= 0.0
    
    #def __init__(self):
         #apenas constroi o objeto, sem alterar nenhuma variavel
         
    def get_responses(self,duration_seconds):
        
        i = 0
        unix_time = 0.0
        
        print("Respostas:\n")
        
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
        
    def print_conclusion(self):
        print("\nEtapa concluida.\n\n")
        
        
    def print_experiment_end(self):
        print("\n\n\n\n\n\n")
        print(ESPACOS1,"Fim do experimento!\n")
        print(ESPACOS2,"Muito obrigada pela sua participação!\n")
        print(ESPACOS3,"Pressione ENTER para sair.") 
        input()
        
    def wait_for_audio_start(self):
        input("Para começar o áudio e para responder a cada batimento aperte ENTER")
        
    def wait_for_hb(self): 
        input("Para começar a responder a cada batimento seu, aperte ENTER")
        
        
    def wait_instructions(self):
        input("Aguarde o pesquisador abrir a porta e lhe dar instruções")
        
    def warn_question(self):
        input("A próxima tela tem uma pergunta para você, quando estiver pronto, aperte ENTER")
        
    def wait_researcher(self):
        input("Aguarde o pesquisador abrir a porta e retirar o fone")
        
    def wait_fone(self):
        input("Aguarde o pesquisador abrir a porta e ajudar a colocar o fone de ouvido")
        
    def wait_estetoscopio(self):
        input("Aguarde o pesquisador abrir a porta e retirar o estetoscópio")
        
    def wait_put_estetoscopio(self):
        input("Aguarde o pesquisador abrir a porta e colocar o estetoscópio")
        
    
    
