import numpy as np
import matplotlib.pyplot as plt
# import scipy.integrate as spint
#from AutomatycznyGeneratorGeometrii import generujTabliceGeometrii as GenTab
from GeometriaDefinicja import *
from AutomatycznyGeneratorGeometrii import *
from RysujGeometrie import *

if __name__ == '__main__':
    
    # Preprocessing
    
    ## parametry sterujace
    c = 0 
    f = lambda x: 1 # wymuszenie


    ## 2. Geometria
    ### 2.1 Definicja
    WEZLY, ELEMENTY, WB = GeometriaDefinicja()
    
    ### lub Automatyczne wygenerowanie geometrii
    x_a =  0 
    x_b =  1
    n = 5
    WEZLY, ELEMENTY = AutomatycznyGeneratorGeometrii(x_a,x_b,n)
    # warunki brzegowe
    WB    = [{"ind": 1, "typ":'D', "wartosc":0}, 
             {"ind": n, "typ":'D', "wartosc":1}]
    
    
    RysujGeometrie(WEZLY, ELEMENTY, WB)

    print(WEZLY)
