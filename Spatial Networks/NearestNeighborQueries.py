import math,sys
dirFile = open("grid.dir","r")
grdFile = open("grid.grd","r")
data = open("Beijing_restaurants.txt","r")
grid = [[[] for _ in range(10)] for _ in range(10)]
dirData = []
grdData = []
distancesTest = []
dataRestaurants = []
readedCells = []
minX=0
minY=0
maxX=0
maxY=0
fileLine = 1
firstLineCounter = 0
priorityQueue = []

if len(sys.argv)!=4:
	print "wrong parameters! try again " 
	exit()

k = int(sys.argv[1])
q = [float(sys.argv[2]),float(sys.argv[3])]

#q = [39.765904,116.222121]

#read data from dir file to dirData
for line in dirFile:
	line = line.split()
	if firstLineCounter==0:
		minX = float(line[0])
		maxX = float(line[1])
		minY = float(line[2])
		maxY = float(line[3])
		firstLineCounter=1
	else:
		dirData.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])])

if q[0]<minX or q[0]>maxX or q[1]<minY or q[1]>maxY:
	print "wrong values! try again!"
	exit()

#read data from grd file to grdData
for line in grdFile:
	line = line.split()
	grdData.append([int(line[0]),float(line[1]),float(line[2])])

cellSizeX = (maxX-minX)/10
cellSizeY = (maxY-minY)/10

#grid
for xyid in grdData:
	for counterX in range(1,11):
		if (xyid[1]<=minX+(counterX*cellSizeX) and xyid[1]>=minX+((counterX-1)*cellSizeX) ):
			for counterY in range(1,11):
				if (xyid[2]<=minY+(counterY*cellSizeY) and xyid[2]>=minY+((counterY-1)*cellSizeY)):
					grid[counterX-1][counterY-1].append([counterX-1,counterY-1,xyid[1],xyid[2],xyid[0]])

#find cell o q points
for counterX in range(1,11):
	if (q[0]<=minX+(counterX*cellSizeX) and q[0]>=minX+((counterX-1)*cellSizeX) ):
		for counterY in range(1,11):
			if (q[1]<=minY+(counterY*cellSizeY) and q[1]>=minY+((counterY-1)*cellSizeY)):
				priorityQueue.append([counterX-1,counterY-1,0])

def generator():
	global priorityQueue
	
	for i in range(0,k):
		while priorityQueue[0][0]>=0 and priorityQueue[0][0]<=9:
			p0 = priorityQueue[0][0]
			p1 = priorityQueue[0][1]
			priorityQueue.pop(0)
			replaceCellWithValues(p0,p1)	
			addNeighborCells(p0,p1)
			calculateDistances()
			priorityQueue = sorted(priorityQueue,key=lambda x: x[2])
			if priorityQueue[0][2]==0:
				priorityQueue.pop(0) 		

		closestNeighbor = priorityQueue[0]
		priorityQueue.pop(0) 
		yield closestNeighbor

def replaceCellWithValues(p0,p1):
	for i in range(0,len(grid[p0][p1])):
		priorityQueue.append([grid[p0][p1][i][2],grid[p0][p1][i][3],0])

def addNeighborCells(p0,p1):
	global priorityQueue
	neighbors = []
	for i in range(0,len(dirData)):
		if math.fabs(dirData[i][0]-p0)<2 and math.fabs(dirData[i][1]-p1)<2:
			if [dirData[i][0],dirData[i][1]] not in readedCells:
				readedCells.append([dirData[i][0],dirData[i][1]])
				priorityQueue.append([dirData[i][0],dirData[i][1],0])

def calculateDistances():
	global priorityQueue,cellSizeX,cellSizeY,minX,minY
	for i in range(len(priorityQueue)):
		if priorityQueue[i][0]>=0 and priorityQueue[i][0]<=9:
			x = minX+(float(priorityQueue[i][0])*cellSizeX)
			y = minY+(float(priorityQueue[i][1])*cellSizeY)
			distance = mindist(x,y)
			priorityQueue[i][2] = distance
		else:
			x = float(priorityQueue[i][0])
			y = float(priorityQueue[i][1])
			distance = mindist(x,y)
			priorityQueue[i][2] = distance

def mindist(x,y):
	return math.sqrt(((x-q[0])**2+(y-q[1])**2))
	 
def main(objectGenerator):
	for closestNeighbors in objectGenerator:
		print closestNeighbors

def test():
	global fileLine
	next(data)
	for line in data:
		line = line.split()
		line.append(fileLine)
		line[0] = float(line[0])
		line[1] = float(line[1])
		dataRestaurants.append(line)
		fileLine+=1

	for i in range(0,len(dataRestaurants)):
		distance = mindist(dataRestaurants[i][0],dataRestaurants[i][1])
		if distance!=0:
			distancesTest.append(distance)

	distancesTest.sort()
	#print distancesTest[0:k]
	return 0

def closeFiles():
	dirFile.close()
	grdFile.close()
	data.close()

main(generator())
if test()==0:
	print "\nTested : Results are same\n"
else:
	print "\nTested : Results are not same\n"

print "Readed cells: ",readedCells
closeFiles()