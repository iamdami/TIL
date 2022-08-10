yolo versions
===
## yolo?
- real time object detection에 사용되는 알고리즘  
- Josept Redmon이 2015년에 yolov1 논문 발표, 공개  
- 각 이미지를 SxS개의 그리드로 분할, 각 그리드의 신뢰도 계산  
- 처음에는 객체와 동떨어진 그리드가 설정되지만, 신뢰도 계산해 위치 조정함으로서 가장 높은 객체인식 정확성 가지는 그리드 얻음  
- 신뢰도는 주변의 그리드 합쳐 높이고, 이후 임계값 설정해 불필요한 부분 제거  

## yolov3
- 2018년 4월 출시  
- 백본 아키텍쳐 Darknet53 기반으로 만들어짐  
- yolo 만든 Josept Redmon이 발표  

## yolov4  
- 2020년 4월 출시  
- v3에 비해 AP, FPS가 각각 10%, 12% 증가함  
- Alexey Bochkousky가 발표  
- v3에서 다양한 딥러닝 기법(WRC, CSP ...)들을 사용해 성능 향상  
- CSPNet 기반의 백본(CSPDarknet53)을 설계해 사용  

![v3와 v4 비교](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Flu8Wg%2FbtqIWQ2Hs1P%2FXnM8Xfj0tuKiSkqtKfm1P1%2Fimg.png)  

## yolov5
- 2020년 6월 출시  
- v4에 비해 낮은 용량과 빠른 속도 가짐(성능은 비슷)  
- yolov4와 같은 CSPNet 기반의 백본 설계해 사용  
- yolov3을 Pytorch로 구현한 GlennJocher가 발표  

![학습 속도 비교](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcxMtKw%2FbtqITtme1vk%2FKmwQtGNOB8c7kqyiIpDREk%2Fimg.png)  
<br>

![용량 비교](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbk8Lc6%2FbtqIWRtIGUT%2Few7zyO6vcIGWaz9Pz3NQkK%2Fimg.png)  
<br>

![yolo 버전 비교](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FHgR35%2Fbtq6RNfukFf%2Ftbar7aaWQKbvE8EEkCevK1%2Fimg.png)  
<br>

## pp-yolo
- 2020년 7월 출시  
- yolov4보다 정확도와 속도 높음  
- v3모델을 기반으로 하지만, Darknet3 백본을 ResNet 백본으로 교체했고 오픈소스 깊이 학습 플랫폼인 PaddlePaddle에 바탕을 두고 있음  

![v3, v4, pp 비교](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbOLNxE%2FbtqIXfnoEUS%2F34IIqhELYmn0WMPmEbE2S1%2Fimg.png)  
<br>

## Conclusion
- yolov4는 v5에 비해 느리고 동작하지만 FPS성능 최적화 가능  
- v5는 v4에 비해 더 쉽게 환경 구성할 수 있음  
  

## References
- [YOLO v4 or YOLO v5 or PP-YOLO?](https://towardsdatascience.com/yolo-v4-or-yolo-v5-or-pp-yolo-dad8e40f7109)  
- [다양한 YOLO 버전, 어떤 버전을 선택해야 할까](https://yong0810.tistory.com/30#:~:text=YOLOv4%EB%8A%94%20v5%EC%97%90%20%EB%B9%84%ED%95%B4,%EC%88%98%20%EC%9E%88%EB%8B%A4%EB%8A%94%20%ED%8A%B9%EC%A7%95%EC%9D%B4%20%EC%9E%88%EB%8B%A4.&text=%EC%8B%A4%EC%9A%A9%EC%A0%81%EC%9D%B8%20%EC%B8%A1%EB%A9%B4%EC%97%90%EC%84%9C%20%EB%B9%A0%EB%A5%B4%EA%B2%8C%20%EA%B5%AC%ED%98%84,%EB%8D%94%20%EC%A2%8B%EC%9D%84%20%EA%B2%83%EC%9D%B4%EB%9D%BC%EA%B3%A0%20%EC%83%9D%EA%B0%81%ED%95%9C%EB%8B%A4.)  
