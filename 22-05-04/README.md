## np.zero와 np.zeros_like
- [numpy.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)  
- [numpy.zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html)  

<br>

- **np.zeros**  
  - 0으로 가득찬 array 반환  
  - tuple, int 혹은 list 값 들어와야 함  
  -> 해당하는 shape으로 형태 만들어준 후 array return  
  -> np.zeros_like 처럼 변수 넣어주면 에러  
<br>

  ![image](https://user-images.githubusercontent.com/50016477/166642438-b82b6905-d51e-43b3-b216-e6baa8a1b5ab.png)  
  
<br>

- **np.zeros_like**  
  - 어떤 변수 만큼의 사이즈인 0으로 가득찬 array 반환  
  - 변수가 들어와야 함  
  - [1, 2, 3] 이런식으로 파라미터 넣어줘도 됨 -> [0, 0, 0] 반환  
<br>

![image](https://user-images.githubusercontent.com/50016477/166642577-2b704bb9-6e7f-4cf9-a191-0ea6959dd404.png)  

<br>
