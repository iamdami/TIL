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
