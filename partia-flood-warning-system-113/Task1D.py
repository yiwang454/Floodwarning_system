#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:10:02 2018

@author: yw454
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_river


def run():
    '''Testing for rivers_with_stations and stations_by_river
    '''
    stations = build_station_list()
    river_sets = rivers_with_stations(stations)
    # showing the number of rivers with stations
    print('There are {} rivers with stations'.format(len(river_sets)))
    
    output = []
    output.append(len(river_sets))
    
    river_list = []
    for river in river_sets:
        river_list.append(river)
    sorted_river = sorted(river_list)

    print(sorted_river[:10])
    
    output.append(sorted_river[:10])
    
    def prt(river_name, output):
        '''This functions will print the list of stations on the given rivers 
        Input:
            river_name:  name of given river, type: string
        '''
        # get lists of rivers mapped to river names
        list_of_stations = stations_by_river(stations)
        
        print(river_name + " has stations including: ")
        print(sorted(list_of_stations[river_name]))
        output.append(sorted(list_of_stations[river_name]))

    prt('River Aire', output)
    prt('River Cam', output)
    prt('Thames', output)
    
    return output


if __name__ == "__main__":
    run()

