#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:16:24 2018

@author: xw338
"""
'''testing for fetch_recent_data'''
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_recent_data
from floodsystem.flood import stations_highest_rel_level
from matplotlib import pyplot as plt

def run():
    
    #get the stations data and sorted by latest water level
    stations = build_station_list()
    
    #get the six stations with the largest water level
    station = stations_highest_rel_level(stations, 1)[0] # NB Graylingwell does not give any date data
    
    color_list = ['b', 'g', 'r', 'c', 'y'] * 100
    
    for weeks in range(3, 5):
        dates, levels = fetch_recent_data(station.measure_id, weeks)
        if len(dates) == 0:
            print("This station:\n", station, "\ndoes not give any date data")
            continue
        
        plt.figure(weeks)
        plot_water_level_with_fit(station, dates, levels, 10, color_list[weeks])

    plt.show()
        
if __name__ == "__main__":
    run()