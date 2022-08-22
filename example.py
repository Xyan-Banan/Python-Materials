import random
from time import time
from random import randint


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSort2(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSort3(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [randint(0, 250) for i in range(50000)]
# t = time()
# bubbleSort(arr.copy())
# print(time() - t)

t = time()
bubbleSort2(arr.copy())
print(time() - t)

# t = time()
# bubbleSort3(arr.copy())
# print(time() - t)
