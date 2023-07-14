import cv2
import numpy as np
cam=cv2.VideoCapture(r'C:\Users\MAULIK MEHROTRA\Desktop\Ghosted.2023.1080p.WEBRip.1400MB.DD5.1.x264-GalaxyRG[TGx]\Ghosted.2023.1080p.WEBRip.1400MB.DD5.1.x264-GalaxyRG.mkv')#link to webcam
while cam.isOpened():
    status,img=cam.read()
    if status is None:
        break
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    stack=np.hstack((img,rgb))
    resize=cv2.resize(stack,None,fx=0.5,fy=0.5)
    cv2.imshow('Webcam',resize)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cam.release()
