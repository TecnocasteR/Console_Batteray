import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []



with open('CO_Monthly_26May19.txt') as fp:

    data = [list(map(float, line.strip().split(' '))) for line in fp]
    y = np.transpose(data)
    
    a = np.arange(1, 3585, 1)
    x = np.transpose(a)

#with plt.style.context(('dark_background')): 
    plt.plot(x,y,'k')
    plt.axis([0, 3600, -100, 100])
    plt.xlabel('single trace')
    plt.ylabel('spec %')
    plt.title('Connectivity Plot')

plt.show()
