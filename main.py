# code that makes the photos
from time import sleep
from picamera import PiCamera
import cv2
import numpy as np
from fastiecm import fastiecm
from orbit import ISS
from skyfield.api import load

# FUNCTIONS

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
    bottom[bottom == 0] = 0.01
    # calculate the ndvi index
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

#
def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    point = ISS.coordinates()

    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(point.latitude)
    west, exif_longitude = convert(point.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Capture the image
    camera.capture(image)

# MAIN
ephemeris = load('de421.bsp')
timescale = load.timescale()
cont = 0 # we use external variable because we don't it to be re inizialized

while True:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris)== False:
        #there is light: we run our experiment

        camera = PiCamera()
        # qui dobbiamo scegliere la risoluzione delle immagini che vogliamo
        camera.resolution = (1296, 972)
        #camera.start_preview()

        
        x = cont # we use external variable because we don't it to be re inizialized
        for x in range(500):  # all'interno dell' range dobbiamo scegliere quante foto fare scattare al programma durante le tre ore
            # Camera warm-up time
            sleep(2)
            capture(camera, "img/image%s.png" % x)
            #camera.capture("img/image%s.png" % x)
            # load the original img
            original = cv2.imread("img/image%s.png" % x)
            original = np.array(original, dtype=float)/float(255)
            contrasted = contrast(original)
            ndvi = calc_ndvi(contrasted)
            ndvi_contrasted = contrast(ndvi)
            # color map the dark ndvi contrasted img
            color_mapped_prep = ndvi_contrasted.astype(np.uint8)
            color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
            cv2.imwrite("ndvi/imageNdvi%s.png" % x, color_mapped_image)
            cont = cont+1
            sleep(12) # in total 14 seconds of gap between 2 images  
    else:
        #is dark
        b=1
        print(b)
