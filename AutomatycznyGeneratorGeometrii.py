import numpy as np

def AutomatycznyGeneratorGeometrii(a,b,n):
    '''
    Parametry:
    a,b - krance przedzialu
    n - liczba rownomiernie rozmieszczonych wezlow
    Zwraca:
    WEZLY
    ELEMENTY
    '''
    
    lp = np.arange(1,n+1)
    x = np.linspace(a,b,n) ;        
    WEZLY = (np.vstack( (lp.T, x.T) )).T #[lp.T, x.T]

    
    lp = np.arange(1,n)
    C1 = np.arange(1,n)
    C2 = np.arange(2,n+1)
    ELEMENTY = (np.block( [[lp], [C1], [C2] ] ) ).T
                    
    return WEZLY, ELEMENTY
