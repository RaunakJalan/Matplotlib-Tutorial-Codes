# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 03:31:29 2018

@author: Raunak
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import urllib




style.use('fivethirtyeight')
#print(plt.style.available)


def bytespdate2num(fmt, encoding = 'utf-8'):
    
    strconvertor = mdates.strpdate2num(fmt)
    
    def bytesconvertor(b):
        s = b.decode(encoding)
        return strconvertor(s)
    
    return bytesconvertor
    
    

def graph_data(stock):
    
    
    fig = plt.figure()

    ax1 = plt.subplot2grid((1,1), (0,0))
    
    
    #hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    
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


    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    
    
    ax1.grid(True)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
   
    ax1.tick_params(axis = 'x', colors = '#f06215')
    ax1.tick_params(axis = 'y', colors = '#000000')
    
    ax1.annotate('Bad News!',(date[1500],highp[750]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(facecolor='k',color='grey'))
                    
                    
    #To show text on screen
    '''
    font_dict = {'family':'serif',
                 'color':'darkred',
                 'size':20}
            
    ax1.text(date[1500], closep[750], 'Text', fontdict = font_dict)
    '''

    plt.xlabel('Date')
    plt.ylabel('Price')
    
    plt.title(stock+'\n')
    
    #plt.legend()
    
    plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.9, top = 0.90, wspace = 0.2, hspace = 0)
    
    plt.show()    



graph_data('EBAY')



