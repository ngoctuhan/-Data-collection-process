from videoto3D import Videoto3D
from imutils import build_montages
import cv2
video3d = Videoto3D(224, 224, 10)

frames =  video3d.get_frames("SL-PTIT-50/an_mung/N3_an_mung_4.mp4")

frame = build_montages(frames, (156, 156), (3, 3))[0]
title = "ăn mừng"

cv2.imshow(title, frame)
cv2.waitKey(0)

