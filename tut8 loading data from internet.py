# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:29:21 2018

@author: Raunak
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import urllib




style.use('dark_background')
print(plt.style.available)


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
    
    
    '''
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'label' not in line:
                stock_data.append(line)
                
             '''   
    
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
    
    
    
    
    
    '''
    Convert date from unix time
    
    
    date,closep,highp,lowp,openp,volume =np.loadtxt(stock_data,
                                                    delimiter = ',',
                                                    unpack = True)
    
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    
    date = dateconv(date)
    
    
    
Customization of labels After getting data and plotting
'''
    
    

    
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1


    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    '''
    ax1.plot_date(date, closep, '-', label = "Price")
    
    ax1.plot([], [], linewidth = 5, label = 'LOSS', color = 'r', alpha = 0.5)
    ax1.plot([], [], linewidth = 5, label = 'PROFIT', color = 'g', alpha = 0.5)
    
    ax1.axhline(closep[0], color='k', linewidth=5)

    ax1.fill_between(date, closep, closep[0],
                     where = (closep > closep[0]), 
                     facecolor = 'g', alpha = 0.5)
    
    ax1.fill_between(date, closep, closep[0],
                     where = (closep < closep[0]), 
                     facecolor = 'r', alpha = 0.5)
    
    #36 shows fill upto
    #alpha is opaqueness
    '''
    
    #ax1.plot(date,closep)
    #ax1.plot(date,openp)
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    
    
    ax1.grid(True)#, color = 'g', linestyle='-', linewidth = 1)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
   # ax1.set_yticks([0,25,50,75])

    
    '''
    ax1.spines['left'].set_color('c')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_linewidth(5)
    '''
    
    #ax1.tick_params(axis='x', colors='#f06215')


    plt.xlabel('Date')
    plt.ylabel('Price')
    
    plt.title(stock+'\n')
    
    #plt.legend()
    
    plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.9, top = 0.90, wspace = 0.2, hspace = 0)
    
    plt.show()    



graph_data('TSLA')



