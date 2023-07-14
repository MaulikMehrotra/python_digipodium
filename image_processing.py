import cv2
import numpy as np
im1=cv2.imread(r'C:\Users\MAULIK MEHROTRA\Desktop\The Batman (2022) [1080p] [WEBRip] [5.1] [YTS.MX]\www.YTS.MX.jpg')
#resize the image
im2=cv2.resize(im1,(800,800))#width height
im3=cv2.resize(im1,None,fx=0.5,fy=0.5)#scalex scaley
#rotate image
im4=cv2.rotate(im1,cv2.ROTATE_90_CLOCKWISE)
im5=cv2.rotate(im1,cv2.ROTATE_90_COUNTERCLOCKWISE)
im6=cv2.rotate(im1,cv2.ROTATE_180)


#filters
im7=cv2.GaussianBlur(im1,(5,5),0) #(image,kernel size,sigma)
im8=cv2.GaussianBlur(im1,(7,7),10) #(image,kernel size,sigma) kernel size can only be odd numbers
im9=cv2.addWeighted(im1,0.5,im7,0.5,0)
gray=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(im1,cv2.COLOR_BGR2HSV)
gray3=np.dstack((gray,gray,gray))
print(gray3.shape)
color_filter_stack=np.hstack((gray3,rgb,hsv))

cv2.imshow('Original',im1)
cv2.imshow('Resize',im2)
cv2.imshow('Resize2',im3)
cv2.imshow('Rotate 90 clockwise',im4)
cv2.imshow('Rotate 90 counter clockwise',im5)
cv2.imshow('Rotate 180',im6)
cv2.imshow('filter',im7)
cv2.imshow('filter2',im8)
cv2.imshow('weighted',im9)
cv2.imshow('color1',gray)
cv2.imshow('color2',rgb)
cv2.imshow('color3',hsv)
cv2.imshow('stack',color_filter_stack)
cv2.waitKey(0)