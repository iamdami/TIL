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
