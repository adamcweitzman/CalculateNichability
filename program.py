import sys
import csv

# path = '../JungleScoutFiles/Search_Term_of_bat_houses.csv'
path = '../JungleScoutFiles/test.csv'

with open('../JungleScoutFiles/Search_Term_of_bat_houses.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))
