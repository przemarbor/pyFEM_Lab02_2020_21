import numpy as np
import matplotlib.pyplot as plt
from RysujGeometrie import *

def RysujRozwiazanie(NODES, ELEMS, WB, u):
    '''
    Parametry:
    WEZLY - krance przedzialu
    ELEMENTY - liczba rownomiernie rozmieszczonych wezlow
    WB
    u - rozwiazanie
    Rezultat:
    okno prezentujace geometrie zagadnienia z wykresami wykonanymi
    przy wykorzystaniu pakietu matplotlib
    '''
    
    RysujGeometrie(NODES,ELEMS,WB)
    
    x = NODES[:,1]
    
    plt.plot(x, u, 'm*')