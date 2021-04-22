import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

#from AutomatycznyGeneratorGeometrii import generujTabliceGeometrii as GenTab
from GeometriaDefinicja import *
from AutomatycznyGeneratorGeometrii import *
from RysujGeometrie import *
from Alokacja import *
from FunkcjeBazowe import *


if __name__ == '__main__':
    
    # Preprocessing
    
    ## parametry sterujace
    c = 0 
    f = lambda x: 0*x # wymuszenie


    ## 2. Geometria
    ### 2.1 Definicja
    WEZLY, ELEMENTY, WB = GeometriaDefinicja()
    n = np.shape(WEZLY)[0]
    
    ### lub Automatyczne wygenerowanie geometrii
    x_a =  0 
    x_b =  1
    n = 5
    WEZLY, ELEMENTY = AutomatycznyGeneratorGeometrii(x_a,x_b,n)
    # warunki brzegowe
    WB    = [{"ind": 1, "typ":'D', "wartosc":1}, 
              {"ind": n, "typ":'D', "wartosc":2}]
    
    
    RysujGeometrie(WEZLY, ELEMENTY, WB)

    # print(WEZLY)
    # print(ELEMENTY)

    A,b = Alokacja(n)
    
    # print(A)
    # print(b)
    
    stopien_fun_bazowych = 1
    phi, dphi = FunkcjeBazowe(stopien_fun_bazowych)
    
    # xx = np.linspace(-1,1, 101) 
    # plt.plot(xx, phi[0](xx), 'r' )
    # plt.plot(xx, phi[1](xx), 'g' )
    # plt.plot(xx, dphi[0](xx), 'b' )
    # plt.plot(xx, dphi[1](xx), 'c' )
    
    #PROCESSING
    
    liczbaElementow = np.shape(ELEMENTY)[0]
    
    for ee in np.arange(0, liczbaElementow ):
        
        elemRowInd = ee
        elemGlobalInd = ELEMENTY[ee,0]        
        elemWezel1 = ELEMENTY[ee,1]     # indeks wezla poczatkowego elemntu ee
        elemWezel2 = ELEMENTY[ee,2]     # indeks wezla koncowego elemntu ee
    
        x_a = WEZLY[ elemWezel1-1 ,1]
        x_b = WEZLY[ elemWezel2-1 ,1]
    
    
        Ml = np.zeros( stopien_fun_bazowych+1, stopien_fun_bazowych+1 )
        
        J = (x_b-x_a)/2
        
        
        Ml[0,0] = J * spint.quad( Aij(dphi[0], dphi[0], c, phi[0],phi[0]), -1, 1)
        
        
        # TODO: obliczyc pozostale elementy Ml
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    