import csv
import numpy
import pandas

filename = "load.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
data = pandas.read_csv(filename, names=names)
print(data.shape)
