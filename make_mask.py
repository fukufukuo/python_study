#マスク画像を作る
import numpy as np
import cv2

width = 512
height = 512

mask = np.zeros([width, height,3], np.uint8) #uint8は、符号なし8ビット整数。0~255

#いったんここで画像として出力
zero_img = cv2.imshow('zero_img', mask)
cv2.waitKey(0)
cv2.destroyAllWindows() #真っ黒な画像が出る

#maskの要素を全て255に変える
np.place(mask, mask == 0, 255)
print(mask)

#画像として出力
zero_img = cv2.imshow('zero_img_white', mask)
cv2.waitKey(0)
cv2.destroyAllWindows() #真っ白な画像が出る


