#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:19:42 2018

@author: yw454
"""

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime


def run():
    #get the stations data and sorted by latest water level
    stations = build_station_list()
    
    #get the six stations with the largest water level
    highest_six = stations_highest_rel_level(stations, 6)
    
    #set the length of time for wanted water level
    dt = 10
    
    #plotting water level against time of those six stations
    i = 0
    station_name = []
    date_and_level = []
    for station in highest_six:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plt.subplots()
        plot_water_levels(station, dates, levels)
        station_name.append(station.name)
        date_and_level.append((dates, levels))
        i += 1
    
    plt.show()    
    print(station_name)
    return station_name, date_and_level

    
    
if __name__ == "__main__":
    run()