import numpy as np
'''Solves problem which was demonstrated in https://www.youtube.com/watch?v=IWvbPIYQPFM&t=670s'''

def create_array(x, y, red):
    '''Creates an x by y array. Taking the coodinates in red, those values in the array are 1 while everything else is 0
     PRECONDIIONS: y -> int, x -> int, red -> lst containing a sublist with 2 values in it. ie) red = [[1,2],[3,4]]
     POSTCONDITIONS: Return an x by y array with all entries 0 except where entries are red, which are designated by a
     1'''

    array = np.zeros((x, y))

    for n in red:
        array[n[0],n[1]] = 1

    return array

def breadth_search(array,x,y,i,j,checked):
    '''A breadth first search which returns the max number of red squares connected to start point i,j
    PRECONDITION: x is the number of rows, y number of columns, i is the row start point, j the column start, checked
    is the values which have already been checked
    POSTCONDITION: Returns an int value which is the maximum number of connected nodes
    PARAMETERS: array -> array, x -> int, y-> int, i -> int, j -> int, checked -> lst of int values'''

    #Base Cases
    if array[i,j] != 1:
        return 0

    elif [i,j] in checked:
        return 0

    #Recursive Step
    else:
        checked.append([i, j])
        if j != 0:
            left = breadth_search(array,x,y,i,j-1,checked)
        else:
            left = 0
        if j != y:
            right = breadth_search(array,x,y,i,j+1,checked)
        else:
            right = 0
        if i != 0:
            up = breadth_search(array,x,y,i-1,j,checked)
        else:
            up = 0
        if i != x:
            down = breadth_search(array,x,y,i+1,j,checked)
        else:
            down = 0

    return(1 + left + right+ up + down)



def connected_num(x,y,array):
    '''Returns the maximum number of connected squares in the entire array
    PARAMETERS: x -> int, y -> int, array -> array
    PRECONDITION: x is the number of rows in array, y the number of columns in array
    POSTCONDITION: Returns an int value which is the maximum number of connected boxes in array'''

    print(array)
    max_num = 0

    for i in range(x-1):
        for j in range(y-1):
            connected = breadth_search(array,x-1,y-1,i,j,[])
            if connected > max_num:
                max_num = connected

    print('\n The max connected nodes in the array are: ',max_num)




#array = create_array(3,3,[[0,0],[1,0],[1,1],[2,1],[0,2]])
#connected_num(3,3,array)


