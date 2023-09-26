'''
Created by: Gurmanpreet Singh Tiwana
https://www.linkedin.com/in/gurmannnpreet/
http://gurmannnpreet.me
https://github.com/gurmannnpreet

Program to find a Reduced Row Echelon Form of a matrix

Consists of the following functions:

findpivot(m)
swaprows(m,row)
makeone(m,row,column)
makezeroes(m,row,column)
makeintegers(m)
main(matrix)
'''

def findpivot(m):
    '''
    m: The matrix in which the pivot has to be found

    It finds the pivoting entry
    The pivot will be considered as the leading entry for the row
    Returns the row and column of the pivot
    '''
    
    #First attempt is to find any leading 1s, it makes the work easy
    for column in range(len(m[0])):
        for row in range(len(m)):  #Searching every element column wise, not row wise.
            
            if m[row][column] == 1:

                #The following statements check if the 1 found is a leading 1
                correct = 1  #Deciding variable
                if column > 0:
                    for a in m[row][:column]:
                        if a != 0:
                            correct = 0
                if correct == 0:
                    break
                return (row, column)
                
    #Now search for any leaading entry, not just 1        
    for column in range(len(m[0])):
        for row in range(len(m)):

            if m[row][column] != 0:
                return (row, column)
    
    return('over')  #If no pivot is found, the execution has to be stopped


def swaprows(m, row):
    '''
    m: matrix which has to operated upon
    row: number of rows that have been finalized till now

    It finds the pivot by executing findpivot function over the matrix given
    Returns over if no pivot is found
    If the row with the leading entry is not in the correct position,
    it swaps the row with the highest row, that has not been finalized yet
    Returns the correctly order matrix along with the column index of the pivot
    '''
    
    pivot = findpivot(m[row:])  #Sends only the unfinalized rows to the findpivot function
    
    if pivot == 'over':  #If the operation is to be ended
        return 'over'  
    
    if (pivot[0]+row) > row:  #Checks if there is a need of a row swap
        m[pivot[0]+row], m[row] = m[row], m[pivot[0]+row]  #Row swapping
    
    return m, pivot[1]


def makeone(m, row, column):
    '''
    m: matrix which has to operated upon
    row: Row index that has the pivot(has to be operated on)
    column: The column index which has the pivot

    It finds the value of the pivot and stores as c
    If c is 1, it does not change anything and returns the same matrix
    If c is not 1, it divided every entry in the row by c, and converts the pivot into 1
    Returns the matrix with the pivot being a leading 1
    '''
    
    c = m[row][column]  #Value of the pivot

    if c == 1:
        return m
    
    for j in range(len(m[row])):
        m[row][j] /= c

    return m


def makezeroes(m, row, column):
    '''
    m: matrix which has to operated upon
    row: Row index that has the pivot/ Finalized rows yet
    column: The column index which has the pivot

    Leaves the row with the pivot as it is
    Finds the required scalar to be able to create zeroes in the pivot column
    Performs appropriate functions on other rows to create neede zeroes
    Returns the matrix after completing its task   
    '''
    
    for i in range(len(m)):  #Iterates through every row
        if i == row:  #Skips the pivot row
            continue
         
        c = m[i][column]  #finds a scalar
        for j in range(len(m[i])):
            m[i][j] = m[i][j] - (c*(m[row][j]))  #Performs the row operation

    return m


def makeintegers(m):
    '''
    m: The matrix that has to operated upon

    It takes a matrix after the program has found the answer
    It converts all entries which are integers, but written as floats i.e with .0 at the end
    Rounds off the floats to 2 decimal places
    Makes the matrix look more readable
    Returns the cleaner looking matrix
    '''
    
    for column in range(len(m[0])):
        for row in range(len(m)):

            if int(m[row][column]) == m[row][column]:  #Checks if the entry is an integer
                m[row][column] = int(m[row][column])

            else:
                m[row][column] = round(m[row][column],2)  #Rounds off the floating point numbers

    return m
            

def main(matrix):
    '''
    matrix: The matrix whose rref is to be found

    Combines all the functions defined above to compute the problem
    Returns the matrix after converting all entries into integers/ 2 decimal numbers
    '''

    for row in range(len(matrix)):  #Iterates the matrix row after row

        step1 = swaprows(matrix, row)  #Finds the pivot and swaps the rows

        if step1 == 'over':  #Breaks the iteration and prevents any further errors
            break

        step2 = makeone(step1[0], row, step1[1])  #Makes the pivot 1 if required
        
        step3 = makezeroes(step2, row, step1[1])  #Makes all entries in the pivot column 0

        matrix = step3 #Changes the matrix variable so that next iteration yields accurate matrices

    answer = makeintegers(matrix)  #Makes the matrix more clean-looking

    return answer  #Returns the final matrix


def rref(matrix):
    '''
    matrix: The matrix that has to be operated on

    The final method that takes the matrix as input
    Prints the final matrix(rref) row by row, to make it more readable
    '''

    solution = main(matrix)  #Calls the main function for the computation

    for i in solution:  #Iteration to print every row in a new line
        print(i) 


#A sample case to check the program
'''
matrix = [
        [-3,-1,3,-3],
        [0,-2,-1,1],
        [3,2,-3,0]
    ]

rref(matrix)
'''
