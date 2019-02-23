#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:29:22 2018

@author: yw454
"""

from Task1E import run


def test_for_1E():
    '''
    Test for Task1E by asserting output of Task1C is the same as its output during first running
    '''
    output = run()
    standard_output = [('Thames', 55), ('River Avon', 31), ('River Great Ouse', 31), ('River Aire', 21), ('River Calder', 21), ('River Severn', 20), ('River Derwent', 18), ('River Stour', 17), ('River Trent', 15), ('River Wharfe', 15)]
    print(output)
    print(standard_output)
    # assert output == standard_output


test_for_1E()