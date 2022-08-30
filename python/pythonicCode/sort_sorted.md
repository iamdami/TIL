## sorting
sort(): 리스트를 내부 정렬하는 메소드  
sorted(): 컨테이너형 데이터 받아 정렬된 리스트 돌려주는 함수  

```
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list). # 2, 3, 4, 5, 6, 8
_list.sort()
print(_list)  # 2, 3, 4, 5, 6, 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
_set.sort()  # Error
print(sorted(_set))  # 12, 15, 31, 54, 65, 82, 94, 156
```
sorted()의 출력값은 리스트  
딕셔너리와 셋은 순서가 없음  
<br>
내림차순 정렬
```
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reversed = True)  # 8, 6, 5, 4, 3, 2
```

### using lambda
다양한 방식으로 정렬 가능  
```
_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']
```
일반적으로 문자열은 대소관계 비교함  
모두 소문자로 바꾸면 대소관계 상관없이 정렬 가능  
