#!/usr/bin/python
from pulp import *
import xlrd
import math

def sortDistanceMatrix(dm):
    firstRow = dm.pop(0)
    firstRow.pop(0)
    firstRow.pop()
    lastRow = dm.pop()
    dm.sort(key=lambda x: x[0])
    
    dm.append(lastRow)
    for row in dm:
        row.pop(0)
    lastCol = []
    for row in dm:
        lastCol.append(row.pop())
    for i in range(len(firstRow)):
        firstRow[i] = (firstRow[i], i)
    firstRow.sort(key=lambda x: x[0])
    for i in range(len(dm)):
        row = dm[i]
        rowLength = len(row)
        rowCopy = []
        for j in range(rowLength):
            rowCopy.append(row[j])
        for j in range(rowLength):
            row[j] = rowCopy[firstRow[j][1]]
    for i, row in enumerate(dm):
        row.append(lastCol[i])

def solve(window,w,c,districtList):
    """
        - w: warehouse name
        - c: cost matrix
        - districtList: includes (district name, distance matrix, demand matrix)
        """
    results = []
    (TRUCK_SIZES, FIXED_COSTS, DISTANCE_RANGES, COSTMAT) = readCostMatrix(c)
    for (district_name, distance_matrix, demand_matrix) in districtList:
        DISTRICT = district_name
        (LOCATIONS, DISTMAT, nrow_distM, ncol_distM) = readDistMatrix(distance_matrix)
        (DEMANDMAT,nrow_demandM) = readDemandMatrix(demand_matrix)
        
        """
        check if all the possible error caused by user
            1. The length of rows in distance matrix and demand matrix must be equal.
            2. In the distance matrix, the number of rows and cols must be equal.
        """
        if (nrow_demandM != (nrow_distM-1)):
            return "In distance matrix and demand matrix excel spreadsheets, please make sure that the number of sites must be matched!"
        if (nrow_distM != ncol_distM):
            return ("In distance matrix excel spreadsheet, please make sure the number of rows and columns are equal!")
    
        # run LP solver
        result = runLPSolver(LOCATIONS,TRUCK_SIZES, DISTANCE_RANGES, DISTMAT, FIXED_COSTS, COSTMAT,DEMANDMAT,DISTRICT)
        results = results + result
    window.outputTab.showtable(results,w)
#display(w, results)
#return results
## success return None
## fail return error message

def sort_table(table, col=0):
    return sorted(table, key=operator.itemgetter(col))

def readDistMatrix(distanceFile):
    """
        - open and read an Excel file for distance matrix
        - @param distanceFile: Distance matrix file location
        - @return new_distMatrix: Distance matrix without the all title of row and col
        """
    book = xlrd.open_workbook(distanceFile)
    dist_sheet = book.sheet_by_index(0)
    #dist_sheet = book.sheet_by_name('Distance_Matrix')
    nrow_distM = dist_sheet.nrows
    ncol_distM = dist_sheet.ncols
    distMatrix = [[0 for col in range(0,ncol_distM)] for row in range(0,nrow_distM)]
    #sorted_distM = []
    new_distMatrix = [[0 for col in range(0,ncol_distM-1)] for row in range(0,nrow_distM-1)]
    LOCATIONS = [0 for i in range(0,ncol_distM-2)]
    
    #if (nrow_distM != ncol_distM):
    #    return ("In distance matrix, please make sure the number of rows and columns are equal!")
    
    # Store the original data
    for row in range(0,nrow_distM):
        dist_sheet.row_values(row)
        for col in range(0,ncol_distM):
            distMatrix[row][col] = dist_sheet.cell(row,col).value
    #print(distMatrix)

    # In the distance matrix, the number of rows and cols must be equal (ERROR CHECK).
    #for i in range(1,nrow_distM):
    #    if (distMatrix[0][i] != distMatrix[i][0]):
    #        return ("In distance matrix, please make sure that all the names in rows and columns are matched")

    # Store the list of locations in array "LOCATIONS"
    for i in range(1,ncol_distM-1):
        LOCATIONS[i-1] = str(distMatrix[0][i])

    # Sort the LOCATIONAS and distMatrix by alphabetical order
    LOCATIONS.sort()
    sortDistanceMatrix(distMatrix)


    return(LOCATIONS, distMatrix, nrow_distM, ncol_distM)

