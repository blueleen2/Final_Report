# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 20:36:32 2014

@author: JN
"""

import pandas as pd
import statsmodels.api as sm
import pylab as pl
import scipy.stats as stats

Raw_data = pd.read_csv('C:/Users/JN/Desktop/AnovaData.csv')

print Raw_data.describe()

Raw_data.hist()

pl.show()

print Raw_data.BPM

print stats.normaltest(Raw_data.BPM)

New_Column = ['RSP_Cycle', 'BPM']

New_Raw_Data = Raw_data[New_Column]

print New_Raw_Data

print stats.mstats.kruskalwallis(New_Raw_Data)