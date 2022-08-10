remove
===
- remove 함수는 값으로 array 요소 삭제  
- array.remove(x) 형태로 사용  
- array 안에서 삭제하고자 하는 값이 여러 개 있다 하더라도 첫 번째 값에 대해서만 삭제  
- remove 함수 사용해 값 삭제할 때는 for문 이용 가능  
<br>

```
num = [1, 2, 2, 3, 3, 3]
num.remove(3)
print(num)
# [1, 2, 2, 3, 3]
# 숫자 3이 2개로 줄어듦
```
<br>

```
num = [1, 2, 2, 3, 3, 3]

for _ in num :
  num.remove(3)
print(num)
# [1, 2, 2]
# 숫자 3이 없음
```
