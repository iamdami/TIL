copy module
===
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dudwo567890&logNo=130163015383
<br>
- copy 모듈은 객체를 복사하기 위한 copy()와 deepcopy() 함수 제공  
- Python에서 list를 다른 변수에 할당하게 되면 참조형태로 전달되기 때문에 실제로 같은 물리공간에 위치한 데이터를 가리키게 됨  
- 참조하는 형태가 아닌 값을 복사하는 형태로 값 가져오려면 copy 모듈을 사용하면 됨  
<br>

## Deep Copy(깊은 복사)
- 실제 값을 새로운 메모리 공간에 복사  
<br>

## Shallow Copy(얇은 복사)
- 주소 값 복사
-> 참조하고 있는 실제 값은 같음

<br>
얕은 복사와 깊은 복사 모두 상위리스트의 경우 값을 복사해 가져왔기 때문에  
원본리스트의 상위리스트에 값 추가하더라도 복사한 리스트의 상위리스트는 영향을 받지 않음  
