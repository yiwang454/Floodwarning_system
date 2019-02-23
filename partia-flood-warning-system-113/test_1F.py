#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:37:10 2018

@author: yw454
"""

from Task1F import run

def test_task1F():
    '''
    Test for Task1F by asserting output of Task1C is the same as its output during first running
    '''
    in_put = run()
    assert in_put ==['Addlestone', 'Airmyn', 'Allerford', 'Arundel Queen St Bridge', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Fleetwood', 'Goole', 'Gravesend', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', "King's Lynn", 'Littlehampton', 'Paull', 'Salt end', 'Silloth Docks', 'Stone Creek', 'Templers Road', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme PS', 'Wilfholme PS Hull Level']
    
test_task1F()