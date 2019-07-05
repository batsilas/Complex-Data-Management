identity = 0

def scan(inputFile):
    next(inputFile)
    for line in inputFile:
        line = line.split("\t") 
        yield line
        
def mj(firstFileLine,secondFileLine,id1,id2):
    global identity,mergeFile,mergeFileFinal,mergeFile2,basicFile,ratingFile,principalFile
    previousLine1 = ["0","0","0","0"]
    previousLine2 = ["0","0","0","0"]
    secondLine = ["0","0","0","0"]
    for firstLine in firstFileLine:
        
    	if (previousLine0[0] == firstLine[0] and identity==1):
            mergeFile.write(str(firstLine[0])+"\t" + str(firstLine[id1])+"\t" +str(previousLine0[id2[0]])+"\t"+str(previousLine0[id2[1]])+ "\n")

        if (previousLine1[0] == firstLine[0] and identity==2):
            mergeFile.write(str(firstLine[0])+"\t" + str(firstLine[id1])+"\t" +str(previousLine1[id2])+ "\n")

        if (previousLine2[0] == firstLine[0] and identity==3):
            mergeFileFinal.write(str(firstLine[0])+"\t" +str(previousLine2[id2[0]])+"\t"+str(previousLine2[id2[1]])+"\t"+str(firstLine[id1])+ "\n")

        if(firstLine[0]<secondLine[0]):
            continue 
        else:
            for secondLine in secondFileLine: 
                if(identity==1):
                    if(firstLine[0]>secondLine[0]):
                        continue
                    elif(firstLine[0]==secondLine[0]):
                        mergeFile.write(str(firstLine[0])+"\t" + str(firstLine[id1])+"\t" +str(secondLine[id2[0]])+"\t"+str(secondLine[id2[1]])+ "\n")
                        continue
                    else:
                    	previousLine0 = secondLine
                        break
                elif(identity==2):
                    if(firstLine[0]>secondLine[0]):
                        continue
                    elif(firstLine[0]==secondLine[0]):
                        mergeFile.write(str(firstLine[0])+"\t" + str(firstLine[id1])+"\t" +str(secondLine[id2])+ "\n")
                        continue
                    else:
                        previousLine1 = secondLine
                        break
                else:
                    if(firstLine[0]>secondLine[0]):
                        continue
                    elif(firstLine[0]==secondLine[0]):
                        mergeFileFinal.write(str(firstLine[0])+"\t" +str(secondLine[id2[0]])+"\t"+str(secondLine[id2[1]])+"\t"+str(firstLine[id1])+ "\n")
                        continue
                    else:
                        previousLine2 = secondLine
                        break
   
    identity += 1
    mergeFile.close()
    if(identity>2):
        mergeFile2 = open("mergeFile2Second.txt")
        return scan(mergeFile2)

def firstQuestion():
    global identity,mergeFile,basicFile,ratingFile
    identity = 1 
    mergeFile = open("mergeFile2First.txt","w+")
    basicFile =  open("title.basics.tsv")
    ratingFile = open("title.ratings.tsv")
    mergeFile.write("titleId\tprimaryTitle\taverageRating\tnumVotes\n")
    mj(scan(basicFile),scan(ratingFile),2,[1,2])
    basicFile.close()
    ratingFile.close()
    mergeFile.close()

def secondQuestion():
    global identity,mergeFile,basicFile,principalFile
    identity = 2
    mergeFile = open("mergeFile2Second.txt","w+")
    basicFile =  open("title.basics.tsv")
    principalFile = open("title.principals.tsv") 
    mergeFile.write("titleId\tprimaryTitle\tnconst\n")
    mj(scan(basicFile),scan(principalFile),2,2)
    basicFile.close()
    principalFile.close()
    mergeFile.close()

def thrirdQuestion():
    global identity,mergeFile,mergeFileFinal,mergeFile2,basicFile,ratingFile,principalFile
    identity = 2
    mergeFile = open("mergeFile2Second.txt","w+")
    mergeFileFinal = open("mergeFile2Third.txt","w+")                       
    basicFile =  open("title.basics.tsv")
    ratingFile = open("title.ratings.tsv")
    principalFile = open("title.principals.tsv")
    mergeFile.write("titleId\tprimaryTitle\tnconst\n")
    mergeFileFinal.write("titleId\tprimaryTitle\ttnconst\taverageRating\n")
    mj(scan(ratingFile),mj(scan(basicFile),scan(principalFile),2,2),1,[1,2])  
    basicFile.close()
    ratingFile.close()
    principalFile.close()
    mergeFileFinal.close()
    mergeFile2.close()


question = input("Select question (a/b/c): ")
while(question>"c"):
	question = input("Invalid letter. Choose a,b or c: ")
if (question=="a"):
	firstQuestion()
elif(question=="b"):
	secondQuestion()
else:
	thrirdQuestion()

