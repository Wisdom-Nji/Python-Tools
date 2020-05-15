#!/bin/python

# How I got things working
# pip3 install pandas

from pandas import read_csv
import pandas as pd


file = 'sample_data.csv'
df = pd.read_csv( file )

print("Type: ", type(df))
print( df )
