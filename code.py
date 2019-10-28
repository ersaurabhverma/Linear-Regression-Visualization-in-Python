import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
x_ = []
y_ = []


def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        x_.append(x)
        y_.append(y)
        lr = LinearRegression()
        lr.fit(np.array(x_).reshape(-1, 1), np.array(y_).reshape(-1, 1))
        m = lr.coef_
        c = lr.intercept_

        img[img == 255] = 0
        cv2.line(img, (0, c), (800, m*800+c), (0, 0, 255), 2)
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

