#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:09:48 2018

@author: yw454
"""

import numpy as np
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib
from random import choice
from floodsystem.analysis import average_of_latest_level  #


def plot_water_levels(station, dates, levels):
    '''
    This function will plot the water level against time for a given station
    Input: 
    station : a MonitoringStation object containing data about a station
    dates   : a list of sample time in a certain period
    levels  : levels of water at the sample times
    color   : the color used to plot this group of lines
    '''
    
    colors = choice(['b', 'g', 'r', 'c', 'y', 'k'])
    # Plot
    plt.plot(dates, levels, label= station.name, color = colors)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.legend()
    
    # plot horizontal lines showing the typical range of water level
    date_length = len(dates)
    low_r = station.typical_range[0] 
    y0 = [low_r] * date_length
    high_r = station.typical_range[1] 
    y1 = [high_r] * date_length
    plt.plot(dates, y0, '--', color = colors)
    plt.plot(dates, y1, '--', color = colors)
    
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels


def plot_water_level_with_fit(station, dates, levels, p):
    '''
    This function plot the best-fit polynomial of the water level about dates of a certain station
    with the original data plotted as well
    Input: 
    station : a MonitoringStation object containing data about a station
    dates   : a list of sample time in a certain period
    levels  : levels of water at the sample times
    p       : the degree of polynomial
    
    '''
    #get best-fit polynomial from dates and levels
    poly, d0 = polyfit(dates, levels, p)
    
    #shift date so that the first value of the date we use to plot is 0
    date_f = matplotlib.dates.date2num(dates) - d0
    
    colors = choice(['b', 'g', 'r', 'c', 'y', 'k'])
    
    #plot original data points and best-fit polynomial
    x = np.linspace(date_f[0], date_f[-1], len(dates))
    y = poly(x)
    plt.plot(dates, y, color = colors)
    plt.plot(dates, levels, '.', color = colors)
    plt.xticks(rotation=45)
    
    
    # plot horizontal lines showing the typical range of water level
    date_length = len(dates)
    low_r = station.typical_range[0] 
    y0 = [low_r] * date_length
    high_r = station.typical_range[1] 
    y1 = [high_r] * date_length
    plt.plot(dates, y0, '--', color = colors)
    plt.plot(dates, y1, '--', color = colors)
    
    

    
    
    
    


