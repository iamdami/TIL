실시간 감정 인식 때 잠깐 맛 봤던 MTCNN
## MTCNN(Multi-task Cascaded Convolutional Neural Networks)  
- [Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks](https://arxiv.org/abs/1604.02878)  
- [MTCNN 논문 리뷰 1](https://yeomko.tistory.com/16)  
- [MTCNN 논문 리뷰 2](https://dyddl1993.tistory.com/29)  

![image](https://user-images.githubusercontent.com/50016477/169724770-fb2a2f9e-7b32-4761-b9ef-2cacafa18ccd.png)  
<br>

![image](https://user-images.githubusercontent.com/50016477/169724813-c424ccee-9da0-4662-82e1-640afa393c68.png)  
<br>

Proposal Network, Refine Network, O-Net은 Output Network인가,, 논문에 안나와있넹  
<br>

- 얼굴 검출, 랜드마크 검출, 그리고 Bounding box regression 세 개 태스크를 함께 학습하는 Joint learning 방식 사용  
- MTCNN은 높은 성능을 보이고, 랜드마크를 함께 표시할 수 있기 때문에 다양한 활용이 가능하다는 장점 존재  
- 다만 프로젝트 적용에 있어서 생각보다 많은 자원 사용되며, 특히 속도상에 이점을 가지기 어려움  
- 마스크 착용 영상에 대해 랜드마크 오탐 잦음  
