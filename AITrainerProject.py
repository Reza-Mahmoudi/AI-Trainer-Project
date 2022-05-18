import cv2
import numpy as np
import  time
import  PoseModule as pm

cap =cv2.VideoCapture(0)
detector = pm.poseDetector()
count=0
dir=0
ptime=0
while True:
    success , img = cap.read()
    img = cv2.resize(img,(1280,720))
    #img = cv2.imread("AiTrianer/2.jpg")
    img = detector.findPose(img,False)
    lmlist = detector.findPosition(img,False)
    #print(lmlist)
    if len(lmlist) !=0:
        #Right Arm
        angle= detector.findangle(img,12,14,16)
        per = np.interp(angle,(210,310),(0,100))
        bar = np.interp(angle,(220,320),(650,100))
        print(angle,per)



        #cheak  for the dumbel curles
        color = (255,255,0)
        if per==100:
            color = (0, 255, 0)
            if dir==0:
                count +=0.5
                dir = 1
        if per==0:
            color = (0, 0, 255)
            if dir==1:
                count +=0.5
                dir=0
        print(count)

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

        ctime= time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img, f'fps:{str(int(fps))}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)
        # left Arm
        #angle = detector.findangle(img, 11, 13, 15)
    cv2.imshow("image ",img)
    cv2.waitKey(1)