def readCostMatrix(costFile):
    """
        - open and read a Cost Matrix from given path
        """
    book = xlrd.open_workbook(costFile)
    cost_sheet = book.sheet_by_index(0)
    #cost_sheet = book.sheet_by_name('Cost_Matrix')
    nrow_costM = cost_sheet.nrows
    ncol_costM = cost_sheet.ncols
    costMatrix = [[0 for col in range(0,ncol_costM)] for row in range(0,nrow_costM)]
    new_costMatrix = [[0 for col in range(0,ncol_costM-2)] for row in range(0,nrow_costM-1)]
    DISTANCE_RANGES = [0 for i in range(0,ncol_costM-2)]
    TRUCK_SIZES = [0 for i in range(nrow_costM-1)]
    FIXED_COSTS = [0 for i in range(nrow_costM-1)]
    # Store the original data
    for row in range(0,nrow_costM):
        cost_sheet.row_values(row)
        for col in range(0,ncol_costM):
            costMatrix[row][col] = cost_sheet.cell(row,col).value
    # print costMatrix
    # Store the list of truck sizes
    for row in range(1,nrow_costM):
        TRUCK_SIZES[row-1] = costMatrix[row][0]
    #print TRUCK_SIZES
    # Store the list of min cost per truck size
    for row in range(1,nrow_costM):
        FIXED_COSTS[row-1] = costMatrix[row][ncol_costM-1]
    #print FIXED_COSTS
    # Store the DISTANCE_RANGES
    for col in range(1,ncol_costM-1):
        DISTANCE_RANGES[col-1] = costMatrix[0][col]
    #print DISTANCE_RANGES
    # Store the cost matrix without title
    for row in range(1,nrow_costM):
        for col in range(1,ncol_costM-1):
            new_costMatrix[row-1][col-1] = float(costMatrix[row][col])
    #print new_costMatrix
    #print(TRUCK_SIZES, FIXED_COSTS, DISTANCE_RANGES, new_costMatrix)
    return(TRUCK_SIZES, FIXED_COSTS, DISTANCE_RANGES, new_costMatrix)

def readDemandMatrix(demandFile):
    """
        - open and read a Demand Matrix from given path
        """
    book = xlrd.open_workbook(demandFile)
    demand_sheet = book.sheet_by_index(0)
    #demand_sheet = book.sheet_by_name('Demand_Matrix')
    nrow_demandM = demand_sheet.nrows
    ncol_demandM = demand_sheet.ncols
    demandMatrix = [[0 for col in range(0,ncol_demandM)] for row in range(0,nrow_demandM)]
    for row in range(0,nrow_demandM):
        demand_sheet.row_values(row)
        for col in range(0,ncol_demandM):
            demandMatrix[row][col] = demand_sheet.cell(row,col).value
    del demandMatrix[0]
    demandMatrix.sort()
    #print (demandMatrix)
    new_demandMatrix = [0 for row in range(0,nrow_demandM-1)]
    for row in range(0,nrow_demandM-1):
        new_demandMatrix[row] = demandMatrix[row][1]

    #print (new_demandMatrix)
    return(new_demandMatrix, nrow_demandM)

