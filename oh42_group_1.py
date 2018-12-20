import numpy as np
##Young Oh
##Group 2
##Group Homework 1
#3. Exploring the module

##A
#1
a = np.array([1,2,0])

#2
b = np.array([[4,5,6],[7,8,9]])

#3
a.dtype
#('int32')

#4
##for a
a.shape
a.size
a.ndim

#a's shape = (3,)
#a's size = 3
#a's ndim = 1

##for b
b.shape
b.size
b.ndim

#b's shape = (2,3)
#b's size = 6
#b's ndim = 2
##All of their attributes are different. Obviously, b's size and number of dimensions are larger than a because b contains more data

#5
a[2] = 3
##print(a)


##B
#1
scores_list = [35.5, 42, 39.2, 50, 47.7]
#2
grades_list = []
for score in scores_list:
    final = (score / 50 * 100)
    grades_list.append(final)


##C
#3
scores = np.array([35,42,39,50,47])

#4
result = scores/50*100
print(result)

#5
scores.dtype
print(scores.dtype)
#('int32')


##D
length = [3, 2, 5, 1, 7]
height = [4, 7, 5, 2, 3]
l = np.array([3, 2, 5, 1, 7])
h = np.array([4, 7, 5, 2, 3])

##E
area = []
sumList = []
for data in range(len(height)):
    area.append(length[data]*height[data])
####print(area)
##sum(area)

##F
areaArray = l*h
#sum(areaArray)
