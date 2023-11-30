# https://docs.python.org/3/library/xml.etree.elementtree.html

import os
import datetime
import requests
import xml.etree.ElementTree as ET
import math
import matplotlib.pyplot as plt


now = datetime.datetime.now()
YYYYNNDDHHMMSS = now.strftime('%Y%m%d%H%M%S')
strUserAgent="someuser@somedomain.com/"+YYYYNNDDHHMMSS
print(YYYYNNDDHHMMSS)
print(strUserAgent)

url = 'https://data.ny.gov/api/views/d6yy-54nr/rows.xml?accessType=DOWNLOAD'

#response = requests.get(url,strUserAgent)
response = requests.get(url,strUserAgent)

if response.status_code == 200:
    xml_content = response.content
else:
    print('Error loading data from URL')

tree = ET.fromstring(xml_content) ## xmltree
""" # test   vvv   eplore the data here   vvv
type(tree) #     <class 'xml.etree.ElementTree.Element'>
tree.tag #     'response'
for elements in tree:
    print(child.tag, child.attrib)
[elem.tag for elem in tree.iter()]
[elem.text for elem in tree.iter()]
[elem.attrib for elem in tree.iter()]
for elem in tree.iter():
    list(elem)
for elem in tree.iter():
    print("    ", elem.tag, elem.text)
""" #        ^^^   eplore the data here   ^^^

os.system('cls')
bigListOfWhiteball = []
bigListOfRedball = []
winnersListRaw = [] # used only for data review and validation
winnersList = [] # used only for data review and validation
topWhiteball = 0
topRedball = 0
drawDate = ""
#Loop through tree
for elem in tree.iter():
    if elem.tag == "draw_date":
        drawDate = elem.text
#            print("    ", elem.tag, elem.attrib, elem.text)
    if elem.tag == "winning_numbers" and drawDate > "2015-10-06T00:00:00":
#        if elem.tag == "winning_numbers":
        print("        ", drawDate, elem.tag, elem.text)
        picks = elem.text
        winnersListRaw.append(picks)
        winningNums = picks.split()
        *whiteBalls, redBall = picks.split()
        pickCount = len(winningNums) - 1
        # Process whiteballs
        for whiteBall in whiteBalls:
            if len(whiteBall) == 1:
                whiteBall = "0" + whiteBall
            winnersList.append(whiteBall)
            bigListOfWhiteball.append(whiteBall)
            i = int(whiteBall)
            if topWhiteball < i:
                topWhiteball = i
            # end of for whiteBall in whiteBalls:
        # Process redball
        bigListOfRedball.append(redBall)
        i = int(redBall)
        if topRedball < i:
            topRedball = i
    # end of for elem in tree.iter():

#    print(winnersListRaw)
#    print(winnersList)
#    print(bigListOfWhiteball)
print("winnersListRaw length: ",len(winnersListRaw))
print("winnersList length: ",len(winnersList))
bigListOfWhiteballLength = len(bigListOfWhiteball)
print("bigListOfWhiteball length: ",bigListOfWhiteballLength)
bigListOfRedballLength = len(bigListOfRedball)
print("bigListOfRedball length: ",bigListOfRedballLength)
print("topWhiteball : ",topWhiteball)
print("topRedball : ",topRedball)
print("topRedball : ",topWhiteball)
print("topRedball : ",topRedball)
##
##
## Process and chart White Balls
##
##

# Count each number
totalValues = topWhiteball 
countOfNumbers=[0] * (totalValues + 1)
countTotal = 0
for num in bigListOfWhiteball:
    i = int(num)
    countOfNumbers[i] = countOfNumbers[i] + 1

# get the average count of the numbers
NumbersOfCountOfNumbers = [int(num) for num in countOfNumbers]
SumOfCountOfNumbers = sum(NumbersOfCountOfNumbers)
MeanOfCountOfNumbers = int(SumOfCountOfNumbers / totalValues)

