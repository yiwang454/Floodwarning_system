# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:24:40 2018

@author: wangyi66
"""

import numpy as np

import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def polyfit(dates, levels, p):
    
    '''
    This function is to derive a best-fit polynomial of the water level of a station about dates
    Input:
    dates   : a list of sample time in a certain period
    levels  : levels of water at the sample times
    p       : the degree of polynomial
    Output:
    a tuple of (1) the polynomial object and (2) any shift of the time (date) axis
    '''
    
    #convert dates into floats
    date_f = matplotlib.dates.date2num(dates)

    d0 = date_f[0]
    
    #find coefficient of the best-fit polynomial
    p_coefficient = np.polyfit(date_f-d0, levels, p)
    
    #convert coefficient into polynomial
    poly = np.poly1d(p_coefficient)
    
    
    return (poly, d0)
    
    
def average_of_latest_level(station, p, dt, dt_future):
    '''
    This function is to get average of the water levels in recent 2 days and the predicting water level of 
    the following 2 days
    Input: 
        station: a MonitoringStaiion object
        p : degree of the best fit polynomial
        dt : the number of sample past days

    '''
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    if len(levels) == 0:
        return None
    poly, d0 = polyfit(dates, levels, p) 
    
    
    # get dates float
    dates_f = matplotlib.dates.date2num(dates)
        
    future_dates_float = dates_f + (dates_f[0] - dates_f[-1])
    
    # get future date from future date float
    future_dates = []
    for date in future_dates_float:
        future_dates.append(matplotlib.dates.num2date(date))
        
    
    future_dates_float_c = future_dates_float - dates_f[0]
    
    # predict future water level by poly
#    x = np.linspace(date_f[0], date_f[-1], len(date_f))
#    print(type(x))
    future_level = list(poly(future_dates_float_c))
    
    #Cuz the predicted level at the end of the future 2 days are too large to be exaxt, so only 
    #fetch part of the future predicted levels
    a = int(float(dt_future)/ float(dt)*len(future_level))
    
    # prepare to calculate average value of past and future levels
    merge_water_level = future_level[-a:-1] + levels 
    merge_dates = future_dates[-a:-1] + dates 
    
    '''
    for date in future_dates[-a:-1]:
        print(date)
        
    print('\n')
    for date in dates:
        print(date)
    
    print('a station')
    '''
    average_level = future_level[-a:-1] + levels[0: a]
    
    #calculate average level
    return sum(average_level) / float(len(average_level)) , merge_water_level, merge_dates
    

    
    
    
    
    
    
        
        
    
    