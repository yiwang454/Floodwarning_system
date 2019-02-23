#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:16:24 2018

@author: yw454
"""

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime

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
        plot_water_level_with_fit(station, dates, levels, 10)
        
        i += 1
        
    print(i, ' out of ', N, ' were printed')
 
    plt.show()
        
if __name__ == "__main__":
    run()