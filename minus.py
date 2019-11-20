import math
import cv2
import numpy as np

img1 = cv2.imread("/Users/a1230119/Desktop/test/t.png", 0)
print(img1.shape)
#img2 = cv2.imread("/Users/a1230119/Desktop/test/2.png", 0)
#img3 = cv2.imread("/Users/a1230119/Desktop/test/8.png", 0)

for i in range(10):
    img = cv2.imread("/Users/a1230119/Desktop/test/{:d}.png".format(i), 0)
    #print(img.shape)
    print("i=", i)
    print(np.sum(img1-img))

# folder 0_2 : loss = 73806221
# folder 1_8 : loss = 389166284
# folder 2_4 : loss = 81096695
# folder 3_7 : loss = 285060144
# folder 5_5 : loss = 72193698
# folder 6_2 : loss = 268058239
# folder 9_7 : loss = 262806684
# folder 38_2 : loss = 43424473
# folder 39_9 : loss = 217095244
