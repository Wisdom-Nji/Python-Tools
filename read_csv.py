#!/bin/python


from pandas import read_csv
import pandas as pd



file1 = 'sample_data.csv'
file2 = 'sample_data2.csv'
file3 = 'sample_data3.csv'

elements_file1 = pd.read_csv( file1 )['name'].tolist()
elements_file2 = pd.read_csv( file2 )['name'].tolist()
elements_file3 = pd.read_csv( file3 )['name'].tolist()

# print (type(elements_file1))

tetha = list(set(elements_file1 + elements_file2 + elements_file3))
print( tetha )

n_tetha = len(tetha)
F = [elements_file1, elements_file2, elements_file3]
list_file = [file1, file2, file3]
# y[len(F)][n_tetha]

y = []

for i in range(len(tetha)):
    for j in range(len(F)):
        for k in range(len(F[j])):
            if F[j][k] == tetha[i] :
                y.append([list_file[j],tetha[i],1])
                break

        y.append([list_file[j],tetha[i],0])

print( y )
