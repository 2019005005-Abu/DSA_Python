##> w r
"""
Use Input - How many data u want to input
loop- input all loope
loop- conditions
"""
numbeOfElements = int(input("Elements"))
Lst = []

for value in range(numbeOfElements):
    num = int(input())
    Lst.append(num)
for num in Lst:
    if num <= 120:
        if num % 10 == 0:
            print(num)
    else:
        break


"""
##problem-1------##
Read all integers N and complete all its divisors
"""
Num = int(input())
for value in range(1, Num + 1):
    if Num % value == 0:
        print(value)

##> w r
"""
##problem-2------##
Hasan  went to gym today he decided to do  X sets of squats.
Each sets consists of 15 squats
"""
"""
1.The first line contains a single integer
T -> the number of test cases Then the test case 
follow
2.The first and  only line of each test cases  contains
contains an integer X -- the total number of sets of squats that
Hasan did

                                   ------------------------------------------------------------------------|
                                               input                                 output                |
                                   ------------------------------------------------------------------------|
                                                3--------------------------------------15------------------|
                                                1--------------------------------------60------------------|
                                                4--------------------------------------1485----------------|
                                                99---------------------------------------------------------|
                                 --------------------------------------------------------------------------|

"""
n_cases = int(input("Cases:"))
for index in range(n_cases):
    n_set = int(input("n_set:"))
    print(n_set * 15)

##Problem_3:

"""
Hasan and Mahmud participate in a coding contest as a result of 
which they received NN chocolates.Now they want to divide the 
chocolate between them equality.
"""
