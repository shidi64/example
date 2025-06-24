import numpy as np
import pandas as pd
def sq(x):
    return x**2

def array(x):
    mass = []
    for i in range(1,x+1):
        temp = [int(num) for num in range(1,x+1)]
        mass.append(temp)
    s = np.array(mass)
    # s =  np.array([[1,2,3],[4,5,6],[7,8,9]])
    return pd.DataFrame(s)