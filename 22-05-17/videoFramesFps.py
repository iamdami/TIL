import cv2

data = cv2.VideoCapture("video_path")
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(data.get(cv2.CAP_PROP_FPS))
print(f"frames: {int(frames)}, fps: {fps}")
