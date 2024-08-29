tests=[]
def evaluate(code,task):
    import time
    for testcases in task:
        startTime=time.time()
        test=code(testcases['input'])
        endTime=time.time()
        if test==testcases['output']:
            print(f'Passed the Test: {testcases}')
        else:
            print(f'Failed the Test: {testcases}')
        print(f'Evaluation time: {endTime-startTime}s')




    

        
        
        
         
        
    
    
    
    

        
            
        
    



            
            
        



