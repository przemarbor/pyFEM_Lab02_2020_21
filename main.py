import numpy as np

# parametry sterujace
c = 0
f = 0 

# geometria
x_a = 0
x_b = 1 

WEZLY = np.array( [[1, 0], 
                   [2, 1],
                   [3, 0.5],
                   [4, 0.75]])

# TODO: ELEMENTY = np.array( )

# warunki brzegowe
twb_L = 'D' # TODO - reszta ....


rysujGeom(WEZLY, ELEMENTY)


print(WEZLY)
