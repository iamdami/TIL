## RCNN
![image](https://user-images.githubusercontent.com/50016477/163913674-d8e7557c-0fb8-44e4-901e-7b7ff6163919.png)

- Region Proposal + Convolutional Neural Network (CNN)  
- 최초의 deeplearning 기술 적용된 Object Detection model  
-  Image classification 수행하는 CNN과 image에서 object가 존재할 영역 제안해주는 region proposal algorithm 연결해 
  높은 성능의 object detection 수행할 수 있음을 제시해 준 논문  
<br>

### RCNN 수행 과정
1. 이미지를 입력으로 받음  
2. 이미지로부터 약 2000개 가량의 region proposal 추출(Selective search 활용)  
3. 각 region proposal 영역을 이미지로부터 잘라내고(cropping) 동일한 크기로 만든 후(warping), CNN 활용해 feature 추출  
4. 각 region proposal feature에 대한 classification 수행  
-> localization 성능 취약할 수 있음  
<br>

=> Fast RCNN  
<br>

### RCNN Reference
- [R-CNNs Tutorial](https://blog.lunit.io/2017/06/01/r-cnns-tutorial/?)  
- [RCNN](https://89douner.tistory.com/88?category=878735)  
- [RCNN (object detection)](https://dbstndi6316.tistory.com/271)  
<br>

RCNN에 왜 왔냐면 COCO paper Abstract에서  
'Deformable Parts Model 이용한 bounding box와 segmentation detection 결과에 대한 baseline의 성능 분석 제공'  
한대서 DPM이 모야!!?  
<br>

## DRM
- DPM (Deformable Parts Model)
![image](https://user-images.githubusercontent.com/50016477/163913937-a79114bb-9a85-482a-8c25-7e6b12ad39d7.png)  

Deformable Part is a discriminatively trained, multi-scale model  
for image training that aim at making possible the effective use of more latent information  
such as hierarchical (grammar) models and models involving latent three dimensional pose.  
<br>

### DRM Reference
- [Lec21-Deformable Part Models](https://www.cs.ucf.edu/~bagci/teaching/computervision16/Lec21.pdf)  
<br>

### video analysis
조사 중인데 color model에도 적용할 수 있을 것 같은 reference 찾았다
![image](https://user-images.githubusercontent.com/50016477/163952446-5891c856-e665-4be1-8e16-4bc67a02501c.png)  

This is a very powerful technique, and it only uses computer vision. We don’t need a single neural network to do this. To summarize this process:
1. We receive the initial object to track using a bounding box  
2. We compute a color histogram of this object  
3. We compute the color of the background (near the object)  
4. we remove the object color from the total image  
5. We now have a color-based obstacle tracker  
6. 
--- 나머지 조사 내용은 월요일에! ---
