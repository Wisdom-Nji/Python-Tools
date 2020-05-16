#!/bin/python


from pandas import read_csv
import pandas as pd

filename = 'sample_data.csv'

df_file_content = pd.read_csv( filename )

print( df_file_content )

filename2 = 'sample_data2.csv'

df_file_content2 = pd.read_csv( filename2 )

print( df_file_content2 )


list_rows = df_file_content['name']
list_rows2 = df_file_content2['name']

for row in list_rows2:
    # found = False
    if row in list_rows:
    	print(row, "Found...")

    '''
    for row1 in list_rows:
        if row == row1:
            print(row, "Found!")
            found = True
            break

    if found == False:
        print(row, "Not found!")'''

