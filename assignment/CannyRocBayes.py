import math
from Image import Image
import matplotlib.pyplot as plt
from ImageRelated import ImageRelated
from DetectionRelated import DetectionRelated

thresholdnum = 500
imagenum = 1000
image = Image()
imagepatch = image.imagegenerate()
imagerela = ImageRelated()
detectrela = DetectionRelated()
emptyarray = imagerela.empty_array(thresholdnum)
emptymatrix = imagerela.empty_matrix(x=3)
frac_trueposi = emptyarray
frac_falseposi = emptyarray
trueposi = emptyarray
falseposi = emptyarray
trueneg = emptyarray
falseneg = emptyarray
up_threshold = emptyarray
low_threshold = emptyarray
risk = emptyarray
trueposi_0 = 0
trueposi_1 = 0
trueposi_2 = 0
trueposi_3 = 0
g = emptymatrix
mask_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
mask_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
judgepixel = detectrela.judgepixel(matrix=imagepatch)
gradvalue = judgepixel[3]
for i in range(thresholdnum-1):
    low_threshold[i] = 10*i
    up_threshold[i] = 2*low_threshold[i]
for j in range(thresholdnum-1):
    for m in range(imagenum-1):
        grad_temp = detectrela.judgepixel(imagerela, value1=7, value2=7)
        grad = grad_temp[0]
        gradx = grad_temp[1]
        grady = grad_temp[2]
        grad_angle = math.atan(grady/gradx)
        NMS_val0 = detectrela.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=9, value2=7, value3=7, value4=9)
        NMS_val1 = detectrela.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=8, value2=7, value3=8, value4=9)
        NMS_val2 = detectrela.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=7, value2=7, value3=9, value4=9)
        NMS_val3 = detectrela.gradvalue(matrix0=imagepatch, matrix1=gradvalue[7, 7], value1=7, value2=8, value3=9, value4=8)
        grad = detectrela.processofNMS(matrix=imagepatch, angle=grad_angle, value0=NMS_val0, value1=NMS_val1, value2=NMS_val2, value3=NMS_val3)
        if grad >= up_threshold[j]:
            if location[m] < 0.5*size*(math.sin(angle[m]+math.cos(angle[m]))):
                trueposi[j] += 1
            else:
                falseposi[j] += 1
        elif low_threshold[j] > grad:
            if location[m] < 0.5*size*(math.sin(angle[m])+math.cos(angle[m])):
                falseneg[j] += 1
            else:
                trueneg[j] += 1
        else:
            for l in range(6,9):
                for p in range(6,9):
                    g[l-5, p-5] = grad_temp = detectrela.judgepixel(imagerela, value1=l, value2=p)
                    grad = grad_temp[0]
                for a in range(0,3):
                    for b in range(0,3):
                        if g[a,b] >= up_threshold[j] and location[m] < 0.5*size*(math.sin(angle[m]) + math.cos(angle[m])):
                            trueposi_0 += 1
                        elif g[a,b] >= up_threshold[j] and location[m] >= 0.5*size*(math.sin(angle[m]) + math.cos(angle[m])):
                            trueposi_1 += 1
                        elif g[a,b] < up_threshold[j] and location[m] < 0.5*size*(math.sin(angle[m]) + math.cos(angle[m])):
                            trueposi_2 += 1
                        else:
                            trueposi_3 += 1
                if trueposi_0 > 0:
                    trueposi[j] += 1
                elif trueposi_1 > 0:
                    falseposi[j] += 1
                elif trueposi_2 == 9:
                    falseneg += 1
                elif trueposi_3 == 9:
                    trueneg += 1
    if trueposi[j] + falseneg[j] == 0 and falseposi[j] + trueneg[j] != 0:
        frac_trueposi[j] = 0
        frac_falseposi[j] = falseposi[j]/(falseposi[j] + trueneg[j])
    elif trueposi[j] + falseneg[j] != 0 and falseposi[j] + trueneg[j] == 0:
        frac_falseposi[j] = trueposi[j]/(trueposi[j] + falseneg[j])
        frac_trueposi[j] = 0
    elif trueposi[j] + falseneg[j] == 0 and falseposi[j] + trueneg[j]:
        frac_trueposi[j] = 0
        frac_falseposi[j] = 0
    else:
        frac_trueposi[j] = trueposi[j]/(trueposi[j] + falseneg[j])
        frac_falseposi[j] = falseposi[j]/(falseposi[j] + trueneg[j])
    risk[j] = 0.05*(1-frac_trueposi[j]) + (1 - 0.05)*frac_falseposi[j]

roc = plt.plot(frac_falseposi, frac_trueposi)
bayes = plt.plot(low_threshold[thresholdnum], low_threshold)
