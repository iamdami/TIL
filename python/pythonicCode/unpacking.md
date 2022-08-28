## Unpacking
### iterable
``` a, b = map(int, input().split()) ```
- 모든 반복 가능한 객체를 iterable이라고 함
- 리스트, 튜플, 문자열 등

> 입력 받은 list에서 첫번째 값, 마지막 값만 필요한 경우
```
_list = [1, 2, 3, 4, 5]
first_index, *rest, last_index = _list
print(rest) # 2 3 4
```
*(asterisk) 사용하는 상황  
- 곱셈, 거듭제곱
- list형 컨데이너를 반복해 확장
- 가변 인자
- unpacking

위 코드에서 rest에 사용한 것은 가변 인자  
- 인자 개수가 몇 개가 될지 확실하지 않을 때 사용

### what is unpacking?
```
_list = [1, 2, 3, 4, 5]
for num in _list:
    print(num, end = ' ') # 1 2 3 4 5
```
_list 내 원소들 출력하는 평범한 코드  

```
_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5
```
-> list unpacking  

list 뿐만 아니라 컨테이너형 구조에서는 모두 적용 가능(튜플, 셋)  

### packing
```
a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)
```
이런 식으로 하나의 변수에 여러 값을 할당하면 튜플로 묶임  
-> packing  
