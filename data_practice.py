#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:54:09 2020

@author: harpal
"""
import os
import pandas_datareader.data as pdr
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
#from matplotlib.finance import candlestick_ohlc
'''
ticker = 'PNB'
end_date =  dt.datetime.today()
start_date = end_date -dt.timedelta(120)
data = pdr.get_data_yahoo('TITAN.BO', start_date, end_date)
price = data['Close']
'''
data1  = pd.read_csv('data.csv')
data = data1
ltps = data.ltp.values
highs = data.High.values
volms = data.Volume.values
mdates.strpdate2num

datelist = data.timestamp.values

dates = list(map(dt.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d %H:%M:%S.%f']))
#dates = list(map(lambda x: x.replace(microsecond=0).time(), dates1))
#print(dates[1])
def figu():
    fig = plt.figure()
    ax1 = plt.subplot(2,1,1)
    ax1.plot(dates, ltps)
    ax1.plot(dates, highs)
    
    ax2 = plt.subplot(2,1,2)
    ax2.plot(dates, volms)
    #Number of tick on xaxis
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #Display The Date on axis in desired Forrmat
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax1.grid(True)

    #rotate label
    for l in ax1.xaxis.get_ticklabels():
        l.set_rotation(90)
    plt.xlabel('Dates')
    plt.ylabel('Price')

    
    plt.show()

figu()
#candlestick_ohlc