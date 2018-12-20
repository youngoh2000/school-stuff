##lecture 9
##local companies
import csv
def com():
    data = open("companies.csv", "r")
    companies = csv.DictReader(data)

    ##data = csv.DictReader(open("companies.csv", "r")
    cool = []
    for company in companies:
        if company["state"] == "IN":
            cool.append(company["company_name"])
    print(sorted(cool))

##companies v2
def companies2():
    data = csv.DictReader(open("companies.csv", "r"))
    user = input("Search for companies in what state?: ")

    lst = []
    for entry in data:
        if user == entry["state"]:
            lst.append((entry["company_name"],entry["web"]))
    for tuple in lst:
        company, web = tuple
        spaces = 30 - len(company)
        print(company, spaces*" ", web)
companies2()
