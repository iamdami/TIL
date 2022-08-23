import csv

with open(".csv", "r") as file:
    readFile = csv.reader(file)
    next(readFile)  # removing header
    for line in readFile:
        ptLine = list(map(int, line[1:]))  # 이런 식으로 가져오면 됨
        print(ptLine)
