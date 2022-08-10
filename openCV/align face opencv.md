align face opencv
===
https://datahacker.rs/010-how-to-align-faces-with-opencv-in-python/
<br>

- face align은 Python에서 좀 더 복잡한 이미지 처리 작업을 시작하기 전에 마스터해야하는 중요한 단계 중 하나  
<br>

##  face alignment?
- face alignment는 입력 이미지(압력 좌표계(input coordinate systems))의 여러 점 집합을 하나의 좌표계로 변환하는 프로세스로 실현될 수 있음  
- 이 좌표계를 출력 좌표계(output coordinate system)라고 부르고 이것을 고정 참조 프레임(stationary reference frame)으로 정의할 수 있음  
- 목표는 입력 좌표를 왜곡하고 변환해 출력 좌표와 정렬하는 것  
- 이를 위해 회전, 이동 및 크기 조정의 세 가지 기본 affine 변환 적용  
- 이런 식으로 얼굴 랜드마크를 입력 좌표계에서 출력 좌표계로 변환 가능  

<br>

## 개괄적 과정
1. 이미지에서 얼굴과 눈 감지  
2. 감지된 눈의 중심 계산  
3. 두 눈의 중심 사이에 선 그리기  
4. 두 눈 사이의 수평선 그리기  
5. 삼각형의 세 모서리 길이 계산  
6. 각도 계산  
7. 계산된 각도로 이미지 회전  
8. 이미지 크기 조정  

<br>

