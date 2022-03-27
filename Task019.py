#19.Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# import random
# print(random.randint(-100, 100))

from msilib import sequence
from random import shuffle
import time
"""решение с использованием времени-секунды"""
def rand_int(start, stop):
    sequence=[items for items in range(start, stop+1)]
    seconds=str(time.time())
    index=int(seconds[len(seconds) - (len(str(stop)) - 1):])
    shuffle(sequence)
    return sequence[index]

print(rand_int(-10,10))

