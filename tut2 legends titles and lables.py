# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:09:01 2018

@author: Raunak
"""

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]


plt.plot(x, y, label = 'First Line')

plt.plot(x2, y2, label = 'Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')

plt.title('Interesting Graph\nCheck it out\n')

plt.legend()

plt.show()













