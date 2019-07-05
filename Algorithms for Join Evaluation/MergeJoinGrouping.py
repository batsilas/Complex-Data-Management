mergeFile = open("mergeFile1.txt","w+")
basicFile = open("title.basics.tsv")
akasFile = open("title.akas.tsv")


def scan(inputFile):
    next(inputFile)
    for line in inputFile:
        line = line.split("\t") 
        yield line

def combineSameNames(languages):
    languages.sort()
    for items in range(0,len(languages)):
        if items < len(languages)-1:
            if languages[items][0] == languages[items+1][0]:
                languages[items][1].append(languages[items+1][1][0])
                del languages[items+1]
    return languages 

def writelines(languages):
    for i in range(0,len(languages)):
        string =" "
        for j in range(0,2):
            string += str(languages[i][j])
        mergeFile.write(string + "\t")
    mergeFile.write("\n")

def mj(basicFileLine,akasFileLine):
    previousLine = ["0","0","0","0"] 
    mergeFile.write("titleId\tprimaryTitle\ttitle (regions)\n")
    for nextBasicLine in basicFileLine:
        languages = []

        if(previousLine[0]==nextBasicLine[0]):
            languages.append([previousLine[2],[previousLine[3]]])
            previousLine = ["0","0","0","0"] 

        if (nextBasicLine[0]<previousLine[0]):
            continue
        else:
            for nextAkasLine in akasFileLine:
                if nextBasicLine[0]<nextAkasLine[0]:
                    break 
                else:
                    languages.append([nextAkasLine[2],[nextAkasLine[3]]])
                
            previousLine = nextAkasLine        
            languages = combineSameNames(languages)
            mergeFile.write(nextBasicLine[0] + "\t" + nextBasicLine[2] + "\t")

            writelines(languages)
            

mj(scan(basicFile),scan(akasFile))

basicFile.close()
akasFile.close()
mergeFile.close()