import pandas as pd 
import matplotlib.pyplot as plt
import numpy
import math
import scipy


cap = 4000
x0 = 2026

def logistic(x, k):
    return (cap/(1+pow(math.e, -1*k*(x-x0))))

df  = pd.read_excel('TCP23_data.xlsx')
x = numpy.array([2018, 2019, 2020, 2021, 2022])
y = numpy.array([369, 423, 416, 750, 928])
fig, ax = plt.subplots()
plt.scatter(x, y)
popt, _ = scipy.optimize.curve_fit(logistic, x, y)
new_x = numpy.arange(2000, 2050, 1)
k = popt 
y_new = logistic(new_x, k)
plt.plot(new_x, y_new, '--', color='red')
plt.show()
