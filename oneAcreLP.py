#!/usr/bin/python
from pulp import *
import xlrd

################## Construct distance matrix ##################
"""
    - open and read an Excel file for distance matrix
    - the python code and excel file should be located in same path/directory
    """
book = xlrd.open_workbook("OneAcreInputs.xlsx")
dist_sheet = book.sheet_by_index(0)
nrow_distM = dist_sheet.nrows
ncol_distM = dist_sheet.ncols
distMatrix = [[0 for col in range(0,ncol_distM)] for row in range(0,nrow_distM)]
new_distMatrix = [[0 for col in range(0,ncol_distM-1)] for row in range(0,nrow_distM-1)]
LOCATIONS = [0 for i in range(0,ncol_distM-2)]
# Store the original data
for row in range(0,nrow_distM):
    dist_sheet.row_values(row)
    for col in range(0,ncol_distM):
        distMatrix[row][col] = dist_sheet.cell(row,col).value
# Store the list of locations in array "LOCATIONS"
for i in range(1,ncol_distM-1):
    LOCATIONS[i-1] = str(distMatrix[0][i])
#print(LOCATIONS)
# Create the distance matrix without the title
for row in range(1,nrow_distM):
    for col in range(1,ncol_distM):
        new_distMatrix[row-1][col-1] = float(distMatrix[row][col])
#print distMatrix
#print new_distMatrix
################## End ##########################################
################## Construct cost distance based on new policy ####
cost_sheet = book.sheet_by_index(1)
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
################## End ##########################################
################## Construct demand matrix ######################
demand_sheet = book.sheet_by_index(2)
nrow_demandM = demand_sheet.nrows
ncol_demandM = demand_sheet.ncols
demandMatrix = [[0 for col in range(0,ncol_demandM)] for row in range(0,nrow_demandM)]
for row in range(0,nrow_demandM):
    demand_sheet.row_values(row)
    for col in range(0,ncol_demandM):
        demandMatrix[row][col] = demand_sheet.cell(row,col).value
#print demandMatrix
new_demandMatrix = [0 for row in range(0,nrow_demandM-1)]
for row in range(1,nrow_demandM):
    new_demandMatrix[row-1] = demandMatrix[row][1]
#print new_demandMatrix
################## End ##########################################
################## Create decision Variable #####################
cost_sheet = book.sheet_by_index(1)
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
demand_sheet = book.sheet_by_index(2)
nrow_demandM = demand_sheet.nrows
ncol_demandM = demand_sheet.ncols

demandMatrix = [[0 for col in range(0,ncol_demandM)] for row in range(0,nrow_demandM)]
for row in range(0,nrow_demandM):
    demand_sheet.row_values(row)
    for col in range(0,ncol_demandM):
        demandMatrix[row][col] = demand_sheet.cell(row,col).value
#print demandMatrix
new_demandMatrix = [0 for row in range(0,nrow_demandM-1)]
for row in range(1,nrow_demandM):
    new_demandMatrix[row-1] = demandMatrix[row][1]
#print new_demandMatrix
################## End ##########################################
################## Create decision Variable #####################

################## Creation of LP starts here ###################
# Creates a list of locations including warehouse
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
        costMatrix[m][n]=new_costMatrix[m][n]

# Create distance matrix
distanceMatrix = [[0 for i in range(0,len(location)+1)] for j in range(0,len(location)+1)]
for i in range(0,len(location)+1):
    for j in range(0,len(location)+1):
        distanceMatrix[i][j]=new_distMatrix[i][j]
# print (distanceMatrix)
# Create demand for each location refer to computer plant example
demand = [5 for i in location]
for i in range(0,len(new_demandMatrix)):
    demand[i]=new_demandMatrix[i]

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
                if(costMatrix[m][n]*distBrackets[i][j][n]*truckSize[m]>fixedC[m]):
                    c[i][j][m][n]=costMatrix[m][n]*distBrackets[i][j][n]*truckSize[m]
                else:
                    c[i][j][m][n] = fixedC[m]

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
    prob+= lpSum(x[i][j][m][n] for j in range(0,len(location)) for m in range(0,len(truckSize)) for n in range(0,len(upperDist))) ==1, "Route Allocation A" +str(i)
for j in range(0,len(location)):
    prob+= lpSum(x[i][j][m][n] for i in range(0,len(location)) for m in range(0,len(truckSize)) for n in range(0,len(upperDist))) ==1, "Route Allocation B" +str(j)

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
        prob += lpSum(truckSize[m] * lpSum(x[i][j][m][n] for n in range(0,len(upperDist)))for m in range(0,len(truckSize))) >= demandMat[i][j]*lpSum(x[i][j][m][n] for m in range(0,len(truckSize)) for n in range(0,len(upperDist))), "Weight Constraint" +str(i) + " "+str(j)

# a .lp file needs to be created for processing
prob.writeLP("OneAcre.lp")
prob.solve()
# to check whether solution is unbounded etc we check value of prob.status
# We have an array/dictionary to convert into text
# values of our decision variables can be printed as:
for item in prob.variables():
    if(item.varValue == 1):
        print item.name, "=" , item.varValue
# print optimal value, value() helps in formating
print "Status:", LpStatus[prob.status]

list = []

for i in range(0,len(location)):
    for j in range(i,len(location)):
        for m in range(0,len(truckSize)):
            for n in range(0,len(upperDist)):
                if((x[i][j][m][n]).varValue == 1.0):
                    vec = [i,j,m,n]
                    list.append(vec)

print list

for k in range(0,len(list)):
    print "Route is taken from ",location[list[k][0]], "and ",location[list[k][1]],"with a demand of ",demandMat[list[k][0]][list[k][1]], "using " , truckSize[list[k][2]], "ton trucks, with distance ", routeDist[list[k][0]][list[k][1]], "travelling ", distBrackets[list[k][0]][list[k][1]][list[k][3]]

print "Total Cost = $", value(prob.objective)

