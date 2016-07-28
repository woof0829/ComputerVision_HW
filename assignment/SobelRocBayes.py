import math
from Image import Image
import matplotlib.pyplot as plt
from ImageRelated import ImageRelated
from DetectionRelated import DetectionRelated

thresholdnum = 50
imagenum = 1000
# Class initialize
image = Image()
imagepatch = image.imagegenerate()
imagerela = ImageRelated()
detectrela = DetectionRelated()
emptyarray = imagerela.empty_array(thresholdnum)
frac_trueposi = emptyarray
frac_falseposi = emptyarray
trueposi = emptyarray
falseposi = emptyarray
trueneg = emptyarray
falseneg = emptyarray
thre = emptyarray
risk = emptyarray
mask_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
mask_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
# the range of sobel threshold
for m in range(thresholdnum):
    thre[m] = 10*m
for i in range(thresholdnum):
    for j in range(thresholdnum):
        grad_temp = detectrela.judgepixel(imagerela, value1=7, value2=7)
        grad = grad_temp[0]
        if location[1, j] < 0.5*size*(math.sin(angle[1, j]))+math.cos(angle[1, j]) and grad >= thre[1, i]:
            trueposi[i] += 1
        elif location[1, j] >= 0.5*size*(math.sin(angle[1, j]))+math.cos(angle[1, j]) and grad >= thre[1, i]:
            falseposi[i] += 1
        elif location[1, j] >= 0.5*size*(math.sin(angle[1, j]))+math.cos(angle[1, k]) and grad >= thre[1, i]:
            trueneg[i] += 1
        else:
            falseneg[i] += 1

    if trueposi[i] + falseneg[i] == 0 and falseposi[i] +trueneg[i] != 0:
        frac_trueposi[i] = 0
        frac_falseposi[i] = falseposi[i]/(falseposi[i] + trueneg[i])
    elif trueposi[i] + falseneg[i] != 0 and falseposi[i] + trueneg[i]:
        frac_trueposi[i] = trueposi[i]/(trueposi[i]+falseneg[i])
        frac_falseposi[i] = 0
    elif trueposi[i] + falseneg[i] == 0 and falseposi[i] + trueneg[i] == 0:
        frac_falseposi[i] = 0
        frac_trueposi[i] = 0
    else:
        frac_trueposi[i] = trueposi[i]/(trueposi[i]+falseneg[i])
        frac_falseposi[i] = falseposi[i]/(falseposi[i]+trueneg[i])
# the part of bayes risk
    risk[i] = 0.05*(1-frac_trueposi[i]) + (1-0.05)*frac_falseposi[i]