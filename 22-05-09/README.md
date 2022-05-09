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
<br>

## ZeroDivisionError: division by zero
- [stackoverflow](https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero)  
![image](https://user-images.githubusercontent.com/50016477/167353764-fb5d6ef6-ba5d-414d-b0b4-0ea02cba28f6.png)  
<br>

## TypeError: 'float' object is not iterable
- Case 1 : Solution for looping scenario using range  
```
element= 7.5
for i in range(int(element)):
  print(i)
```
- Case 2 : Float iteration as str object  
```
element= 7.5
for i in str(element):
  print(i)
```
