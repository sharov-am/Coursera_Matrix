# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    return [x for x in L if x%num != 0]



## Problem 2
def myLists(L):
    return [list(range(1,x+1)) for x in L]



## Problem 3
def myFunctionComposition(f, g):
    return {fKey : g[f[fKey]] for fKey in f.keys()}



## Problem 4
# Please only enter your numerical solution.

complex_addition_a = complex(5,3)
complex_addition_b = complex(0,1)
complex_addition_c = complex(-1,.001)
complex_addition_d = complex(.001,9)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    current = 0
    for x in L:
      current += x
    return current



## Problem 7
def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current


## Problem 8
def myMin(L):
    current =  float("inf")
    for x in L:
        if x < current:
            current = x
    return current


## Problem 9
def myConcat(L):
    current = ""
    for x in L:
       current += x
    return current



## Problem 10
def myUnion(L):
    current = set()
    for x in L:
       current = current.union(x)
    return current


if __name__ == "__main__":
    t =myLists([1,2,4])
    print(t)