diviatons=[0] * (totalValues+1)
for i in range(1,totalValues):
    diviatons[i] = abs(countOfNumbers[i]-MeanOfCountOfNumbers)**2
# end of for i in range(1,totalValues):

divNom = 0
for i in range(1,totalValues):
    divNom = divNom + diviatons[i]

variance = divNom / topWhiteball
stdDiv = int(math.sqrt(variance))

print("diviatons: ",diviatons)
print("totalValues: ",totalValues)
print("MeanOfCountOfNumbers: ",MeanOfCountOfNumbers)
print("countOfNumbers: ",countOfNumbers)
#    print("diviatons: ",diviatons)
print("devNom: ",divNom)
print("variance: ",variance)
print("stdDiv: ",stdDiv)

# Chart whiteballs
plt.title('Porweball Whiteball Picks')
plt.legend(['Number Pics'])
plt.xlabel("Pick")
plt.ylabel("Pick Count")
# mean
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers] * (totalValues-1)
plt.plot(x1, y2,label = "Mean",color="#78FF4F")
# +std/3
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers+(stdDiv)] * (totalValues-1)
plt.plot(x1, y2,label = "+strDiv",color="#FFC61B")
# -std/3
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers-(stdDiv)] * (totalValues-1)
plt.plot(x1, y2,label = "-stdDiv",color="#FFC61B")
# data
x = list(range(1,totalValues))
y = countOfNumbers[1:totalValues]
plt.plot(x, y,label = "Count of Picks",color="blue",linewidth=2,marker='o')
#plt.show()
plt.savefig('c:\data\PowerballWhiteBalls'+YYYYNNDDHHMMSS+'.png')
plt.clf()

##
##
## Process and chart Red Balls
##
##

# Count each number
totalValues = topRedball 
countOfNumbers=[0] * (totalValues + 1)
countTotal = 0
for num in bigListOfRedball:
    i = int(num)
    countOfNumbers[i] = countOfNumbers[i] + 1

# get the average count of the numbers
NumbersOfCountOfNumbers = [int(num) for num in countOfNumbers]
SumOfCountOfNumbers = sum(NumbersOfCountOfNumbers)
MeanOfCountOfNumbers = int(SumOfCountOfNumbers / totalValues)

diviatons=[0] * (totalValues+1)
for i in range(1,totalValues):
    diviatons[i] = abs(countOfNumbers[i]-MeanOfCountOfNumbers)**2
# end of for i in range(1,totalValues):

divNom = 0
for i in range(1,totalValues):
    divNom = divNom + diviatons[i]

variance = divNom / topWhiteball
stdDiv = int(math.sqrt(variance))

print("diviatons: ",diviatons)
print("totalValues: ",totalValues)
print("MeanOfCountOfNumbers: ",MeanOfCountOfNumbers)
print("countOfNumbers: ",countOfNumbers)
#    print("diviatons: ",diviatons)
print("devNom: ",divNom)
print("variance: ",variance)
print("stdDiv: ",stdDiv)

# Chart whiteballs
plt.title('Porweball Redeball Picks')
plt.legend(['Number Pics'])
plt.xlabel("Pick")
plt.ylabel("Pick Count")
# mean
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers] * (totalValues-1)
plt.plot(x1, y2,label = "Mean",color="#78FF4F")
# +std/3
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers+(stdDiv)] * (totalValues-1)
plt.plot(x1, y2,label = "+strDiv",color="#FFC61B")
# -std/3
x1 = list(range(1,totalValues))
y2 = [MeanOfCountOfNumbers-(stdDiv)] * (totalValues-1)
plt.plot(x1, y2,label = "-stdDiv",color="#FFC61B")
# data
x = list(range(1,totalValues))
y = countOfNumbers[1:totalValues]
plt.plot(x, y,label = "Count of Picks",color="blue",linewidth=2,marker='o')
#plt.show()
plt.savefig('c:\data\PowerballRedBalls'+YYYYNNDDHHMMSS+'.png')



