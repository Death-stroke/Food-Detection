import cv2
import glob
import os
import numpy as np
import scipy.io

#all_imgs=glob.glob("UECFOOD100\\*\\*.jpg")

cls=open("UECFOOD100\\category.txt")
class_names=cls.readlines()
class_names=class_names[1:]
class_names=[class_names[i].split()[1] for i in range(len(class_names))]
cls.close()

imgs=open("UECFOOD100\\multiple_food.txt",'r').readlines()
imgs=imgs[1:]
imgs=[imgs[i].split() for i in range(len(imgs))]

saved_imgs=[]
bb=[]
for i in range(len(imgs)):
    p="UECFOOD100\\"+str(imgs[i][1])+"\\"+str(imgs[i][0])+".jpg"
    print(str(i)+"   "+p)
    im=cv2.imread(p)
    im=cv2.resize(im,(512,512),interpolation=cv2.INTER_AREA)
    cv2.imwrite("UECFOOD100\\food images\\"+os.path.basename(p),im)
    t=imgs[i][0]
    g=[]
    saved_imgs.append(p)
    for j in range(1,len(imgs[i])):
        b=open("UECFOOD100\\"+str(imgs[i][j])+"\\bb_info.txt").readlines()[1:]
        b=[b[k].split() for k in range(len(b))]
        for k in range(len(b)):
            if(t==b[k][0]):
                break
        cx=abs((int(b[k][1])+int(b[k][3]))/2)
        cy=abs((int(b[k][2])+int(b[k][4]))/2)
        w=abs((int(b[k][1])-int(b[k][3])))
        h=abs((int(b[k][2])-int(b[k][4])))
        g.append([imgs[i][j],cx,cy,w,h])
    bb.append([t,g])

with open("UECFOOD100\\food images\\classes.txt",'w') as f:
    for i in class_names:
        f.write(i+"\n")
with open("UECFOOD100\\food images\\bb_inf.txt",'w') as f:
    for i in bb:
        f.write(str(i)+'\n')
with open("UECFOOD100\\food images\\images.txt",'w') as f:
    for i in saved_imgs:
        f.write(os.path.basename(i)+'\n')
