## Object Tracking
<pre>
Object tracking is the task of taking an initial set of object detections, 
creating a unique ID for each of the initial detections, 
and then tracking each of the objects as they move around frames in a video, 
maintaining the ID assignment.
</pre>
- [object tracking - paperswithcode](https://paperswithcode.com/task/object-tracking/latest) 

## Paper
- [A Survey on Object Detection and Tracking Methods](https://www.semanticscholar.org/paper/A-Survey-on-Moving-Object-Detection-and-Tracking-Pathan-Chauhan/590acc13826d21e2468801c1ec038ec4d1afe8ab?p2df)  
- [Comparison of Background Subtraction and Frame Differencing Methods for Indoor Moving Object Detection](https://ieeexplore.ieee.org/document/9398484)  
<pre>
The results of the study show in terms of the success of the frame differencing method 
that is more accurate in detecting objects.
While in terms of computing the background subtraction method is faster in detecting objects.
</pre>

## Reference
- [Object Tracking - blog review](https://mickael-k.tistory.com/26)
- [paper review(ko)](https://eehoeskrap.tistory.com/90)
- [SORT - blog review](https://mickael-k.tistory.com/48)  
- [Yolov5_StrongSORT_OSNet Evaluation(with other SOTA online trackers](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Evaluation)  
- [Object Tracking - quick guide](https://cv-tricks.com/object-tracking/quick-guide-mdnet-goturn-rolo/)  
- [object-tracking-deepsort](https://nanonets.com/blog/object-tracking-deepsort/)  

## Background substraction
- [background substraction pdf](https://www.dsi.unive.it/~atorsell/Visione/12-background%20subtraction.pdf)  

## VOT(Visual Object Tracking), MOT(Multiple Object Tracking)
- [VOT, MOT](https://gaussian37.github.io/vision-concept-vot_mot/)  

## Kalman Filter, Particle Filter
- [Kalman Filter](https://www.codeproject.com/Articles/865935/Object-Tracking-Kalman-Filter-with-Ease)  
- [Kalman Filter - wikipedia](https://ko.wikipedia.org/wiki/%EC%B9%BC%EB%A7%8C_%ED%95%84%ED%84%B0)  
  - 칼만 필터는 과거에 수행한 측정값 바탕으로 현재 상태 변수의 결합분포 추정  
  - 알고리즘은 예측과 업데이트의 두 단계로 이루어짐  
  - 예측 단계: 현재 상태 변수 값과 정확도 예측  
  - 업데이트 단계: 이전에 추정한 상태 변수 기반으로 예측한 측정치와 실제 측정치의 차이 반영해 현재 상태 변수 업데이트  
- [particle Filter](https://www.codeproject.com/Articles/865934/Object-Tracking-Particle-Filter-with-Ease)  

## Algorithm
- [SORT - github](https://github.com/abewley/sort)  
  - A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences.
  
영상분석솔루션 동향 조사 중 발견했는데 다들 비슷한 과정 거쳐 나아가는 게 넘 신기했다..!  
- https://github.com/kimhwangdae/MarkAny_Intern  
<br>

## Yolo5 object tracking pytorch
- [Yolo5 object tracking pytorch](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet)  
- [Deep learning person re-identification in PyTorch](https://github.com/KaiyangZhou/deep-person-reid)  
  - **Torchreid**: library for deep-learning person re-identification, written in PyTorch  
- [deep_sort_pytorch](https://github.com/ZQPei/deep_sort_pytorch)  
<br>

## 지능형 영상분석 폭력 탐지
- [지능형 영상분석을 통한 폭력 비폭력 구분](https://eehoeskrap.tistory.com/216)  
  - 객체의 형태가 심하게 변화하는 특징을 이용해 화면상의 객체 크기 및 변화 횟수 급격히 증가하면 폭력 발생으로 간주  
(객체의 크기 변화, 즉 높이와 너비 값 인식해 미리 세팅된 높이와 너비 변화율과 변화 횟수 값 이상일 때)  
<br>

## 이상 탐지(Anomaly Detection)
- [Anomaly Detection](https://eehoeskrap.tistory.com/403)  
  - 정상(Normal) 데이터와 Abnormal(비정상, 이상치, 특이치) 데이터를 구별해내는 문제  
<br>

## fall down
- [fall down datasets](https://eehoeskrap.tistory.com/348)  
- [Human-Falling-Detect-Tracks](https://github.com/GajuuzZ/Human-Falling-Detect-Tracks)  
- [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)  
<br>

## 적응적 배경 모델링(Adaptive background modeling)
- 기존의 배경 모델링 방법은 배경 모델의 반복적 갱신(recursive update)으로 인해  
  배경보다 객체가 더 자주 동장하는 혼잡한 환경에서는 정확한 배경 모델링을 생성하기 어려운 문제를 지님  
  기존의 혼합 Gaussian 모델을 기반으로 하는 적응적 배경 모델링 방법은 영상 내 전경 영역의 비율에 따라 배경 모델 학습 비율을 적응적으로 조절  
  따라서 혼잡 상황애서 배경 모델 갱신 억제해 배경 모델 잘 유지시키는 것 가능  
<br>
