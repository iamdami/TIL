VoVNET의 추후 버전 이름은 aVoVNet이였음 조켓다 ㅎㅎ  
fast -> faster 처럼,,, above,,♡  
<br>

### nms, confidence threshold, IoU threshold  
- https://medium.com/analytics-vidhya/non-max-suppression-nms-6623e6572536  
- Algorithm  
  1. define a value "confidence threshold", "IoU threshold"  
  2. sort the bounding boxes(descending order of confidence)  
  3. confidence threshold value 보다 작은 confidence value 가진 boxes remove  
  4. highest confidence 가진 box 부터 시작해 남은 boxes에 대해 같은 작업 진행  
  5. same class에 속한 남은 모든 boxes에 대해 current box의 IoU 계산  
  6. 2개 boxes의 IoU가 IoU threshold 보다 크면, 그 중 lower confidence 가진 box를 our boxes list에서 remove  
  7. list의 모든 boxes에 대해 이 연산 진행될 때까지 반복  

