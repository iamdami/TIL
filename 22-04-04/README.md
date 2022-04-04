## Non-maximum Suppression (NMS)  
- [NMS](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c)  
  - **Input**: A list of Proposal boxes B, corresponding confidence scores S and overlap threshold N.  
  - **Output** : A list of filtered proposals D.  
  - **Algorithm**:
Select the proposal with highest confidence score, remove it from B and add it to the final proposal list D.(Initially D is empty).  
Now compare this proposal with all the proposals — calculate the IOU (Intersection over Union) of this proposal with every other proposal. If the IOU is greater than the threshold N, remove that proposal from B.
Again take the proposal with the highest confidence from the remaining proposals in B and remove it from B and add it to D.  
Once again calculate the IOU of this proposal with all the proposals in B and eliminate the boxes which have high IOU than threshold.  
This process is repeated until there are no more proposals left in B.  

난 이걸 왜 비최대억제라고 어렵게 말하는지 모르겠어~_~  
<br>

### NMS Algorithm
![image](https://user-images.githubusercontent.com/50016477/161475001-b69089ee-7b82-4fc2-8b3d-1da6ea31bdc0.png)  
1. B 초기화(proposal boxes)
2. 모든 box에 대해 bool variable 갖게 하고 False로 set
  -> bool variable은 b[i]가 남겨져야 할 지, 제거돼야 할 지 indicate
3. b[i]들끼리 비교해 줄 또다른 loop 시작
4. if both box들이 같은 IoU 가졌을 경우, 점수 비교 후 b[i] 점수가 그것의 b[j]보다 작다면, b[i]는 제거됨
  -> flag True로 set  
5. b[i]가 다른 box들과 비교되었고, 아직 제거된 flag가 False라면, b[i]는 고려되어야 함  
  -> final list에 더해짐  
6. 남은 box들에 대해 같은 프로시저 진행, final list return  
<br>

## LFW
- [retinaface test1](https://github.com/AlexandrWh/FaceID/blob/120cba62db56da696a1ef970fa8b0f4f1a81cd3e/retinaface/detector.py)  
- [retinaface test2](https://intrepidgeeks.com/tutorial/pytorch-retinaface-test)  
- 
