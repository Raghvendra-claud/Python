from functools import reduce
# MAP
def cube(x):
    return x*x*x

# print(cube(5))
l = [1,2,3,4,5,4,6]
# newl = []
# for i in l:
#     newl.append(cube(i))
newl = list(map(cube,l))

print(newl)

# FILTER
def filter_function(a):
    return a>4

# newnewl = list(filter(filter_function,l))
newnewl = list(filter(lambda x: x>4,l))

print(newnewl)