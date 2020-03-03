# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:41:01 2019

@author: prego-j
"""
import csv 
import sys 
import copy

#placeholder list for copy of the mlb-games
n_list = []

#Opening file and converting to list
#Added exception handling for when missing MLB file
def reading():
    try:
        with open('justices.csv', newline="") as file:      
            csv_reader = csv.reader(file)
            read = file.readlines()       
        return read
    except FileNotFoundError as e:
        print("Could not locate Justices File.")
        print("System is closing.")
        print()
        sys.exit()
        
def openAndLoad():
    read_line = reading()
    read = [line.rstrip() for line in read_line] #stripped the right to eliminate extra space in column 2
    for line in read:
        line.replace('\n','')
        row = line.split(',')
        x = int(row[4])        
        y = int(row[5])
        if y == 0:
            row.append('2019')
        z = y-x
        row.append(z)
        n_list = copy.deepcopy(row)
        state = row [3]
        #print(state)
        if state == search():
            print('Its here')
        else:
             print ("{0:<20s}{1:^11s}{2:<5s}".format("JUSTICE","APPOINTED BY ","YRS SERVED"))
             print ("{0:<20s}{1:^11s}{2:<5s}".format("*"*8,"*"*8,"*"*5))
             print(n_list[1],'\t\t\t',n_list[2],n_list[3],n_list[6])
            
            
                
    
def search():
    state = input('Enter a two-letter state abbreviation: ')
    return state
        
def output():
    for i in row:
        print (row[3])   
       
def main():
    reading()    
    openAndLoad()
    #output()
    #search()
    
if __name__ == '__main__':
    main()