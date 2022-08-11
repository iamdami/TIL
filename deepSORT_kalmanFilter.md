처음 보는 주제들 여기저기서 빵빵 튀어나오는 중,,,,,  
여태껏 나 왜 못 마주쳤냐!  
재밌는데 정신없어 ~~  

## DeepSORT(Deep Association Metric)  
MOT 보다가 나온 내용.  
<br>
**SORT = Kalman Filter + Hungarian Algorithm  
DeepSORT = deep-learning + SORT**  
<br>

대략 이런 느낌,,  
SORT에 deep-learning 추가된 이유는 이전 속도 기반으로 예측하는 Kalman Filter의 한계 때문인 듯  

- [object-tracking-deepsort](https://nanonets.com/blog/object-tracking-deepsort/)  
- [deep-sort-with-mxnet-yolo3](https://haandol.github.io/2020/02/27/deep-sort-with-mxnet-yolo3.html#fn:5)  
- https://github.com/nwojke/deep_sort  
<br>

## Kalman Filter
- 1960년대 초 루돌프 칼만이 개발한 알고리즘  
- 다음의 2가지 가정이 갖춰진 경우 사용 가능  
  - 모션 모델과 측정 모델이 linear할 경우  
  - 모션 모델과 측정 모델이 Gaussian 분포 따를 경우  
- 상태 예측(state prediction)과 측정 업데이트(measurement update) 반복 수행하며 로봇의 현재 위치 계산  

python은 진짜 최고야 짜릿해  
- [pykalman library도 있어버리기~](https://pykalman.github.io/)  
```
from pykalman import KalmanFilter
import numpy as np

kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])
measurements = np.asarray([[1,0], [0,0], [0,1]])  # 3 observations
kf = kf.em(measurements, n_iter=5)
(filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
```
<br>

- [Sensor Fusion -> Kalman Filter 구체적으로 설명돼있음!](https://medium.com/@celinachild/kalman-filter-%EC%86%8C%EA%B0%9C-395c2016b4d6)  
- [understanding-kalman-filters-with-python -> 사실 이게 더 구체적!](https://medium.com/@jaems33/understanding-kalman-filters-with-python-2310e87b8f48)  

