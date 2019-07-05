import sys
import csv

file = open("2017_ALL.csv","r")
next(file)

if len(sys.argv)!=2:
	print "wrong parameters! try again " 
	exit()

W = []	
statisticsToUse = []
statistics = sys.argv[1].replace('[',' ').replace(']',' ').replace(',',' ').split()
flags = []


for i in range(len(statistics)):
	statisticsToUse.append(int(statistics[i])+2)

def dominates(firstItem,secondItem):
	counter = 0
	for i in range(len(statisticsToUse)):
		if float(firstItem[statisticsToUse[i]])>=float(secondItem[statisticsToUse[i]]):
			counter += 1
	if counter != len(statisticsToUse):
		return False
	return True


line = next(file).split(",")
W.append(line)
k=0
itemsToPop = []
while(k!=596):
	try:
		line = next(file).replace("\r\n","").split(",")
	except:
		break
	flag = False
	itemsToPop = []

	for i in range(0,len(W)):
		flag = dominates(W[i],line)
		if flag == True:
			break
	if flag:
		continue	
	else:
		i = 0
		while i < len(W):
			if dominates(line,W[i]):
				del W[i]
				i -= 1
			i += 1				
		W.append(line)
	k+=1

print "players: ", W,"\n","number of players: ",len(W)
