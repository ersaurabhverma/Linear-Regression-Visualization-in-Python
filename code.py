import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
x_ = []
y_ = []
font = cv2.FONT_HERSHEY_SIMPLEX 
org1 = (20, 50) 
org2 = (20, 70) 
org3 = (20, 90)
fontScale = 0.5
color = (255, 255, 255) 
thickness = 1

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        x_.append(x)
        y_.append(y)
        lr = LinearRegression()
        lr.fit(np.array(x_).reshape(-1, 1), np.array(y_).reshape(-1, 1))
        m = lr.coef_[0][0]
        c = lr.intercept_[0]
        print(m,c)
        img[img == 255] = 0
        cv2.putText(img, f'Slope = {m:.4f}', org1, font,  
                   fontScale, color, thickness) 
        
        cv2.putText(img, f'Intercept = {c:.4f}', org2, font,  
                   fontScale, color, thickness) 
        cv2.putText(img, f'Y = {m:.4f} * X + {c:.4f}', org3, font,  
                   fontScale, color, thickness) 
        cv2.line(img, (0, int(c)), (800, int(m*800+c)), (0, 0, 255), 2)
        for ix, iy in zip(x_, y_):
            cv2.circle(img, (ix, iy), 5, (0, 200, 0), -1)


img = np.zeros((600, 800, 3), np.uint8)
cv2.namedWindow('Linear Regression')
cv2.setMouseCallback('Linear Regression', draw_circle)


while 1:
    cv2.imshow('Linear Regression', img)

    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        img = np.zeros((600, 800, 3), np.uint8)
        x_ = []
        y_ = []

