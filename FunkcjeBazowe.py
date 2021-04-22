import numpy as np

def FunkcjeBazowe(n):
    '''
    Parametry :
    n - stopien wymaganych funkcji ksztaltu
    Zwraca :
    f - (n +1) -elementowa lista ( lub tupla ) funkcji bazowych stopnia n
    df - (n +1) -elementowa lista ( lub tupla ) pochodnych funkcji bazowych stopnia n
    '''
    
    if n==0:
        f  = (lambda x: 1 + 0*x )
        df = (lambda x: 0*x )
        
    elif n == 1:
        
        f = (lambda x: -1/2*x + 1/2, lambda x: 0.5*x+0.5 )
        df= (lambda x: -1/2 + 0*x ,   lambda x: 0.5  + 0*x )
        
    # elif n == 2:
    #     f =  (lambda , lambda, lambda )
    #     df = 
        
    else: 
        raise Exception("Blad w funkcji FunkcjeBazowe().")

    return f,df
