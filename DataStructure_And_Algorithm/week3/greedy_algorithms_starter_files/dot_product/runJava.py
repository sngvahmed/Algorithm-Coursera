from random import randint
import os
import sys
from dot_product import max_dot_product


os.system("javac DotProduct.java")

for i in range(100):
    n = randint(1, 100)
    arr1, arr2 = [], []
    for j in range(n):
        arr1.append(randint(-100, 100))
        arr2.append(randint(-100, 100))

    str1 = ' '.join(str(e) for e in arr1)
    str2 = ' '.join(str(e) for e in arr2)

    os.system('echo "{} {} {}" > input.txt'.format(n, str1, str2))

    os.system("java DotProduct < input.txt")
    file = open("out.txt", "r")
    input = int(file.read())
    resultP = max_dot_product(arr1, arr2)
    if resultP == input:
        print("YES")
    else:
        print("NO {} {} rjava={} rpy={}".format(arr1, arr2, input, resultP))
        break
