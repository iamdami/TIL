# 매번 쓸 때마다 헷갈려서 기록!

import csv

with open(".csv", "r") as file:
    readFile = csv.reader(file)
    next(readFile)
    for line in readFile:
        print(line)
