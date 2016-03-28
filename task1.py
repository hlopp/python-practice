#!/usr/bin/python

key = raw_input ("Type keys with space separator:")
value = raw_input ("Type values with space separator:")

keylist = key.strip().split(' ')
valuelist = value.strip().split(' ')

def func(list1,list2):
    ''' Create dictionary from two lists'''
    dictionary = {}
    for i in range(0,len(list1)):
        #print list1[i],list2[i]
        if i >= len(list2):
            dictionary[list1[i]] = None
        else:
            dictionary[list1[i]] = list2[i]
    return dictionary

print(func(keylist,valuelist))


	

 
