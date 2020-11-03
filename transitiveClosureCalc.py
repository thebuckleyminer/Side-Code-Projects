#To customise all you have to do is make sure to add up to xn rows and make sure there are n entries in each list for each row.
#Then on line 8 and 9 just uncomment, and/or add the variables for the rows you added or took away.
x0 = [0,1,0,0]
x1 = [0,0,1,0]
x2 = [0,1,0,0]
x3 = [1,1,0,0]

matrixX = [x0,x1,x2,x3]#,x4,x5,x6,x7,x8,x9,x10.....]
matrixY = [x0,x1,x2,x3]#,x4,x5,x6,x7,x8,x9,x10.....]

def yColumns(y):
    """Turns the input of rows into columns instead"""
    outputList=[]
    tempList=[]
    for i in range(len(y)):
        for j in y:
            tempList.append(j[i])
        outputList.append(tempList)
        tempList = []
    return outputList

def dotProd(xRow, yCol):
    """Returns the dot product of a row and column"""
    total = 0
    for i in range(len(xRow)):
        total += xRow[i] * yCol[i]
    return total

def binaryMatrixMult(xMAT,yColMAT):
    """Does the binary Matrix Multiplication"""
    result = []
    temp = []
    for i in range(len(xMAT)):
        for j in range(len(yColMAT)):
            binaryTempNumber = dotProd(xMAT[i], yColMAT[j])
            if binaryTempNumber >= 1:
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
        temp = []
    return result

def binaryTransitiveClosure():
    """Calculates all of the G through G+"""
    fullList = [matrixX]
    fullList.append(binaryMatrixMult(matrixX,yColumns(matrixY)))
    for i in range(len(matrixX)-2):
        fullList.append(binaryMatrixMult(matrixX,yColumns(fullList[-1])))
    return fullList

def printMatrix(matNestedList, nestedSize = 1):
    """Makes printing out cleaner"""
    if nestedSize == 1:        
        for i in matNestedList:
            print(i)
    if nestedSize == 2:
        counter = 1
        for i in matNestedList:
            print("G"+str(counter)+" (Walk of length "+str(counter)+")")
            counter +=1
            for j in i:
                print(j)
            print()

def emptyMatrixMaker(NumOfRows):
    """Makes an empty list for Binary Addition for final Transitive closure"""
    outputList = []
    row=[]
    for i in range(NumOfRows):
        for j in range(NumOfRows):
            row.append(0)
        outputList.append(row)
        row = []
    return outputList

transitiveMatrix = emptyMatrixMaker(len(matrixX))  

fullList = binaryTransitiveClosure()
iteratorNumber = len(fullList)
for i in range(iteratorNumber):
    for j in range(iteratorNumber):
        for k in range(iteratorNumber):
            if fullList[i][j][k] == 1:
                transitiveMatrix[j][k] = 1

"""The final print output"""
printMatrix(binaryTransitiveClosure(),2)
print("G+ (The Transitive Closure of G)")
printMatrix(transitiveMatrix)
