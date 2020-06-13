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
# print( tetha )

n_tetha = len(tetha)
F = [elements_file1, elements_file2, elements_file3]
list_file = [file1, file2, file3]

y = []

for i in range(len(tetha)):
    for j in range(len(F)):
        found = False
        for k in range(len(F[j])):
            if F[j][k] == tetha[i] :
                # y.append([list_file[j],tetha[i],1])
                mariette = [list_file[j], tetha[i], 1]
                # array = [ filename, element, bool ]
                y.append( mariette )
                found = True
                break

        if found == False :
            # y.append([list_file[j],tetha[i],0])
            y.append([list_file[j], tetha[i], 0])


# Declaring empty arrays for files and elements so to have them unique
list_of_file_from_y = []
list_of_elements_from_y = []

# looping through y to get the names of files and the individual elements, then storing the output in their respective arrays
for item in y:
    list_of_file_from_y.append( item[0] ) # for each item in y, we take out the filename
    list_of_elements_from_y.append( item[1] ) # for each item in y, we take out the element

list_of_file_from_y = list(set(list_of_file_from_y)) # we make the filenames unique thus no repetition
list_of_file_from_y.sort() # we sort the filenames in ascending order

list_of_elements_from_y = list(set(list_of_elements_from_y)) # we repeat the above steps for the elements here
# list_of_elements_from_y.sort()

print( "Element", end=' ') # we print element in the first column of our table, we end with ' ' because we want to continue on the same line to print the filenames

for i in range(len(list_of_file_from_y)): # we loop through the filenames and print them one at a time, ending with ' ' for the reasons explained above
    print( list_of_file_from_y[i], end=' ')

print() # this takes us to the next row

for element in list_of_elements_from_y: # we loop through every element and print them for each row, we end with ' ' so that we can continue on the same line
    print( element, end= ' ')
    for item in y: # we loop through y, to get the boolean of each matching file for each element
        if item[1] == element : # we compare the element in each array of y to match the array of the row we currently are looping in
            print( item[2], end= ' ') # print the booleans in single line
    print()

