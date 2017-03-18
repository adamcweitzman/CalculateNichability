import sys
import csv
import math

#path = '../JungleScoutFiles/Search_Term_of_bat_houses.csv'
#path = '../JungleScoutFiles/Search_Term_of_shower_ curtains.csv'
#path = '../JungleScoutFiles/test.csv'
#path = '../JungleScoutFiles/Bedding.csv'
path = '../JungleScoutFiles/Search Term of small drones.csv'
#path = 'users/adam/Desktop/AmazonFBA/JungleScoutFiles/'

def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


def Main():
    totalReviews = 0
    totalRevenue = 0
    numberOfRowsUnderFiftyReviews = 0
    count = 0

    with open(path) as csvfile:
        for i in range(7):
            csvfile.__next__()
        reader = csv.DictReader(csvfile)
        for row in reader:
            formattedRevenue = str(row['Est. Revenue']).replace(',', '').replace('$', '').replace('<', '')
            formattedReview = str(row['# of Reviews']).replace(',', '')
            if(formattedReview == "N.A."  or formattedRevenue == "N.A."):
                continue
            elif(int(formattedReview) <= 50):
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
    input("press any key to continue...")

if __name__ == "__main__":
    Main()




