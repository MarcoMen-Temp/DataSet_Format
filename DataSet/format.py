"""Marco Men - Exercise 5 (Format)
Adapted from StackOverFlow: 'Formatting Output of CSV file in Python' """ 
import csv

with open("iris.csv") as f:
      reader = csv.reader(f)
      for row in reader:
            print('{:<10}  {:<10}  {:<10}  {:<10}' .format(*row))
