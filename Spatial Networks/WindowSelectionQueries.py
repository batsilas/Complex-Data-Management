import sys

data = open("Beijing_restaurants.txt","r")
dirFile = open("grid.dir","r")
grdFile = open("grid.grd","r")
outputFile = open("output.txt","w")
testFile = open("outputTest","w")
dirData = []
firstLineCounter = 0
dataRestaurants = []
fileLine = 1
minX=0
minY=0
maxX=0
maxY=0
fullIn = []
partIn = []
out = []
outputArray = []
testArray = []
flagEqual = 1
next(data)

if len(sys.argv)!=5:
	print "wrong parameters! try again " 
	exit()
#W = [minX,minY,(minX+((2)*cellSizeX))+(cellSizeX/2),(minY+((2)*cellSizeY))+(cellSizeY/2)]
W = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])]

def main():
	global firstLineCounter,W
	#read dir data in dirData and save max and min
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

	cellSizeX = (maxX-minX)/10
	cellSizeY = (maxY-minY)/10

	#find cells which are full in or part in W area
	for counterX in range(1,11):
		if (W[0]<=minX+((counterX-1)*cellSizeX) and W[1]>=minX+(counterX*cellSizeX)):
			for counterY in range(1,11):
				if (W[2]<=minY+((counterY-1)*cellSizeY) and W[3]>=minY+(counterY*cellSizeY)):
					fullIn.append([counterX-1,counterY-1])
				elif (W[2]>minY+(counterY*cellSizeY) or W[3]<minY+((counterY-1)*cellSizeY)):
					out.append([counterX-1,counterY-1])
				else:
					partIn.append([counterX-1,counterY-1])
		elif(W[0]>minX+(counterX*cellSizeX) or W[1]<minX+((counterX-1)*cellSizeX)):
			for counterY in range(1,11):
				out.append([counterX-1,counterY-1])	
		else:
			for counterY in range(1,11):
				if (W[2]<=minY+((counterY-1)*cellSizeY) and W[3]>=minY+(counterY*cellSizeY)):
					partIn.append([counterX-1,counterY-1])
				elif (W[2]>minY+(counterY*cellSizeY) or W[3]<minY+((counterY-1)*cellSizeY)):
					out.append([counterX-1,counterY-1])
				else:
					partIn.append([counterX-1,counterY-1])

	#print fullIn
	#print partIn
	print "Readed "+str(len(fullIn))+ " cells which were full in and "+str(len(partIn))+" part in!\n" 
	
	#join full in and part in arrays
	fullAndPart = fullIn+partIn
	fullAndPart.sort()
	
	#write to output file points that are in W area
	if len(fullAndPart)!=0:
		for i in range(0,len(fullAndPart)):
			for j in range(0,len(dirData)):
				if fullAndPart[i] in fullIn:
					if(fullAndPart[i][0]==dirData[j][0] and fullAndPart[i][1]==dirData[j][1]):
						grdFile.seek(dirData[j][2])
						for j in range(0,dirData[j][3]):
							line = grdFile.readline()
							lineTemp = line.split()
							outputArray.append(float(lineTemp[0])) 
							outputFile.write(line)
				elif fullAndPart[i] in partIn:
					if(fullAndPart[i][0]==dirData[j][0] and fullAndPart[i][1]==dirData[j][1]):
						grdFile.seek(dirData[j][2])
						for j in range(0,dirData[j][3]):
							line = grdFile.readline() 
							lineTemp = line.split()
							if float(lineTemp[1])>=W[0] and float(lineTemp[1])<=W[1] and float(lineTemp[2])>=W[2] and float(lineTemp[2])<=W[3]:
								outputArray.append(float(lineTemp[0]))
								outputFile.write(line)

def test():
	global fileLine
	#read data file in dataRestaurants using for testing
	for line in data:
		line = line.split()
		line.append(fileLine)
		line[0] = float(line[0])
		line[1] = float(line[1])
		dataRestaurants.append(line)
		fileLine+=1

	#test if output array is equal to test array
	for line in dataRestaurants:
		if float(line[0])>=W[0] and float(line[0])<=W[1] and float(line[1])>=W[2] and float(line[1])<=W[3]:
			testArray.append(float(line[2]))
			testFile.write(str(line[2]) + " "+str(line[0]) + " "+str(line[1]) + "\n")

	for i in range(len(outputArray)):
		if outputArray[i] not in testArray:
			print "Tested : Results are not same"
			exit()
	print "Tested : Results are same"

def closeFiles():
	dirFile.close()
	grdFile.close()
	testFile.close()
	outputFile.close()
	data.close()

main()
test()
closeFiles()
