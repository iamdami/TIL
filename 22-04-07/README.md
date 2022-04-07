## FCOS: Fully Convolutional One Stage Detector
- per-pixel prediction 방식으로 Object Detection을 재구성  
- multi-level prediction 사용해 recall 개선  
- overlapped bounding box로 인한 모호성 해결하는 방법 제안  
- low-quality detected bounding boxes 억제하고 전체 성능 크게 향상시키는 “centerness” 개념 소개  
- [FCOS 설명 - youtube](https://youtu.be/_ADYE6QaAAY)  
- [FCOS - paper review](https://eehoeskrap.tistory.com/624)  
- [FCOS - github](https://github.com/tianzhi0549/FCOS)  
<br>

## Mask Scoring
CenterMask paper에 등장  
- 예측한 Mask의 quality 고려해 classification score 재조정하는 방법  
- [Mask Scoring - paper review](https://junha1125.github.io/blog/artificial-intelligence/2021-03-09-MaskScore/)  
