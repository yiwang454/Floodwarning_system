#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:07:22 2018

@author: yw454
"""

from Task1C import run

def test_for_1C():
    '''
    Test for Task1C by asserting output of Task1C is the same as its output during first running
    '''
    in_put = run()
    assert in_put == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    
test_for_1C()
