import dlib
import cv2
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

ALL = list(range(0, 68))
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17)) # index 1, 15 = 옆광대

index = ALL

image = cv2.imread("7.jpg")
image2 = cv2.imread("8.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

for face in rects:
    shape = predictor(gray, face)

    list_points = []
    for p in shape.parts():
        list_points.append([p.x, p.y])

    list_points = np.array(list_points)

    '''for i, pt in enumerate(list_points[JAWLINE]):
        pt_pos = (pt[0], pt[1])
        if (i == 3 or i == 4 or i == 5):
            cv2.circle(image, pt_pos, 2, (0, 255, 0), -1)
            print(i, pt_pos)'''

    for i, pt in enumerate(list_points[ALL]):
        pt_pos = (pt[0], pt[1])
        cv2.circle(image, pt_pos, 2, (0, 255, 0), -1)


x = (list_points[JAWLINE][3]-list_points[JAWLINE][4])[0]
y = (list_points[JAWLINE][3]-list_points[JAWLINE][4])[1]
print(y/x) # 기울기 사각턱이면 점간의 기울기가 더 클 것으로 예상
'''print((list_points[NOSE][6]-list_points[RIGHT_EYEBROW][4])[1],": 중안부 좌표 길이") # 중안부 좌표 길이
print((list_points[JAWLINE][8]-list_points[NOSE][6])[1],": 하안부 좌표 길이") # 하안부 좌표 길이'''
cv2.imshow("5", image)

gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

for face in rects:
    shape = predictor(gray, face)

    list_points = []
    for p in shape.parts():
        list_points.append([p.x, p.y])

    list_points = np.array(list_points)

    '''for i, pt in enumerate(list_points[JAWLINE]):
        pt_pos = (pt[0], pt[1])
        #print(i, pt_pos)
        if (i == 3 or i == 4 or i ==5):
            cv2.circle(image2, pt_pos, 2, (0, 255, 0), -1)
            print(i, pt_pos)'''

    for i, pt in enumerate(list_points[ALL]):
        pt_pos = (pt[0], pt[1])
        cv2.circle(image2, pt_pos, 2, (0, 255, 0), -1)

x = (list_points[JAWLINE][3]-list_points[JAWLINE][4])[0]
y = (list_points[JAWLINE][3]-list_points[JAWLINE][4])[1]
print(y/x)

'''print((list_points[NOSE][6]-list_points[RIGHT_EYEBROW][4])[1],": 중안부 좌표 길이") # 중안부 좌표 길이
print((list_points[JAWLINE][8]-list_points[NOSE][6])[1],": 하안부 좌표 길이") # 하안부 좌표 길이'''

#cv2.imshow("Output", image)
cv2.imshow("6", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()