"""F2D2: astroPi code """

from time import sleep
from picamera import PiCamera
import cv2
import numpy as np
from fastiecm import fastiecm
from orbit import ISS
from skyfield.api import load

""" FUNCTIONS """

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

# function to convert position in exif data with correct type (from angle to string)


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

# shoot the img and add location as exif data


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


"""MAIN"""

# load the iss position with skyfield library
ephemeris = load('de421.bsp')
timescale = load.timescale()
# we use external variable to count the number of img taken and set it to a max based on the available space (3gB)
cont = 0
# simulates the img during the night-dark period
b = 0

# camera settings
camera = PiCamera()
# set default resolution
x_res = 4056
y_res = 3040
camera.resolution = (x_res, y_res)

# 3gb of space, max number of img (about 10mB) = 300, we save original and ndvi img so we shoot only 150
while cont != 150:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris) == False:  # run the experiment only in light

        # x = cont # we don't want x to be inizialized when iss switch from dark to light
        # for x in range(2):
        sleep(2)

        # add exif data and shoot img
        capture(camera, "img/img%s.jpg" % cont)

        # load the original img
        original = cv2.imread("img/img%s.jpg" % cont)
        original = np.array(original, dtype=float)/float(255)
        contrasted = contrast(original)  # apply contrast to original
        ndvi = calc_ndvi(contrasted)
        ndvi_contrasted = contrast(ndvi)  # apply contrast to ndvi

        # color map the dark ndvi contrasted img
        color_mapped_prep = ndvi_contrasted.astype(np.uint8)
        color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

        # crop the image
        cropped_image = color_mapped_image[400:2450, 1200:3200]
        cv2.imwrite("ndvi/Ndvi%s.jpg" % cont, cropped_image)

        sleep(34)  # in total 36 seconds of gap between 2 images  (36-2 at the start)
        cont = cont+1
    else:
        # ISS is in the dark
        print('dark %s' % b)
        b = b+1
        sleep(36)  # simualte sleep of time gap equale to gap between to img
