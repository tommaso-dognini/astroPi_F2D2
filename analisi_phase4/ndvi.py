# This program is used to calculate ndvi index for every image obtained after it was cropped.
import cv2
import numpy as np
from fastiecm import fastiecm


# function to increase the contrast
def contrast(img):
    in_min = np.percentile(img, 5)
    in_max = np.percentile(img, 95)

    out_min = 0.0
    out_max = 255.0

    out = img - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    return out


# function to culculate the ndvi index
def calc_ndvi(img):
    # create the variabels for the 3 colors channels: red. green and blue
    b, g, r = cv2.split(img)

    # create bottom as the sum of the red and blue channel
    bottom = (r.astype(float) + b.astype(float))

    # initialize bottom
    # to avoid dividing by 0 wich won't give a risult
    bottom[bottom == 0] = 0.01

    # calculate the ndvi index
    ndvi = (b.astype(float) - r) / bottom
    return ndvi


# array with the id numbers of the chosen images (the good ones)
a = [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 86, 87, 89, 90, 91, 92, 94,
     95, 95, 96, 97, 98, 99, 120, 121, 122, 123, 130, 131, 277, 278, 279, 296, 297, 298, 299]

chosen = [63, 68, 90, 91, 95, 97, 130, 131, 278, 270, 299]
# repeat the process for every image
for i in [279]:
    # load the original img
    original = cv2.imread(f'img/chosen/{i}.png')
    contrasted = contrast(original)

    #contrasted = contrast(original)
    ndvi = calc_ndvi(contrasted)
    ndvi_contrasted = contrast(ndvi)

    # color map the dark ndvi contrasted img
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    # save the ndvi image
    cv2.imwrite(f'img/chosen/ndvi{i}.jpg', color_mapped_image)
