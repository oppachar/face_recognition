import cv2
import mediapipe as mp
import time

#cap = cv2.VideoCapture("Videos/3.mp4")
pTime = 0

#image = cv2.imread("img/1.jpg")
img = cv2.imread("img/2.jpg")

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceMesh.process(imgRGB)
if results.multi_face_landmarks:
     for faceLms in results.multi_face_landmarks:
       ''' mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS,
                                drawSpec,drawSpec)'''
       for id,lm in enumerate(faceLms.landmark):
                #print(lm)
            ih, iw, ic = img.shape
            x,y = int(lm.x*iw), int(lm.y*ih)
            #cv2.circle(img, (x, y), 2, (0,255,0), -1)
            if (id == 123 or id == 352): # 광대 index에만 점을 찍음
                    print(id,x,y)
                    cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

'''cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime'''
'''cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
            3, (255, 0, 0), 3)'''
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()