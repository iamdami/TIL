- [CNN BottleNeck](https://coding-yoon.tistory.com/116)  
- [Does MaxPooling reduce overfitting?](https://stackoverflow.com/questions/59717290/does-maxpooling-reduce-overfitting)  
  - 응 절대 아니지~  
  <pre>DONT use max pooling for the purpose of reducing overfitting 
  because it's is used to reduce the rapresentation 
  and to make the network a bit more robust to some features, 
  further more using it so much will make the network more and more robust 
  to a some kind of featuers.</pre>  
- [stochastic pooling](https://blog.naver.com/laonple/220830178487)  
  - max pooling과 average pooling의 문제점 해결 위해 고안된 방법  
  - 단순히 activation 선택하거나 모든 activation 평균 구하는 게 아니라 drop out과 마찬가지로 확률 p에 따라 적절한 activation 선택  
- [pooling layer](https://kevinthegrey.tistory.com/142)  
- [Keras - pooling layers](https://keras.io/api/layers/pooling_layers/)  
- [padding](https://ardino.tistory.com/40)  
  - valid padding: padding 추가하지 않은 형태
    valid padding 적용 후 필터 통과시키면 그 결과는 항상 입력 사이즈보다 작게 됨  
  - full padding: 입력 데이터의 모든 원소가 합성곱 연산에 같은 비율로 참여하도록 하는 형태
  - same padding(half padding): 출력 크기를 입력 크기와 동일하게 유지하는 형태  
- [overfitting 해결 - Regularization(규제화)](https://warm-uk.tistory.com/51)  
- [Dropout Regularization (C2W1L06)](https://www.youtube.com/watch?v=D8PJAL-MZv8)  
- [](https://tutorials.pytorch.kr/beginner/blitz/neural_networks_tutorial.html)  
  - nn은 모델 정의하고 미분하는데 autograd 사용  
- https://pytorch.org/docs/stable/nn.functional.html#convolution-functions  
  - pytorch Convolution functions  
- [Pooling Layers for Convolutional Neural Networks](https://machinelearningmastery.com/pooling-layers-for-convolutional-neural-networks/)  
  - Pooling is required to down sample the detection of features in feature maps.  
  - How to calculate and implement average and maximum pooling in a convolutional neural network.  
  - How to use global pooling in a convolutional neural network.  
- [Source code for bob.learn.pytorch.architectures.LightCNN](https://www.idiap.ch/software/bob/docs/bob/bob.learn.pytorch/stable/_modules/bob/learn/pytorch/architectures/LightCNN.html)  
  - https://github.com/AlfredXiangWu/LightCNN 찾았어요 선생님...


<br>
제발 대충 좀 보자,,,,,,,,,,,,  

공부를 어디서 멈출지 아는 것도 중요행,..  
