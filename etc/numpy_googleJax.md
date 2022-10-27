## JAX
Google이 만든 Python과 Numpy만을 결합한 머신러닝 라이브러리  
- Python과 Numpy로 개발됨
- Numpy를 GPU에서 연산시킬 수 있게해 기존 Numpy 성능 뛰어넘음
- 자동 미분 계산
- jit(just in time) 컴파일 기법과 XLA 컴파일러 사용해 컴파일 가능  
- tensor array등을 고려하지 않고 numpy array만을 고려해 코드 짤 수 있음  
- jit 컴파일 데코레이터 함수 적용시 부분 컴파일 가능  

<br>

### 라이브러리 API
- grad, jit : instances of such transformations  
- vmap : automatic vectorization  
- pmap : single-program multiple-data (SPMD) parallel programming of multiple accelerators, with more to come  

<br>

## Tutorial
[jax docs](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html)  
