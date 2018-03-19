"""Marco Men - Exercise 5 (Format)
Adapted from StackOverFlow: 'Formatting Output of CSV file in Python' """ 
import csv

def concat(*args, sep= " | "):
      return sep.join(args)


print(concat("Petal Length", "Petal Width", "Sepal Length","Sepal Width"))

with open("iris.csv") as f:
      reader = csv.reader(f)
      for row in reader:
            print('{:>12} | {:>11} | {:>12} | {:>11}' .format(*row))
