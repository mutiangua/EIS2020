from mcpi. minecraft import Minecraft
import mcpi. block as block
import numpy as np
import cv2
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

a=70
b=70

img= cv2. imread("xia.jpg")
#height,width=img.shape[:2]
#size=(int(width*0.1),int(height*0.1))
#img=cv2.resize(img,size,interpolation=cv2.INTER_AREA)
print(len(img[0]))
print(len(img))
GrayImage=cv2.cvtColor (img,cv2. COLOR_BGR2GRAY)
ret, thresh1=cv2.threshold(GrayImage,0,255,cv2.THRESH_BINARY)
resized_image =~ cv2. resize (thresh1, (b, a))

for i in range (a):
  for j in range(b):
        mc.setBlock(pos.x+a-i-1,pos.y,pos.z+j,173) 
        #time. sleep(0.1)
        #print("finish")
for i in range (a):
  for j in range(b):
        if resized_image[i][j]==0:
          mc.setBlock(pos.x+a-i-1,pos.y,pos.z+j,80)
          #print("end")
