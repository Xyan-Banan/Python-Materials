from random import random,randrange,randint,uniform

a,b,step = 0,10,3
x = random() #значение из диапазона [0;1.0)
x = randrange(a) #целое число из диапазона [0;a) random() * a
x = randrange(a,b) #целое число из диапазона [a;b)
x = randrange(a,b,step) #целое число из диапазона [a;b) с шагом step ()
x = randint(a,b) #целое число из диапазона [a;b] randrange(a,b + 1)
x = uniform(a,b) #число с плавающей точкой из диапазона [a;b] (для a<=b) и [b;a] (для b<a). точка b может быть или не быть включена из-за проблем с округлением