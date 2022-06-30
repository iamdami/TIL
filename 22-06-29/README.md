## ViT
- Image의 patch에 대해 Transformer와 비슷한 architecture를 채용하는 image classification model  
- 한 image는 fixed-sized patch들로 나눠짐  
- 각 fixed-sized patch은 선형적으로 embedding되고 위치 embedding이 추가됨  
- Vector들의 결과 sequence는 standard Transformer ecoder로 넣어짐  
- Classification을 수행하기 위해 여분의 학습 가능한 classification token을 해당 sequence에 추가하는 standard한 접근법이 사용됨  

![image](https://user-images.githubusercontent.com/50016477/176384438-7a4637e9-bd5c-481e-ac86-891f372814f9.png)


[paper - AN IMAGE IS WORTH 16X16 WORDS:
TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE](https://arxiv.org/pdf/2010.11929.pdf)  
- [paper review -  AN IMAGE IS WORTH 16X16 WORDS:
TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE](https://hipgyung.tistory.com/entry/%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-ViTVision-Transformer-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-An-Image-is-Worth-16x16-Words-Transformers-for-Image-Recognition-at-Scale)  
- [paper review - ATTENTION-IS-ALL-YOU-NEED](https://hipgyung.tistory.com/entry/ATTENTION-IS-ALL-YOU-NEED-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0)  
- [kaggle - vit-tutorial-baseline](https://www.kaggle.com/code/abhinand05/vision-transformer-vit-tutorial-baseline/notebook)  
- [hands-on-guide-to-using-ViT-for-image-classification - keras](https://analyticsindiamag.com/hands-on-guide-to-using-vision-transformer-for-image-classification/)  
- [hands-on-guide-to-using-ViT-for-image-classification - pytorch](https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/)  

[LeViT : a Vision Transformer in ConvNet's Clothing for Faster Inference](https://github.com/facebookresearch/LeViT)  
