#code that makes the photos
from time import sleep
from picamera import PiCamera
from pathlib import Path
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
def calc_ndvi (img):
    #create the variabels for the 3 colors channels: red. green and blue
    b, g, r = cv2.split(img)
    # create bottom as the sum of the red and blue channel 
    bottom = (r.astype(float) + b.astype(float))
    #initialize bottom
    bottom[bottom==0] = 0.01
    # calculate the ndvi index
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

base_folder = Path(__file__).parent.resolve()

camera = PiCamera()
camera.resolution = (1296,972) #qui dobbiamo scegliere la risoluzione delle immagini che vogliamo 
camera.start_preview()
for i in range(1):   #all'interno dell' range dobbiamo scegliere quante foto fare scattare al programma durante le tre ore
    # Camera warm-up time
    sleep(2)
    camera.capture(f"{base_folder}/image%s.jpg" % i)
    # load the original img
    original = cv2.imread('imgage%s.jpg' % i)
    contrasted = contrast(original)
    ndvi = calc_ndvi(contrasted)
    ndvi_contrasted = contrast(ndvi)
    # color map the dark ndvi contrasted img
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    cv2.imwrite(f"{base_folder}/imagendvi%s.jpg" % i, color_mapped_image)

# NDVI INDEX SIMULATION

#import modules
import cv2
import numpy as np
from fastiecm import fastiecm


# load the original img
original = cv2.imread('img/park.png')

# function to dispaly and resize the img
def display(img, img_name):
    # load the img as np array
    img = np.array(img, dtype=float)/float(255)

    # resize the img
    height = int(img.shape[0] / 2)
    width = int(img.shape[1] / 2)
    image = cv2.resize(img, (width, height))
    cv2.namedWindow(img_name)
    cv2.imshow(img_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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
def calc_ndvi (img):
    #create the variabels for the 3 colors channels: red. green and blue
    b, g, r = cv2.split(img)
    
    # create bottom as the sum of the red and blue channel 
    bottom = (r.astype(float) + b.astype(float))
    
    #initialize bottom
    bottom[bottom==0] = 0.01

    # calculate the ndvi index
    ndvi = (b.astype(float) - r) / bottom
    return ndvi



# display the image
display(original, 'Original')

contrasted = contrast(original)
display(contrasted, 'Contrasted original')
#cv2.imwrite('img/Contrasted_original.png', contrasted)

ndvi = calc_ndvi(contrasted)
display(ndvi, 'NDVI')
#cv2.imwrite('img/ndvi.png', ndvi)

ndvi_contrasted = contrast(ndvi)
display(ndvi_contrasted, 'NDVI Contrasted')
cv2.imwrite('img/ndvi_contrasted.png', ndvi_contrasted)

# color map the dark ndvi contrasted img
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
display(color_mapped_image, 'Color mapped')
cv2.imwrite('img/color_mapped_image.png', color_mapped_image)
