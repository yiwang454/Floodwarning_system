#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:34:00 2018

@author: yw454
"""

from floodsystem.stationdata import build_station_list
from floodsystem.analysis import average_of_latest_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime
from random import choice

def run(N=5):
    
    #get the stations data and sorted by latest water level
    stations = build_station_list()
    
    #get the six stations with the largest water level
    highest_five = stations_highest_rel_level(stations, N) # NB Graylingwell does not give any date data
    
    #set the length of time for wanted water level
    dt = 365
    
    i = 0

    for station in highest_five:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0:
            print("This station:\n", station, "\ndoes not give any date data")
            continue
        
        plt.figure(i)
        
        colors = choice(['b', 'g', 'r', 'c', 'y', 'k'])
    
        #plot predicted water level in future 2 days with the past few days
        for p in range(3, 4):
            average_value, water_level_list, dates_list = average_of_latest_level(station, p = p, dt = 7, dt_future = 2)
            plt.plot(dates_list, water_level_list, color = colors)
            plt.title(station.name)
            plt.xticks(rotation=45)
            print(average_value)
            plt.show()
            i += 1
        
    print(i, ' out of ', N, ' were printed')
 
    
        
if __name__ == "__main__":
    run()