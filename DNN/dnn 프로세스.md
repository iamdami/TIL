dnn 프로세스
===
추론 엔진으로 opencv를 사용하려면 tensorflow, caffe 및 pytorch 같은 딥러닝 프레임워크에서 훈련된 모델들을 로드하는 것  
blobFromImage() 사용해 이미지 전처리하고 로드된 사전 학습된 모델로 blob 전달해 예측 결과 얻어냄  
<br>

- readNetFrom  
- blobFromImage  
- setInput  
- forward  
<br>

opencv는 caffe, tensorflow, torch, darknet의 모델 및 omnk 형식의 모델 지원  
-> 모델 로딩하고 자신의 유스케이스에 대한 환경설정 파일만 로드하면 됨  
<br>

따라서 readNetFromCaffe는 네트워크 아키텍처에 대한 텍스트 설명 파일인 prototxt 경로와  
훈련 모델 있는 caffemodel 파일의 경로를 인수로 받음  
blobFromImage는 이미지에서 4차원 blob 만들고 선택적으로 크기 조정 가능  
<br>  

setInput 메서드 사용시 blobFromImage를 네트워크에 대한 입력으로 사용해 만든 blob 설정  
<br>

forward 사용시 네트워크 통해 forward 패스 수행해 결과 예측 생성 가능  
<br> 

## blob
- 동일한 방식으로 전처리된 동일한 너비, 높이 및 채널 수 가진 하나 이상의 이미지  
- 하나의 이미지는 blobFromImage에 전달,  
  두 개 이상 이미지는 blobFromImags 사용  
- 함수의 출력 값: 4차원 텐서  
- **NCHW** : C: 채널 수, H: 텐서 높이, W: 텐서 너비  
  -> 이 값들은 blob 객체에 저장된 후 훈련된 모델로 전달됨  
<br> 

blobFromImage는 이미지에서 4차원 blob 만들고 선택적으로 크기 조정하고 중앙에서 이미지 자르고 평균값 빼는 등의 작업 수행  
```blob = cv2.dnn.blobFromImage(image, scalefactor, size, mean, swapRB, crop, ddepth)```
<br> 

- input Image: 신경망 통과할 이미지  
- scalefactor 사용시 선택적으로 특정 요소만큼 이미지 크기 늘리거나 줄일 수 있음  
- size: 신경망이 예상하는 이미지의 크기 나타냄  
- 평균: 각 채널에서 빼야하는 R, G, B값 나타냄  
- swapRB: 첫 번째와 마지막 채널 교환  
- crop: 크기 조정한 루 이미지를 자를지 여부
  -> 가본적으로 자르기는 수행되지 않음  
  < br>
- ddepth(): 출력 blob의 depth
