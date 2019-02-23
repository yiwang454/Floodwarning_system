#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:51:20 2018

@author: yw454
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    '''
    Test for function: rivers_by_station_number
    '''
    
    stations = build_station_list()
    output = rivers_by_station_number(stations, 12)
    print(output)
    return output
    
if __name__ == "__main__":
    run()
