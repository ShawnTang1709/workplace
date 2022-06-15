import numpy as np
import matplotlib.pyplot as plt
import cv2
def aidemy_imshow(name, img):
    b, g, r = cv2.split(img)   #將各種通道的資料拆解出來
    img = cv2.merge([r, g, b]) #依 RGB 的順序再次合併
    plt.title(name)            # 以 matplotlib 繪圖
    plt.imshow(img)
    plt.show()
imgopenCVlogo = cv2.imread("test.jpg") 
#使用matplotlib展示圖片
plt.subplot(111)
plt.imshow(imgopenCVlogo)
plt.title("Original") 

b, g, r = cv2.split(imgopenCVlogo)
 
b

img_1 = cv2.merge([r,g,b])
img_2 = cv2.merge([g,r,b])
img_3 = cv2.merge([r,b,g])

# 在拆分通道時，除了使用OpenCV的split（）方法，還可以用Numpy的索引：
b2 = imgopenCVlogo[:,:,0]   #得到藍色通道 0
g2 = imgopenCVlogo[:,:,1]   #得到綠色通道 1
r2 = imgopenCVlogo[:,:,2]   #得到紅色通道 2

plt.subplot(141);plt.imshow(imgopenCVlogo);plt.title("Original in Matpoltlib")
plt.subplot(142);plt.imshow(img_1);plt.title("Display_RGB")
plt.subplot(143);plt.imshow(img_2);plt.title("Display_GRB")
plt.subplot(144);plt.imshow(img_3);plt.title("Display_RBG")
plt.show()

#--------------------------------------------------------------


img = cv2.imread('test.jpg')   
img.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic Original Image', img)

img_flip = cv2.flip(img, 0)
img_flip.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic 0', img_flip)

img_flipH = cv2.flip(img, 1)
img_flipH.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic 1', img_flipH)
img_flip2 = cv2.flip(img, -1)

plt.subplot(221);plt.imshow(img);plt.title("1")
plt.subplot(222);plt.imshow(cv2.flip(img, 0));plt.title("2")
plt.subplot(223);plt.imshow(cv2.flip(img, 1));plt.title("3")
plt.subplot(224);plt.imshow(cv2.flip(img, -1));plt.title("4")
plt.show()

#-----------------------------------------------------------------------------


img5 = cv2.imread('C:/Users/Shawn Tang/Desktop/AI_Class/Class data/Python/AI/OpenVCdata/photo-01/ESO-001/114.jpg')   
img.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic Original Image', img5)

img_flip = cv2.flip(img5, 0)
img_flip.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic 0', img_flip)

img_flipH = cv2.flip(img, 1)
img_flipH.shape
# (3648, 2736, 3)
cv2.imshow2('Sample pic 1', img_flipH)
img_flip2 = cv2.flip(img, -1)

b, g, r = cv2.split(img5)
img_1 = cv2.merge([r,g,b])
img_2 = cv2.merge([g,r,b])
img_3 = cv2.merge([r,b,g])


plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=2.5, hspace=0.5)

plt.subplot(331);plt.imshow(cv2.flip(img_1, 0));plt.title("1")
plt.subplot(332);plt.imshow(cv2.flip(img_2, 0));plt.title("2")
plt.subplot(333);plt.imshow(cv2.flip(img_3, 0));plt.title("3")
plt.subplot(334);plt.imshow(cv2.flip(img_1, 1));plt.title("4")
plt.subplot(335);plt.imshow(cv2.flip(img_2, 1));plt.title("5")
plt.subplot(336);plt.imshow(cv2.flip(img_3, 1));plt.title("6")
plt.subplot(337);plt.imshow(cv2.flip(img_1, -1));plt.title("7")
plt.subplot(338);plt.imshow(cv2.flip(img_2, -1));plt.title("8")
plt.subplot(339);plt.imshow(cv2.flip(img_3, -1));plt.title("9")
plt.show()
#-----------------------------------------------------------------------------

imgopen = cv2.imread("*")
# Select ROI
r = cv2.selectROI(imgopen)
# Crop image
imCrop = imgopen[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
# Display cropped image
pic = "Test"
cv2.imwrite(str(pic)+'.jpg', imCrop)


import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
fnums = []
for i in glob.glob('*.jpg'):
    fnums.append(int(i.split('.')[0][1:]))
fnums.sort()
img = cv2.imread('I80.jpg', cv2.IMREAD_UNCHANGED)
roi = cv2.selectROI(img)
files = []
for i in fnums:
    img = cv2.imread('I' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
    img = img[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
    files.append(img)