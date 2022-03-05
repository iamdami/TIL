eval()
===
https://docs.python.org/ko/3.8/library/functions.html?highlight=eval#eval  

- 문자열이나 표현식, 변수들을 입력으로 받아 이를 계산하고 반환해주는 함수  
- 문자열, 표현식, 변수들이 모두 str 타입이어야 함  
  
```
x = 1
eval('x+1')
>>>> 2
```  
<br> 
  
- ```requests```등으로 json, list 등의 데이터 받는 경우 문자열로 받아지는 경우가 많음  
- 이 경우 string 데이터를 파싱하면 문자열을 바로 list로 반환하려고 하면 문자열 입력이기 때문에  
  character 단위로 쪼개짐  
- 문자열로 표현된 리스트를 리스트 자체로 만들려면 ```eval()```을 쓰면 됨  
- eval()을 사용하면 해당 표현식을 입력받아 계산해 반환해줌  
<br>

```
test = ['a', 1, 2, '34']
test = str(test)
test
>>>> "['a', 1, 2, '34']"

eval(test)
>>>> ['a', 1, 2, '34']

type(eval(test))
>>>> <class 'list'>
```
