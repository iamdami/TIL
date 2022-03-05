import cv2
import numpy as np
from google.colab.patches import cv2_imshow


# Creating face_cascade and eye_cascade objects
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
# face_cascade와 eye_cascade 생성 -> 감지된 얼굴과 눈 저장할 것

# Loading the image
img = cv2.imread('.jpg')
cv2_imshow(img)

# Converting the image into grayscale
# cascades가 grayscale 이미지에만 작동하기 때문에 이미지를 회색조로 변환해야 함
# 얼굴과 눈을 grayscale 이미지에서 탐지하지만 직사각형은 해당 컬러 이미지에 그림
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating variable faces
faces= face_cascade.detectMultiScale (gray, 1.1, 4)

# Defining and drawing the rectangle around the face
# 네 가지 요소의 튜플 얻을 수 있음
# 여러 인수 필요 -> 1. grayscale된 이미지, 2. 이미지 크기가 얼마나 줄어들 것인지 알려주는 배율, 3. 최소 이웃 수
for(x , y,  w,  h) in faces:
  cv2.rectangle(img, (x,y) ,(x+w, y+h), (0,255,0), 3)
cv2_imshow(img)

# Creating two regions of interest
# 직사각형 내부에 위치할 두 관심영역 만들기
# 1. 눈 감지할 회색조 이미지의 영역, 2. 직사각형 그릴 컬러 이미지 영역
roi_gray=gray[y:(y+h), x:(x+w)]
roi_color=img[y:(y+h), x:(x+w)]

# Creating variable eyes
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
index=0
# Creating for loop in order to divide one eye from another
# 첫 번째 눈과 두 번째 눈의 좌표를 각각 변수에 저장
for (ex , ey,  ew,  eh) in eyes:
  if index == 0:
    eye_1 = (ex, ey, ew, eh)
  elif index == 1:
    eye_2 = (ex, ey, ew, eh)
    
# Drawing rectangles around the eyes
  cv2.rectangle(roi_color, (ex,ey) ,(ex+ew, ey+eh), (0,0,255), 3)
  index = index + 1
cv2_imshow(img)

# 더 작은 눈이 left eye
if eye_1[0] < eye_2[0]:
   left_eye = eye_1
   right_eye = eye_2
else:
   left_eye = eye_2
   right_eye = eye_1
  
# Calculating coordinates of a central points of the rectangles
# 직사각형 중심점 좌표 계산
# 인덱스 0: x좌표, 인덱스 1: y좌표, 인덱스 2: 직사각형 너비, 인덱스 3: 직사각형 높이
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
left_eye_x = left_eye_center[0] 
left_eye_y = left_eye_center[1]
 
right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]
 
cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0) , -1)
cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0) , -1)
cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)

# 수평선 그리고 그 선과 두 중심점 연결하는 선 사이 각도 계산
# 목표: 이 각도를 기준으로 이미지 회전
# 만약 왼쪽 눈의 y좌표가 오른쪽 눈의 y좌표보다 크면 이미지를 시계 방향으로 회전해야 하고
# 그렇지 않다면 이미지를 시계 반대 방향으로 회전
if left_eye_y > right_eye_y:
   A = (right_eye_x, left_eye_y)
   # Integer -1 indicates that the image will rotate in the clockwise direction
   direction = -1 
else:
   A = (left_eye_x, right_eye_y)
  # Integer 1 indicates that image will rotate in the counter clockwise  
  # direction
   direction = 1 

cv2.circle(roi_color, A, 5, (255, 0, 0) , -1)
 
cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)
cv2.line(roi_color,left_eye_center, A,(0,200,200),3)
cv2.line(roi_color,right_eye_center, A,(0,200,200),3)
cv2_imshow(img)

# 각도를 계산하려면 직각 삼각형의 두 다리 길이 먼저 찾아야 함
# 그 후 공식 이용해 필요한 각도 구할 수 있음
delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_y
angle=np.arctan(delta_y/delta_x)
angle = (angle * 180) / np.pi

# np.arctan 에서 함수가 각도를 라디안 단위로 반환한다는 점에서 유의
# Width and height of the image
h, w = img.shape[:2]
# 결과를 각도로 반환하려면 angle 𝜃에 180을 곱하고 𝜋로 나눠야 함
# Calculating a center point of the image
# Integer division "//"" ensures that we receive whole numbers
center = (w // 2, h // 2)
# Defining a matrix M and calling
# cv2.getRotationMatrix2D method
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
# Applying the rotation to our image using the
# cv2.warpAffine method
rotated = cv2.warpAffine(img, M, (w, h))
cv2_imshow(rotated)

# Width and height of the image
h, w = img.shape[:2]
#각도 별로 이미지 회전 가능
# Calculating a center point of the image
# Integer division "//"" ensures that we receive whole numbers
center = (w // 2, h // 2)
# Defining a matrix M and calling
# cv2.getRotationMatrix2D method
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
# Applying the rotation to our image using the
# cv2.warpAffine method
rotated = cv2.warpAffine(img, M, (w, h))
cv2_imshow(rotated)

# calculate distance between the eyes in the first image
dist_1 = np.sqrt((delta_x * delta_x) + (delta_y * delta_y))

# 이미지에서 눈 사이 거리를 참조 프레임으로 사용할 이미지 크기 조정해야 함
# 먼저 이 거리를 계산해야 함
# calculate distance between the eyes in the second image
dist_2 = np.sqrt((delta_x_1 * delta_x_1) + (delta_y_1 * delta_y_1))

# 이미 직각 삼각형의 두 변 길이 계산헸으므로 피타고라스 정리 사용해 빗변 나타내는 눈 사이의 거리 계산 가능
# 이 코드로 다른 모든 사진에 대해서도 동일한 작업 수행 가능
# 그 후 이 결과의 비율 계산하고, 해당 비율에 따라 이미지 크기 조정 가능
#calculate the ratio
ratio = dist_1 / dist_2

# Defining the width and height
h=476
w=488
# Defining aspect ratio of a resized image
dim = (int(w * ratio), int(h * ratio))
# We have obtained a new image that we call resized3
resized = cv2.resize(rotated, dim)
cv2_imshow(resized)

