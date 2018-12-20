##Young Oh
##Group 2
##Question 1
##The placehold is: %A

##Question 2
##import date time and excel
##make a empty list called weekends
##make a list that contains "Saturday" and "Sunday"
##get the data from ShopRecords.csv into a dictionary
##loop data
##split by "/" and sort the dates into year, month, day
##as long as the results are "Saturday" and "Sunday"
##if so add the names of the items into the weekends
##
##loop weekends
##print the results


##Question 3
import csv, datetime
def weekend():
    weekends = []
    weekendDays = ["Saturday", "Sunday"]
    data = csv.DictReader(open("ShopRecords.csv", "r"))
    for entry in data:
        
        dates = entry["Date"].split("/")
        dateSort = datetime.date(int(dates[2]), int(dates[0]), int(dates[1]))

        if dateSort.strftime("%A") in weekendDays:
            weekends.append(entry["Item"])

    for item in weekends:
        print(item)

            
#main
weekend()
