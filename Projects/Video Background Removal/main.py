import cv2
import cvzone
import cvzone.FPS
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS,50)

segmentor = SelfiSegmentation()

listImg = os.listdir("Images")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f"Images/{imgPath}")
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,imgList[indexImg],cutThreshold=0.5)

    imageStacked = cvzone.stackImages([img,imgOut],2,1)
    cv2.imshow("Image",imageStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg-=1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg+=1
    elif key == ord('q'):
        break