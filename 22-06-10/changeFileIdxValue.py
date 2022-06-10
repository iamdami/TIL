from operator import index
import os
import os.path


with open("./path", "r") as f:
    data = f.read()

data = data.replace("0 ", "80 ")

with open("./path", "w") as f:
    f.write(data)
