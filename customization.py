# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:43:40 2018

@author: Raunak
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 22:00:57 2018

@author: Raunak
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np
import urllib
from urllib import request as ur
import matplotlib.dates as mdates
import datetime as dt
from matplotlib import style


style.use('_classic_test')
print(plt.style.available)

fig = plt.figure()

ax1 = plt.subplot2grid((1,1), (0,0))


date = []
closep = []
highp = []
lowp = []
openp = []
volume = []

with open('22-09-2016-TO-21-09-2018SBINN2N.csv', 'r') as csvfile:
    
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        if 'Last Price' not in row and 'Date' not in row and 'High Price' not in row and 'Low Price' not in row and 'Open Price' not in row and 'No. of Trades' not in row:
            date.append(str(row[2]))
            closep.append(float(row[8]))
            highp.append(float(row[5]))
            lowp.append(float(row[6]))
            openp.append(float(row[4]))
            volume.append(int(row[10]))
            
            

#print(price)
#print(price[0])

ax1.plot(date, closep, '-', label = "Close")
ax1.plot(date, openp, '-', label = "Open")
    
ax1.plot([], [], linewidth = 5, label = 'LOSS', color = 'r', alpha = 0.5)
ax1.plot([], [], linewidth = 5, label = 'PROFIT', color = 'g', alpha = 0.5)

#ax1.axhline(closep[0], color = 'k', linewidth = 5)

#ax1.fill_between(date, closep,0)


'''
ax1.fill_between(date, closep, closep[0],
                 where = (closep > closep[0]), 
                 facecolor = 'g', alpha = 0.5)
    
ax1.fill_between(date, closep, closep[0],
                 where = (closep < closep[0]), 
                 facecolor = 'r', alpha = 0.5)
'''


for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)


ax1.grid(True, color = 'g', linestyle='-', linewidth = 1)
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
ax1.set_yticks([10900,11000, 11200,11400, 11600])


#removes line or colors it
#ax1.spines['left'].set_color('c')
#ax1.spines['right'].set_visible(False)
#ax1.spines['top'].set_visible(False)

#ax1.spines['left'].set_linewidth(5)
#ax1.tick_params(axis = 'x', colors = '#f06215')

            
'''

x=0
y = len(date)
ohlc = []

while x < y:
    append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]

    ohlc.append(append_me)
    x+=1
    
    

candlestick_ohlc(ax1, ohlc, width = 0.6)


'''
plt.xlabel('Date')
plt.ylabel('Price')

plt.title('SBIN\n')

plt.legend()

plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.9, top = 0.90, wspace = 0.2, hspace = 0)

plt.show()