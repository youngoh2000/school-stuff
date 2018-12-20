#Young Oh
#Group 2

#1
#re.findall("^#+(?:[\w]{6}"), lines)

#2
#import urllib.request and re
#extract data by urllib.request.urlopen...
#re.findall anything after "<div>W that has 2 numericals for wins
#re.findall anything after "<div>W that has 2 numericals for losses
#return wins and loses

#bonus
#make lists for win and lose
#loop through stats[0] which is the winning game scores
#split them into individual numbers
#differences between the 2 numbers are added to winScore
#loop through stats[1] which is the losing game scores
#split them into individual numbers
#differences between the 2 numbers are added to loseScore
#print out the differences between the 2 lists

#3
import urllib.request, re
def basketball(url):
    web_page = urllib.request.urlopen(url)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    wins = re.findall("(?<=<div>W) [0-9]+-[0-9]+", lines)
    losses = re.findall("(?<=<div>L) [0-9]+-[0-9]+", lines)
    print("Wins: ", len(wins))
    print("Losses: ", len(losses))
    return wins, losses

#main
stats = basketball("http://cgi.soic.indiana.edu/~dpierz/mbball.html")

#Bonus
winScore = 0
loseScore = 0
for win in stats[0]:
    split = win.split("-")
    difference = int(split[0])-int(split[1])
    winScore += difference
for lose in stats[1]:
    split = lose.split("-")
    difference = int(split[0])-int(split[1])
    loseScore += difference
print("Total Difference:", winScore - loseScore)
