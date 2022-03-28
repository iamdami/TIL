LFW
===
- [LFW](http://vis-www.cs.umass.edu/lfw/#resources)  
  - Labeled Faces in the Wild, a database of face photographs designed for studying the problem of unconstrained face recognition. The data set contains more than 13,000 images of faces collected from the web. Each face has been labeled with the name of the person pictured.  
  - [LFW offers splits for train and test](http://vis-www.cs.umass.edu/lfw/#views)  
- [Calculate LFW accuracy](https://stackoverflow.com/questions/60504959/how-to-calculate-lfw-accuracy-of-a-face-recognition-model)  
- [The definition of FPR, TPR, and TP, FN, TP, TN](https://en.wikipedia.org/wiki/Confusion_matrix)  
- [Facenet github repo - learn how to draw the ROC curve and compute u and S_E](https://github.com/davidsandberg/facenet/wiki/Validate-on-LFW)  
- LFW adopts ROC curve  
- ```u``` : mean classification accuracy  
- ```S_E``` : standard error of the mean(the tables)  
- LFW에서 사용되는 ROC curve는 늘 "plot"  
  -> FPR(false positive rates)  
     TPR(true positive rates)  
<br>

Confusion matrix
===
- special kind of contingency table, with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table)  
- [Confusion matrix (TP, TN, FP, FN) 및 단일/다중 클래스 평가 방법](https://neosla.tistory.com/18)  
- [Confusion matrix - more detailed](https://koreapy.tistory.com/896)  
<pre>
TP : True positive, True인데 분류모델에서 예측이 True라고 판단된 경우 
TN : True negative, False인데 분류모델에서 예측이 False라고 판단된 경우 
FP : False positive, False인데 분류모델에서 예측이 True라고 판단된 경우 
FN : False negative, True인데 분류모델에서 예측이 False라고 판단된 경우
</pre>

