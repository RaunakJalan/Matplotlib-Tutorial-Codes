# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:16:08 2018

@author: Raunak
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import urllib


'''
During subplotting we have to give labels at the time of editing the axes
that is why position of plt.xlabel and ylabel has changed.
'''


#For ax1, ax2 and ax3 they are not zooming in at the same time and they are not
#related with the dates and price in x  axis. and can be seen when zoomed in that
#is why sharex and sharey is used.

'''
If the three charts are starting at different position apply [-start:] change to:

ax1.plot(date[-start:], h_1[-start:],...)
and
candlestick_ohlc(ax2, ohlc[-start:],...)

and ax3 is already given [-start:]
'''

style.use('fivethirtyeight')
#print(plt.style.available)

#print(plt.__file__)

MA1 = 10
MA2 = 30

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):

    fig = plt.figure(facecolor = '#f0f0f0')
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex = ax1)
    #plt.xlabel('Date')
    plt.ylabel('Price')

    #creating multi y axis:
    ax2v = ax2.twinx()

    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)
    plt.ylabel('MAvgs')
    
    


    
    stock_price_url ='https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)

    
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})
    
    
    
    
    
    
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    ma1 = moving_average(closep,MA1)
    ma2 = moving_average(closep,MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date,h_l,'-', label = 'H-L')
    
   #This takes only 5 values on y sides ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 5),prune = 'lower')
   #prune removes the overlapping value
    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
  
    #for label in ax2.xaxis.get_ticklabels():
     #   label.set_rotation(45)

    #ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))

    #ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 7),prune = 'upper')
    ax2.grid(True)
    
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1]+4, closep[-1]), bbox=bbox_props)

    
##    # Annotation example with arrow
##    ax2.annotate('Bad News!',(date[11],highp[11]),
##                 xytext=(0.8, 0.9), textcoords='axes fraction',
##                 arrowprops = dict(facecolor='grey',color='grey'))
##
##    
##    # Font dict example
##    font_dict = {'family':'serif',
##                 'color':'darkred',
##                 'size':15}
##    # Hard coded text 
##    ax2.text(date[10], closep[1],'Text Example', fontdict=font_dict)

    ax2v.plot([], [], color = '#0079a3', alpha = 0.4, label = 'Volume')
    ax2v.fill_between(date, 0, volume, facecolor = '#0079a3', alpha = 0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    #limiting height of second y axis
    ax2v.set_ylim(0, 2*volume.max())


    ax3.plot(date[-start:], ma1[-start:], linewidth = 1, label = (str(MA1)+'MA'))
    ax3.plot(date[-start:], ma2[-start:], linewidth = 1, label = (str(MA2)+'MA'))
    
    
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                    where = (ma1[-start:] < ma2[-start:]),
                    facecolor = 'r', edgecolor = 'r', alpha = 0.5)
    
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                    where = (ma1[-start:] > ma2[-start:]),
                    facecolor = 'g', edgecolor = 'g', alpha = 0.5)
    
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 5),prune = 'upper')



    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    
    plt.setp(ax1.get_xticklabels(), visible = False)
    plt.setp(ax2.get_xticklabels(), visible = False)
    
    plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)

    ax1.legend()
    leg = ax1.legend(loc = 9, ncol = 2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)

    ax2v.legend()
    leg = ax2v.legend(loc = 9, ncol = 2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)

    ax3.legend()
    leg = ax3.legend(loc = 9, ncol = 2, prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    
    plt.show()

    fig.savefig('Ebay.png', facecolor = fig.get_facecolor())


graph_data('EBAY')
