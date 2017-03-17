import sys
import csv

with open('../JungleScoutFiles/Search_Term_of_bat_houses.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
for row in reader:
    print("row")
