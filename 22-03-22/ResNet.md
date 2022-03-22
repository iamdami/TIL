Ref.
===

- [유튜브 '동빈나' paper review](https://www.youtube.com/watch?v=671BsKl8d0E)  
- [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)  
- https://www.datamaker.io/posts/36/  
![image](https://user-images.githubusercontent.com/50016477/159427804-e296932a-151c-4be8-a1a5-00521868bd91.png)  
  - Residual Block 이용해 네트워크 최적화 난이도 ↓  
  - F(x) = H(x) - x 학습  
  - **앞서 학습된 정보 + 잔여 정보**  
    **multiple conv layers + shortcuts**  
    ⇒ 학습 빠르고 더 높은 성능  
  - 입력 값 = 출력 값일 때는 identity mapping 사용 가능      
    if not  
    1. side에 padding 붙이고 identity mapping  
    2. projection 연산 활용, short connection  

- https://bskyvision.com/644  
