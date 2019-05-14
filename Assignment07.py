#-----------------------------------------------------#
#Project: Assignment 07
#Developer: LWinkenwerer
#Date: 05/12/2019
#Changelog: None
#----------------------------------------------------#
"""The purpose of this assignment is to create a program to pickle and unpickle data and create a Try/Except block"""

#Section 1. Pickling Data

import pickle #need to import pickle to serialize the data

import codecs #use codecs to fix the data type error and specify UTF-8

with codecs.open('data_pick.dat', 'a', 'utf-8-sig') as pickle_file: #specify that the binary file pickle_file is UTF-8

    import numpy as numpy #import the scientific computing package NumPy
    '''create my random dictionary of numbers to serialize'''
    data_dict = {
        'fltData1': numpy.random.random(1),
        'fltData2': numpy.random.random(1),
        'fltData3': numpy.random.random(1),
    }

    with open('data_pick.dat', 'wb') as pickle_file:  #pickle my randomly generated data dictionary to pickle_file
        pickle.dump(data_dict, pickle_file)

    with open('data_pick.dat', 'rb') as pickle_file:  #unpickle my data
        new_data = pickle.load(pickle_file)

    print(new_data) #check out the results

    pickle_file.close()


#Section 2. Practice Try/Except Block

try:

    import keras as keras  #attempt to import any package/library and see if it has been installed already

except ModuleNotFoundError as e:
    print("\nModule not yet installed for import!")

except Exception as e:
    print("python error info:")
    print(e)

input("\nEnter 'Yay!' to Exit")

