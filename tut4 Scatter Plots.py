# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:52:54 2018

@author: Raunak
"""

import matplotlib.pyplot as plt



x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]


plt.scatter(x, y, label = "Skitscat", color = 'k', marker = 'o', s = 100)


plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting Graph\nCheck it out\n')

plt.legend()

plt.show()
