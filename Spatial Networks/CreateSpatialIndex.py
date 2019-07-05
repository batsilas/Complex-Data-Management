data = open("Beijing_restaurants.txt","r")
grdFile = open("grid.grd","w")
dirFile = open("grid.dir","w")
x = []
y = []
dataArray = []
fileLine = 1
grid = [[[] for _ in range(10)] for _ in range(10)]
column3InDir = [[[] for _ in range(10)] for _ in range(10)]
grdDataTest = []
dirDataTest = []
next(data)

def main():
	global fileLine
	#read data file lines in dataArray
	for line in data:
		line = line.split(' ')
		line.append(fileLine)
		dataArray.append(line)
		fileLine+=1

	#find max and min
	for i in range(1,len(dataArray)):
		x.append(float(dataArray[i][0]))
		y.append(float(dataArray[i][1]))

	maxX = max(x)
	minX = min(x)
	maxY = max(y)
	minY = min(y)

	cellSizeX = (maxX-minX)/10
	cellSizeY = (maxY-minY)/10

	#fill cells in grid with right values
	for xycoo in dataArray:
		for counterX in range(1,11):
			if (float(xycoo[0])<=minX+(counterX*cellSizeX) and float(xycoo[0])>=minX+((counterX-1)*cellSizeX) ):
				for counterY in range(1,11):
					if (float(xycoo[1])<=minY+(counterY*cellSizeY) and float(xycoo[1])>=minY+((counterY-1)*cellSizeY)):
						grid[counterX-1][counterY-1].append(xycoo)

	#write grd file
	for row in range(0,10):
		for column in range(0,len(grid[row])):
			column3InDir[row][column].append(grdFile.tell())
			for xycoo in range(0,len(grid[row][column])):
				grdFile.write(str(grid[row][column][xycoo][2])+" "+str(grid[row][column][xycoo][0])+" "+str(grid[row][column][xycoo][1]))
			
	#write dir file
	dirFile.write(str(minX)+" "+str(maxX)+" "+str(minY)+" "+str(maxY)+"\n")
	for i in range(10):
		for j in range(10):
			dirFile.write(str(i)+" "+str(j)+" "+str(column3InDir[i][j][0])+" "+str(len(grid[i][j]))+"\n")

def closeFiles():
	grdFile.close()
	dirFile.close()
	data.close()

def test():
	global result
	temp = 0
	dirFile = open("grid.dir","r")
	grdFile = open("grid.grd","r")
	data = open("Beijing_restaurants.txt","r")
	next(dirFile)

	for line in grdFile:
		line = line.split()
		grdDataTest.append(int(line[0]))

	for line in dirFile:
		line = line.split()
		dirDataTest.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])])

	for cols in range(0,10):
		for rows in range(0,10):
			if(len(grid[cols][rows])!=dirDataTest[temp][3]):
				print "Tested : Results are not same "
				closeFiles()
				exit()
			temp = temp + 1
	
	for i in range(0,len(dataArray)):
		if dataArray[i][2] not in grdDataTest:
			print "Tested : Results are not same "
			closeFiles()
			exit()

	print "Tested : Results are same "

main()
closeFiles()
test()
closeFiles()