import cv2
LCDH = 107
LCDW = 143
def mergeArea(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (x + i <= 0 or y + j <= 0 or x + i >= LCDH - 1 or y + j >= LCDW - 1):
                continue
            if thresh1[x + i][y + j] == 255:
                thresh1[x + i][y + j] = thresh1[x][y]
                mergeArea(x+i, y + j)



img = cv2.imread('test.jpg', 0)
ret, thresh1 = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
count = 1
for i in range(1, LCDH - 1):
    for j in range(1, LCDW - 1):
        if thresh1[i][j] == 255:
            count += 1
            thresh1[i][j] = count
            if i == 103:
                a = 1
                b = 2
            mergeArea(i, j)
cv2.imshow('result', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
