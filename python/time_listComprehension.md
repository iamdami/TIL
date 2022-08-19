## time module  
- [A Beginner’s Guide to the Python time Module](https://realpython.com/python-time-module/)  
what I needed was **time.ctime**  
```
>>> from time import ctime
>>> ctime()
'Mon Feb 25 19:11:59 2019'
```
<br>

## using list comprehension
```
new = []
for i in A:
    new.append([i])
```
- more beautiful solution:  
```
new = [[i] for i in A]
```
