import pandas as pd
import random
def func(x):
    return x+2 *x**2
def df(x,y):
    mass = []
    for i in range(x):
        temp = [random.randint(1,10) for _ in range(y)]
        mass.append(temp)
    data =  pd.DataFrame(mass)
    for i in range(y):
        mean = data[i].mean()
        print(f'Среднее арифметическое {mean}')
        median = data[i].median()
        print(f'Медиана {median}')
    return data