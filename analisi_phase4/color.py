from cProfile import label
import fontTools
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

# This program is used to calculate ndvi index for every image obtained after it was cropped.


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


chosen = [63, 68, 90, 91, 95, 130, 131, 278, 270, 299]

for i in [299]:
    # load the original img
    original = cv2.imread(f'img/chosen/{i}.png')
    contrasted = contrast(original)

    #contrasted = contrast(original)
    ndvi = calc_ndvi(contrasted)
    ndvi_contrasted = contrast(ndvi)

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 6))
    # ax0
    ax0.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.set_title('IR', fontsize=20)

    # ax1
    imgplot = plt.imshow(ndvi_contrasted)
    imgplot.set_cmap('YlGn')
    cbar = plt.colorbar(orientation="vertical", shrink=1, pad=0.05, aspect=20)
    # cbar.set_label(label='NDVI')
    cbar.set_ticks([])
    plt.clim(0, 255)
    plt.yticks([])
    plt.xticks([])
    ax1.set_title('NDVI', fontsize=20)

    fig.savefig(f'img/chosen/color{i}.jpg', dpi=300)
