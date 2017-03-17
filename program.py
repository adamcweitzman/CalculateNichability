import sys
import csv

path = '../JungleScoutFiles/Search_Term_of_bat_houses.csv'
# path = '../JungleScoutFiles/test.csv'

with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Rating'], row['Price'])
        # print(row['person'], row['place'])
