#code that makes the photos
from time import sleep
from picamera import PiCamera
import cv2
import numpy as np
from fastiecm import fastiecm
from orbit import ISS
from skyfield.api import load


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



ephemeris = load('de421.bsp')
timescale = load.timescale()

while True:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        #there is light: we run our experiment

        camera = PiCamera()
        camera.resolution = (1296,972) #qui dobbiamo scegliere la risoluzione delle immagini che vogliamo 
        camera.start_preview()
        for i in range(1):   #all'interno dell' range dobbiamo scegliere quante foto fare scattare al programma durante le tre ore
            # Camera warm-up time
            sleep(2)
            camera.capture("img/image%s.jpg" % i) 
            # load the original img
            original = cv2.imread("imgage%s.jpg" % i)
            contrasted = contrast(original)
            ndvi = calc_ndvi(contrasted)
            ndvi_contrasted = contrast(ndvi)
            # color map the dark ndvi contrasted img
            color_mapped_prep = ndvi_contrasted.astype(np.uint8)
            color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
            cv2.imwrite("img/imageNdvi%s.jpg" % i, color_mapped_image)
            
    else:
        #is dark
        b=1