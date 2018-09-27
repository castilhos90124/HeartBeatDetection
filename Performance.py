

import os

ESPACOS1="                               "
ESPACOS2="        "
ESPACOS3="   "
ESPACOS4="                "
ESPACOS5="     "
ESPACOS6=""
ESPACOS7=" "
ESPACOS8="                          "
ESPACOS9="                       "


class Performance(object):
    
    escolha = 0
    
    
    
    def print_instructions(self):
                        
        print("\n\n")
        print(ESPACOS1,"Qual o seu nível de confiança no acerto das suas respostas nas duas")
        print(ESPACOS2,"últimas etapas ?\n")
        print(ESPACOS3,"Escolha uma das respostas abaixo de 1 (nenhuma confiança) a 9 (total") 
        print(ESPACOS4,"confiança):\n")
        print(ESPACOS5,"1	2	3	4	5	6	7	8	9\n\n")
        print(ESPACOS6)
        escolha = input("Escolha:")
        
        print(ESPACOS9,"Pressione ENTER para iniciar a próxima etapa.")
        input()
    
   
        
    
    
    
        
        
