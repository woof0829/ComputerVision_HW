import math
from Image import Image
import matplotlib.pyplot as plt
from DetectionRelated import DetectionRelated
# Canny

threlow = 100
threup = 2*threlow
tempvalue = 0
image = Image()
imagepatch = image.imagegenerate()
detection = DetectionRelated()
judgepixel = detection.judgepixel(matrix=imagepatch)
gradvalue = judgepixel[3] #梯度值
gradx = judgepixel[1]
grady = judgepixel[2]
angle = math.atan(grady[7, 7]/gradx[7, 7])
NMS_val0 = detection.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=9, value2=7, value3=7, value4=9)
NMS_val1 = detection.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=8, value2=7, value3=8, value4=9)
NMS_val2 = detection.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=7, value2=7, value3=9, value4=9)
NMS_val3 = detection.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=7, value2=8, value3=9, value4=8)
nonmaxsup = detection.processofNMS(gradvalue[0], angle=angle, value0=NMS_val0, value1=NMS_val1, value2=NMS_val2, value3=NMS_val3)
cannythre = detection.cannythre(threlow=100, value=nonmaxsup, image=imagepatch)
for i in range(6, 9):
    for j in range(6, 9):
        if not (i == 7 and j == 7):
            grad = detection.judgepixel(imagepatch, value1=i, value2=j)
            if grad >= threup:
                tempvalue += 1
if tempvalue > 0:
    imagepatch[7, 7] = 255
else:
    imagepatch[7, 7] = 0
imageshow = plt.imshow(imagepatch, cmap='gray', interpolation='nearest')
plt.show(imageshow)
