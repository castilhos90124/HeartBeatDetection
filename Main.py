#from CondicaoMotoraS1 import CondicaoMotoraS1
#from PreInteroceptivaS2 import PreInteroceptivaS2
#from FeedbackS3 import FeedbackS3
#from PosInteroceptivaS4 import PosInteroceptivaS4

import time


class Main(object):
    
    teste = 0
    
    start_time = time.time()
    
    print("ola")
    for i in range(0,10000000):
        teste+=1
    print("mundo")
    elapsed_time = time.time() - start_time
    
    print(start_time)
    print(elapsed_time)
    
   

    