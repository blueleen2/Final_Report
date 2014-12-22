# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 17:26:12 2014

@author: JN
"""


import pandas as pd
import statsmodels.api as sm
import pylab as pl


df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")

df.head()

df.columns = ["admit", "gre" , "gpa", "prestige"]

print df.columns

print df.describe()

df.hist()

pl.show()

dummy_ranks = pd.get_dummies(df['prestige'],prefix='prestige')

print dummy_ranks.head()

cols_to_keep = ['admit', 'gre', 'gpa']

data = df[cols_to_keep].join(dummy_ranks.ix[:, 'prestige_2':])

print data.head()

data['intercept'] = 1.0

train_cols = data.columns[1:]

logit = sm.Logit(data['admit'], data[train_cols])

result = logit.fit()

print result.summary()
