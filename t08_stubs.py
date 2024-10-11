# CSC 445 - Fall 2022
# Code for T08: Practicing with Recursion
# Author: Patrick Shepherd

# This file gives you stubs for five recursive functions you must complete.

import os

# Function 1: Determine if an element is in a list.
def findme(item, thelist):
    """ Takes an integer, 'item', and searches for it in list 'thelist' recursively.
        Return True if item is in mylist, False otherwise.
    """
    if 0 == len(thelist):
        return false 
    elif item == thelist[0]:
        return true
    findme(item, mylist[1:])
  
# Function 2: Determine the number of steps it takes to solve Tower of Hanoi with n rings.
def hanoi(n):
    """ Takes an integer n and returns the number of moves it would take to solve the
        Tower of Hanoi with n disks.
        Return an integer number of moves.
    """
    pass
  
# Function 3: Determine if a string is a palindrome.
def ispalindrome(thestring):
    """ Check if string 'thestring' is a palindrome.
        Return True if so, False otherwise.
    """
    pass
  
# Function 4: Pretty-print a directory tree on your computer
def printtree(f, prefix=''):
     print(f"{prefix}{'*' * len(prefix)}{os.path.basename(f)}")
if os.path.isdir(f):
    # Get the list of items in the directory
    items = os.listdir(f)
        
    for item in items:
        # Construct the full path of the item
        full_path = os.path.join(f, item)
            
        # Recursively call printtree for each item
        printtree(full_path, prefix + ' ')
pass
  
# Helper function for mergesort
def merge(lista, listb, listc):
    """ Merges 3 lists, lista, libst
    """
    pass

# Function 5: Implement MergeSort, but with a 3-way split instead of 2-way.
def mergesort(thelist):
    """ Sorts a list of numbers using a modified MergeSort algorithm,
    """
    pass
