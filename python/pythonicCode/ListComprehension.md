## List Comprehension
기본형  
```
_list = [i for i in range(10)] # 0 1 2 3 4 5 6 7 8 9
```

### 구조
> (변수를 활용해 만들 값) for (변수 명) in (순회할 수 있는 값)  
- list comprehension으로 된 코드 읽을 때 for 뒤 부터 읽으면 편함  
- 다차원 배열도 사용 가능

```
square = [[x ** 2 for in range(3)] for _ in range(3)]
print(squre) # [[1, 4, 9], [1, 4, 9], [1, 4, 9]]
```

- 코드 길이는 확실히 줄일 수 있지만, 너무 길면 가독성 떨어지고 헷갈림  
- 리스트 뿐만 아니라 튜플, 셋, 딕셔너리도 만들 수 있음  

### 예제 코드
```
# 1 ~ 10 담는 리스트
_list = [i for i in range(10)]

# 2, 4, 6, ..., 20 담는 리스트
_list = [2 * i for in in range(10)]

# 주어진 리스트 받아 3의 배수만 담는 리스트
input = [random.randrange(1, 200) for i in range(100)]
_list = [i for i in input if i % 3 == 0]

# 값이 두 개 들어있는 튜플 받아 리스트 생성하되, 튜플 내부의 값을 뒤집어 저장
tupleList = [(j, i) for i in range(100), for j in range(100, 0, -1)]
_list = [(j, i) for i, j in tupleList]

# 주어진 리스트를 그대로 담되, 15 넘어가는 값은 15로 바꿔 저장
_list = [i if i <=15 else 15 for i in tmp]

# 두 개 리스트 합치되, 가능한 모든 조합 저장하는 리스트
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i, j) for i in x, for j in y]
```


