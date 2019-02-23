#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:16:24 2018

@author: xw338
"""
'''testing for flood warning ultra system, return the most flood severe town'''
from floodsystem.flood import get_warning_for_town
from floodsystem.stationdata import *


def run():
    # get all valid towns' name
    towns = get_town_set()
    severity = 0
    most_severe_town = []
    for town in towns:
        tmp_sev = get_warning_for_town(town)
        if tmp_sev is None:
            continue
        if tmp_sev == severity:
            most_severe_town.append(town)
        elif tmp_sev > severity:
            severity = tmp_sev
            most_severe_town = [town]
        else:
            continue
    
    print("These towns :", town)
    print("have the highest flood severity of: ", severity)
        
if __name__ == "__main__":
    run()