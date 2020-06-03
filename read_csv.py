#!/bin/python


from pandas import read_csv
import pandas as pd



file1 = 'sample_data.csv'
file2 = 'sample_data2.csv'
file3 = 'sample_data3.csv'

elements_file1 = pd.read_csv( file1 )['name']
elements_file2 = pd.read_csv( file2 )['name']
elements_file3 = pd.read_csv( file3 )['name']

tetha = elements_file1 + elements_file2 + elements_file3

n_tetha = len(tetha)
F = [file1, file2, file3]
y[len(F)][n_tetha]

for i in tetha:
    for j in F:
        for k in F[j]:
            if F[j][k] == tetha[i] :
                y[j][i] = 1
                break

        y[j][i] = 0

print( y )

