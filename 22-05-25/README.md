## Trained model save, load in Pytorch  
- [Pytorch에서 학습한 모델 저장 및 불러오기](https://justkode.kr/deep-learning/pytorch-save)  
  - **torch.save**: 객체를 디스크에 저장. pickle 모듈 이용해 객체 직렬화 하며, 이 함수 사용해 모든 종류의 모델, Tensor 등 저장 가능  
  - **torch.load**: pickle 모듈 이용해 객체 역직렬화 후 메모리에 할당  
  - **torch.nn.Module.load_state_dict**: 역직렬화된 state_dict 사용해 모델 매개변수들 불러옴
    state_dict는 각 weight를 매개변수 Tensor로 매핑한 Python dict 객체  
- https://tutorials.pytorch.kr/beginner/saving_loading_models.html  
![image](https://user-images.githubusercontent.com/50016477/170160464-52384a13-54e7-446a-92d0-894411844ccd.png)  

<br>

