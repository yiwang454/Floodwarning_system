#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:37:10 2018

@author: xw338
"""

from Task2B import run


def test_task2B():
    '''
    Test for Task2B by asserting output of Task1C is the same as its output during first running
    Due to the fact that task2B has interactions with online data, it is better to just test that it is runnable
    '''
    run()


test_task2B()