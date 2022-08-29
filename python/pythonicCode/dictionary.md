## Dictionary
- dictionary와 set은 hash table 구조 띔  
-> 삽입, 삭제, 탐색 연산의 시간복잡도: O(1). 

### set
> 초보 코드
값을 찾기 위해 list에서 in 사용함  
```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(100):
    if i in data:
        print(1)
```
위 코드는 데이터를 순차적으로 탐색함  
-> 하나의 숫자 찾기 위해 최대 10번 데이터 확인해야 함  

> 이럴 때 set 사용  

```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataSet = set(data)  

for i in range(100):
    if i in data:
        print(i)
```
실제로 몇 백만 개의 데이터 있는 set에 약 10만 번 정도 in 연산 해도 1초도 안 걸리는 시간에 완료함  
list 사용 시 몇 시간 이상 걸릴 수 있음!  

set 구조 상 같은 값이 들어올 수 없음
```
eraseDuplicate = [21, 31, 65, 21, 58, 94, 13, 31, 58]
resList1 = list(set(eraseDuplicate)) # 21, 31, 65, 58, 94, 13

testList = ['Test', 'test', 'TEST', 'tteesstt']
resList2 = list(set(map(lambda string: string.lower(), testList))) # test, tteesstt
```
위 코드에서 뒤에 있는 string은 각각의 값을 string이라고 지칭하겠다고 선언하는 것  
각각의 데이터를 소문자로 바꾸고 그걸 set으로 바꾸고 다시 list로 돌린 것  

set은 iterable한 데이터를 기반으로 만들 수 있음  
-> 이걸 다시 list로 바꿔주면 중복된 값 제거된 list 만들어 짐  

### dictionary
키와 쌍으로 이루어져 있음  
```
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict.append((fruit[i], price[i])) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

```

> zip
- 각 iterable의 요소들을 모으는 이터레이터 만듦

리스트를 묶어준다는 얘기  

```
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}
```

일반적으로 딕셔너리에서 없는 값 찾으려고 하면 오류 남  
```
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict['strawberry']) # Error!
```

이를 피하기 위해 주로 in 옵션 사용해 데이터가 있는지 확인하고, 없으면 값 추가하고 있으면 출력하는 방식으로 넘어감  
-> 꼭 if를 써야하는 게 아님!  
```
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict.setdefault('strawberry', 0)) # 0
```

> ``` setdefault ``` 는 딕셔너리에 값 있을 때는 해당 값 반환, 값 없을 때는 두 번째 인자로 넘겨준 값 추가 후 추가한 값 리턴   

위 같은 메소드 활용한 유사 dictionary 존재  
> defaultdict

```
from collections import defaultdict

movieReview = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]
idx = defaultdict(list)

for review in movieReview:
    idx[review[0]].append(review[1])
```
defaultdict에서 값 검색할 때 값 없으면 인자로 넘겨준 값이 default값 됨  
-> 찾을 때마다 setdefault를 암묵적으로 실행해준다고 생각하면 됨  

### dictionary unpacking
```
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(*_dict.keys()) # apple grape orange banana
print(*_dict.values()) # 3200 15200 9800 5000
print(*_dict.items()) # ('apple', 3200) ('grape', 15200) ('orange', 9800) ('banana', 5000)
```

