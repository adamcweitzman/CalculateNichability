import sys
import csv
import math


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

path = '../JungleScoutFiles/Search_Term_of_bat_houses.csv'
#path = '../JungleScoutFiles/Search_Term_of_shower_ curtains.csv'
#path = '../JungleScoutFiles/test.csv'

totalReviews = 0
totalRevenue = 0
numberOfRowsUnderFiftyReviews = 0
count = 0

with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        formattedRevenue = str(row['Est. Revenue']).replace(',', '').replace('$', '').replace('<', '')
        formattedReview = str(row['# of Reviews']).replace(',', '')
        if(formattedReview == "N.A."  or formattedRevenue == "N.A."):
            continue
        elif(int(formattedReview) <= 50):
            print("hi")
            revenue = int(formattedRevenue)
            review = int(formattedReview)
            totalRevenue += revenue
            totalReviews += review
            count += 1

AvgRevenue = totalRevenue / count
AvgReview = totalReviews / count
fullnessPercentage = (AvgReview / AvgRevenue) * 100
score = str((500 - round(fullnessPercentage * 100)) * .2)
print("Niche Score: " + score)

# 3000 rev 10 reviews 33 BEST
# 3000 rev 50 reviews 166 mid
# 2000 rev 10 reviews mid 250
# 3000 rev 30 reviews 100 mid
# 1000 rev 45 reviews

# 5200 and 5 .09 should be best
# 19000 and 5 .02
# 19000 and 250 1.3 should be worst


#want low rank and low reviews




