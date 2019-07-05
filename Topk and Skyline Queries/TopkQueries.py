import sys
import csv
import collections

all2017File = open("2017_ALL.csv","r")
filesToOpen = []
filesToSeek = []
bestScores = []
ids = {}
w = []
numberOfAccesses = 0
mainArray = []
count = 0
arrayList = []

def test(k,fileArray,bestScores):
	allFile = csv.reader(all2017File,delimiter = ',')
	next(allFile)
	players = {}
	for line in allFile:
		pointsOfPlayer = 0
		for i in range(len(fileArray)):
			player = line[0]
			pointsOfPlayer = pointsOfPlayer+float(line[int(fileArray[i])+2])/bestScores[i]
		players[player] = pointsOfPlayer
	players = collections.OrderedDict(sorted(players.items(),key=lambda kv: kv[1], reverse=True))
	print "Testing... Ids of top players: \n",players.keys()[0:k]

if len(sys.argv)!=3:
	print "wrong parameters! try again " 
	exit()

fileArray = sys.argv[1].replace('[',' ').replace(']',' ').replace(',',' ').split()
k = int(sys.argv[2])
fileNames = ["2017_TRB.csv","2017_AST.csv","2017_STL.csv","2017_BLK.csv","2017_PTS.csv"]

s_lists = [[] for i in xrange(len(fileArray))]

for i in range(0,len(fileArray)):
	fileId = open(fileNames[int(fileArray[i])-1],"r")
	filesToOpen.append(fileId)
	filesToSeek.append(fileId)

for i in range(0,len(filesToOpen)):
	filesToOpen[i] = csv.reader(filesToOpen[i],delimiter = ',')
	strn1 = filesToOpen[i].next() 
	bestScores.append(int(strn1[1]))
	filesToSeek[i].seek(0)

while(True):
	tempArray = []
	fub = {}
	flb = {}
	numberOfAccesses += 1
	for i in range(0,len(filesToOpen)):
		try:
			strn2 = next(filesToOpen[i])	
		except StopIteration:
			pass
		tempArray.append([int(strn2[0]),float(strn2[1])/float(bestScores[i]),i])
	mainArray.append(tempArray)

	for i in range(len(mainArray)):
		for j in range(len(mainArray[i])):
			if mainArray[i][j][0] in flb:
				flb[mainArray[i][j][0]] += mainArray[i][j][1] 
				ids[mainArray[i][j][0]].append(j)
			else:
				flb[mainArray[i][j][0]] = mainArray[i][j][1]
				ids[mainArray[i][j][0]] = [j]

	for i in range(0,len(mainArray)):
		for j in range(0,len(mainArray[i])):
			key = ids.keys()[j]
			value = ids[key]
			fub[mainArray[i][j][0]] = flb[mainArray[i][j][0]]
			for h in range(len(filesToOpen)):
				if h not in value:
					fub[mainArray[i][j][0]] = flb[mainArray[i][j][0]]  + mainArray[-1][j][1]

	flb = collections.OrderedDict(sorted(flb.items(),key=lambda kv: kv[1]))
	fub = collections.OrderedDict(sorted(fub.items(),key=lambda kv: kv[1]))

	while flb[flb.keys()[-1]] >= fub[fub.keys()[-1]]:
		delKey = flb.keys()[-1]
		w.append([flb.keys()[-1],flb[flb.keys()[-1]]])
		del fub[delKey]
		del flb[delKey]
		i = 0
		while i < len(mainArray):
			j = 0
			while j < len(mainArray[i]):	
				if mainArray[i][j][0] == delKey:
					del mainArray[i][j]
					i -= 1
					j -= 1
				j += 1
			i+=1
		
		if len(w) == k:
			print "Top players: ",w
			print "Number of Accesses: ", numberOfAccesses
			test(k,fileArray,bestScores)
			exit()
		if len(flb)==0:
			break