def runLPSolver(LOCATIONS,TRUCK_SIZES, DISTANCE_RANGES, DISTMAT, FIXED_COSTS, COSTMAT,DEMANDMAT,DISTRICT):
    
    # Create list of locations
    location = [0 for i in LOCATIONS]
    for i in range(0,len(LOCATIONS)):
        location[i]=LOCATIONS[i]

    last = len(location)

    # Create list of truck sizes
    truckSize = [0 for m in TRUCK_SIZES]
    for m in range(0,len(TRUCK_SIZES)):
        truckSize[m]=TRUCK_SIZES[m]
    # Create Upper and Lower limits of distances denominations
    upperDist=[0 for n in DISTANCE_RANGES]
    for n in range(0,len(DISTANCE_RANGES)):
        upperDist[n]=DISTANCE_RANGES[n]

    lowerDist=[0 for n in DISTANCE_RANGES]
    for n in range(1,len(DISTANCE_RANGES)):
        lowerDist[n]=upperDist[n-1]

    # Create cost matrix
    costMatrix = [[0 for n in upperDist] for m in truckSize]
    # Assign cost matrix to c(m,n)
    # Read some csv assign
    for m in range(0,len(truckSize)):
        for n in range(0,len(upperDist)):
            costMatrix[m][n]=COSTMAT[m][n]

    # Create distance matrix
    distanceMatrix = [[0 for i in range(0,len(location)+1)] for j in range(0,len(location)+1)]
    for i in range(0,len(location)+1):
        for j in range(0,len(location)+1):
            distanceMatrix[i][j]=DISTMAT[i][j]
    # print (distanceMatrix)
    # Create demand for each location refer to computer plant example
    demand = [0 for i in location]
    for i in range(0,len(location)):
        demand[i]=DEMANDMAT[i]

    # Create routes distances
    routeDist = [[0 for i in range(0,len(location))] for j in range(0,len(location))]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            if (i==j):
                routeDist[i][j] = distanceMatrix[i][last]*2
            else:
                routeDist[i][j] = distanceMatrix[i][last]+distanceMatrix[j][last]+distanceMatrix[i][j]


    # Create demand matrix
    demandMat = [[0 for i in range(0,len(location))] for j in range(0,len(location))]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            if (i==j):
                demandMat[i][j]=demand[i]
            else:
                demandMat[i][j]=demand[i]+demand[j]

    # Create list of residual distance

    resDist = [[[0 for n in upperDist] for j in location]for i in location]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for n in range(0,len(upperDist)):
                if (routeDist[i][j] >= lowerDist[n]):
                    resDist[i][j][n] = routeDist[i][j] - lowerDist[n]
                else:
                    resDist[i][j][n] = 0

    # Create Distance give distance brackets
    distBrackets = [[[0 for n in upperDist] for j in location]for i in location]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for n in range(0,len(upperDist)):
                distBrackets[i][j][n] = lowerDist[n] + resDist[i][j][n]

    # Create fixed costs
    fixedC = [0 for m in truckSize]
    for m in range(0,len(truckSize)):
        fixedC[m]=FIXED_COSTS[m]

    # Create the prob variable
    prob=LpProblem("TheOneAcre",LpMinimize)
        
    c = [[[[0 for n in upperDist]for m in truckSize] for j in location]for i in location]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for m in range(0,len(truckSize)):
                for n in range(0,len(upperDist)):
                    if(costMatrix[m][n]*distBrackets[i][j][n]*demandMat[i][j]>=fixedC[m]):
                        c[i][j][m][n]=costMatrix[m][n]*distBrackets[i][j][n]*demandMat[i][j]
                    else:
                        c[i][j][m][n] = fixedC[m] + 0.1*n

    # Decision Variable
    # x1 = LpVariable("name",<lowerbound or None>,<upperbound or None>,<type LpInteger or LpContinuous>)
    x = [[[[0 for n in upperDist]for m in truckSize] for j in location]for i in location]
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for m in range(0,len(truckSize)):
                for n in range(0,len(upperDist)):
                    x[i][j][m][n]=LpVariable("x"+str(i)+"-"+str(j)+"-"+str(m)+"-"+str(n), 0, 1, LpBinary)


    # Add objective function always
    prob+= lpSum(c[i][j][m][n]*x[i][j][m][n] for i in range(0,len(location)) for j in range(i,len(location)) for m in range(0,len(truckSize)) for n in range(0,len(upperDist))), "Objective Function"
        
    # Next we add constraints
    
    # A farm must be visited at one and only one truck
    for i in range(0,len(location)):
        prob+= lpSum(x[i][j][m][n] for j in range(0,len(location)) for m in range(0,len(truckSize)) for n in range(0,len(upperDist))) ==1, "Route Allocation Row" +str(i)
    for j in range(0,len(location)):
        prob+= lpSum(x[i][j][m][n] for i in range(0,len(location)) for m in range(0,len(truckSize)) for n in range(0,len(upperDist))) ==1, "Route Allocation Col" +str(j)
    
    # X must be symmetrical
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for m in range(0,len(truckSize)):
                for n in range(0,len(upperDist)):
                    prob+= x[i][j][m][n] == x[j][i][m][n] , "Symmetrical Property" +str(i) + " "+str(j) + " "+str(m) + " "+str(n)

    # Distances constraint
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for n in range(0,len(upperDist)):
                prob += upperDist[n] * lpSum(x[i][j][m][n] for m in range(0,len(truckSize))) >= distBrackets[i][j][n]* lpSum(x[i][j][m][n] for m in range(0,len(truckSize))), "Distance Constraint" +str(i) + " " +str(j) + " " +str(n)

    # Weight constraint
    for i in range(0,len(location)):
        for j in range(0,len(location)):
            for m in range(0,len(truckSize)):
                prob += truckSize[m] * lpSum(x[i][j][m][n] for n in range(0,len(upperDist))) >= demandMat[i][j]*lpSum(x[i][j][m][n] for n in range(0,len(upperDist))) , "Weight Constraint" +str(i) + " "+str(j) + " " +str(m)

    #print ("Done Adding")
    # a .lp file needs to be created for processing
    prob.writeLP("OneAcre.lp")
    prob.solve()
    
    # Extract decision variables that are 1
    
    list = []
    
    for i in range(0,len(location)):
        for j in range(i,len(location)):
            for m in range(0,len(truckSize)):
                for n in range(0,len(upperDist)):
                    if((x[i][j][m][n]).varValue == 1.0):
                        vec = [i,j,m,n]
                        list.append(vec)

    #print list

    #print "Total Cost = $", value(prob.objective)

    numRow = len(list)
    numCol = 9
    #print (routeDist)
    #print(distanceMatrix[0][last])
    #print(distanceMatrix[9][last])
    #print(distanceMatrix[0][9])
    # Create the output array
    
    if (LpStatus[prob.status]=="Optimal"):
        output=[[0 for col in range(0,numCol)]for row in range(0,numRow)]
        for row in range(0,numRow):
            output[row][0] = DISTRICT
            if (list[row][0]==list[row][1]):
                output[row][1]= location[list[row][0]]
                output[row][2]= "-"
            else:
                output[row][1]= location[list[row][0]]
                output[row][2]= location[list[row][1]]
        
            output[row][3]= routeDist[list[row][0]][list[row][1]]
            output[row][4]= distBrackets[list[row][0]][list[row][1]][list[row][3]]
            output[row][5]= demandMat[list[row][0]][list[row][1]]
            output[row][6]= truckSize[list[row][2]]
            output[row][7]= math.floor(c[list[row][0]][list[row][1]][list[row][2]][list[row][3]])
            
            if (output[row][3]<output[row][4]):
                output[row][8]= c[list[row][0]][list[row][1]][list[row][2]][list[row][3]-1]
            else:
                output[row][8] = output[row][7]
    else:
        output=[[0 for col in range(0,numCol)]]
        output[0][0] = DISTRICT
        output[0][1] = "Infeasible"
    
    return output

