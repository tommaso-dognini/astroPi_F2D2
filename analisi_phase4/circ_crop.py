#This program crops the images as a circle cutting the black part of them that is not needed.
import numpy as np
from PIL import Image, ImageDraw

# array with the id numbers of the chosen images (the good ones)
a = [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 86, 87, 89, 90, 91, 92, 94,
     95, 95, 96, 97, 98, 99, 120, 121, 122, 123, 130, 131, 277, 278, 279, 296, 297, 298, 299]


# repeat the process for every image
for i in a:
    img=Image.open(f'/Users/tommasodognini/Documents/astroPi_F2D2/data_phase3/img{i}.jpg')

    #img_difetto = Image.open('/Users/tommasodognini/Documents/astroPi_F2D2/data_phase3/Ndvi80.jpg')
    #img_difetto_arr =np.array(img_difetto)


    height,width = img.size
    lum_img = Image.new('L', [height,width] , 0)

    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(450,0), (width+250,width-250)], 0, 360, fill = 255, outline = "white")
    img_arr =np.array(img)
    
    lum_img_arr =np.array(lum_img)
    final_img_arr = np.dstack((img_arr,lum_img_arr))

    Image.fromarray(final_img_arr).save(f'/Users/tommasodognini/Documents/astroPi_F2D2/analisi_phase4/img/cropped/cropped{i}.png')

