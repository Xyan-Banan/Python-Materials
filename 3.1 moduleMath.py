#MATH MODULE USING
##################

#первый вариант использования
def first():
    import math
    math.sin(math.pi/2)

#второй вариант
#from math import *
#sin(pi/2)

#третий вариант
def third():
    from math import sin,pi
    sin(pi/2)


#ROUNDING
#########

x = 1.55
y = -1.55

# round to the nearest integer
round(x)       #  2
round(y)       # -2

# the second argument gives how many decimal places to round to (defaults to 0)
round(x, 1)    #  1.6
round(y, 1)    # -1.6

# math is a module so import it first, then use it.
import math

# get the largest integer less than x
math.floor(x)  #  1
math.floor(y)  # -2

# get the smallest integer greater than x
math.ceil(x)   #  2
math.ceil(y)   # -1

# drop fractional part of x
math.trunc(x)  #  1, equivalent to math.floor for positive numbers
math.trunc(y)  # -1, equivalent to math.ceil for negative numbers

#round breaks ties towards the nearest even number. This corrects the bias towards larger numbers when performing a large number of calculations.

round(0.5)  # 0
round(1.5)  # 2

#Python round away from zero for negative numbers. Consider:

math.floor(-1.7)    #-2
math.ceil(-1.7)     #-1
-5 // 2             #-3