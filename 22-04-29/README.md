## Stochastic pooling
- max pooling과 average pooling의 단점을 model averaging 통해 극복, overfitting 문제 피할 수 있음  
- Stochastic pooling은 dropout과 맥을 같이 함  
<br>

## Maxout
- [From Maxout to Channel-Out: Encoding Information on Sparse Pathways](https://link.springer.com/chapter/10.1007/978-3-319-11179-7_35)  
- dropout 효과 극대화시키기 위해 구현한 활성화 함수  
![image](https://user-images.githubusercontent.com/50016477/165909291-6722be63-43b3-4fd2-9a8d-4f1d4e1ce58b.png)  
Where w = weights, b = biases, T = transpose  
<br>

![image](https://user-images.githubusercontent.com/50016477/165911082-5c6f0c32-71ed-4fd0-990c-87af5148be4c.png)  
- 일반적인 hidden layer는 1개의 layer로 구성되지만 Maxout hidden layer는 2개의 layer로 구성됨  
  - affine function 수행하는 영역(녹색)과, 최대값 선택하는 영역(파란색)
  - affine function: 전통적인 hidden layer처럼 활성화 함수 있는 게 아니라 단순히 입력 x를 각각의 weight에 곱해 더하는 형식이라 이렇게 부름  
<br>

![image](https://user-images.githubusercontent.com/50016477/165910199-f742fa35-0ba3-4a36-b64c-d0078e38dd56.png)  

<br>

- 결과적으로 Maxout은 **affine 함수 부분과 최대값 선택하는 부분 이용해 임의의 볼록 함수(convex function)를 piecewise linear approximation하는 것**  
- Maxout시 결과 좋아지는 이유: Maxout에 dropout 적용하면서 생기는 model averaging 효과 때문    
- [Maxout 참고 링크](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=laonple&logNo=220836305907)  
