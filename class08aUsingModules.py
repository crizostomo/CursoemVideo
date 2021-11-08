import math
import random

num = int(input('type a number'))
squareroot = math.sqrt(num)
print('the square root of {} is {:.2f}'.format(num, squareroot))

#{.2f} limitates the spaces

randomNum = random.random()
randomNumInt = random.randint(1, 20)
print(randomNum)
print(randomNumInt)