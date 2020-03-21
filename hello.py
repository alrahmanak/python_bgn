#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# Define a main() function that prints a little greeting.
def main():
  # get value of length of the array
  arrayLenght = len(sys.argv)
  firstParameter = sys.argv[0]
  secondParameter = sys.argv [1]
  thirdParameter = ''
  fourthParameter = ''
  fifthParameter =''
  sixthParameter = ''

  
  if arrayLenght >= 3:
    thirdParameter = sys.argv [2]
  if arrayLenght >= 4:
    fourthParameter = sys.argv [3]
  if arrayLenght >= 5:
    fifthParameter = sys.argv [4]
  if arrayLenght >= 6:
    sixthParameter = sys.argv [5]
  
  # Get the name from the command line, using 'World' as a fallback.
  if arrayLenght >= 2:
    name = sys.argv[1]
  else:
    name = 'Dhahran'
  # print the lenght of the array sys.argv
  print ('Lenght of the array : ', arrayLenght)
  print('First parameter :', firstParameter)
  print('Second parameter :', secondParameter)
  print('Third parameter :', thirdParameter)
  print('fourth parameter :', fourthParameter)
  print('fifth parameter :', fifthParameter)
  print('sixth parameter :', sixthParameter)
  print ('Howdy ', name)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
