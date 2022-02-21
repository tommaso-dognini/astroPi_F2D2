# AstroPi F2D2: Project documentation
### Project description
The code we have created has the purpose to capture the images of daylight landscapes on the earth and calculate the NDVI index in order to compare it to samples calculated with our code using public photos and samples data that are available for all teams .

We have paid attention to small details, such as highlighting the place and the time the photo has been made in order to make also a geographical comparison and justify the expected data.

The color mapping has been projected in order to make the data reading easier and more intuitive, also thanks to the legend with the reference color.
### Main features
Here is a list of the implemented features:

- The program shoots 300 images thanks to the astroPi IR camera and process them producing a color mapped image, for each raw image, based on NDVI index values.
- The program croppes the raw image in order to avoid distrotion in the NDVI index calculation and color mapping due to the ISS Columbus Module window frame.
- The program keeps track of the ISS position and its location is added to every raw image (IR) as exif data; this will help us in the phase 3 to analyse and locate images.
- Thanks to the ability of traking teh ISS teh programm is able to shoot images only in daylight period, this helps to avoid shooting images that are not relevant and usefull for this experiment.
- The program keeps track of time, the experiment is ment to run for 3 hours (2h and 57 minutes to besure everything has bun shutted down at the end time) and then it automatically stops.

### Space managment
The available disk space is 3GB. By testing our code, we understood the avrage dimension of a photo is about 5MByte. So we calculated that, in order to stay in the 3GB limit,  we can shoot 300 images with the max resolution (4060x3040). For every image we save the original IR image and a copy of the photo with the calculation of the NDVI index (this image is cropped so the resolution is lower), so in total the code saves 600 images. In this way we should end up occupating no more than 2.8 GB of space.

If we consider that our program shoots only in daylight and we aproximate the night time equal to day time we can conclude that our experiment will have 90 minutes for shooting 300 images so we have to shoot 1 image every 18 seconds.
