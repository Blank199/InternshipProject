from itertools import combinations

"""
@:param arr - array with values
        r - number of elements
@:returns a list of lists with all the combination
"""


def combination(arr, r):
    # an auxiliary array for saving data
    data = [0] * r
    res = []

    # add in res data saved in data
    auxiliaryCombination(arr, r, 0, data, 0, res)
    return res


""" arr[] ---> Input Array 
r     ---> Size of a combination to be printed 
index ---> Current index in data[] 
data[] ---> Temporary array to store 
            current combination 
i     ---> index of current element in arr[] 
res     ---> an empty lst for result  """


def auxiliaryCombination(arr, r, index, data, i, res):
    # Current combination is ready,
    if index == r:
        list = []
        for j in range(r):
            list.append(data[j])
        res.append(list)
        return

    # depletion data
    if i >= len(arr):
        return

    # add the next value
    data[index] = arr[i]
    auxiliaryCombination(arr, r, index + 1, data, i + 1, res)

    # step over
    auxiliaryCombination(arr, r, index, data, i + 1, res)


"""
@:param points - list of 4 points represented as tuples
@:returns true if the list form a rectangle

"""


def verifyRectangle(points):
    # lists that contains all values for X and Y
    x = []
    y = []

    # fill x and y with unique values
    for point in points:
        if point[0] not in x:
            x.append(point[0])
        if point[1] not in y:
            y.append(point[1])

    # return true if the length of the array is 2
    # false otherwise
    if len(x) == len(y) == 2:
        return True
    return False


"""
@:param points - list of 4 points represented as tuples
@:returns number of rectangles that could be formed 

"""


def countingRectangles(points):
    count = 0
    # generate all combinations of four
    res = combination(points, 4)

    # check if the combination form a rectangle
    for i in list(res):
        if verifyRectangle(i):
            count += 1
    return count


print(countingRectangles([(1, 1), (1, 3), (2, 3), (2, 1), (3, 1), (3, 3)]))
