# AstroPi F2D2: Project documentation
## *Repository link*
https://github.com/tommaso-dognini/astroPi_F2D2 
## *The team:*
**Members:** Tommaso Dognini, Stefano Fanciosti, Pietro Donghi, Lorenzo Fumagalli <br/>
**Tutor:** Emanuela Magni <br/>
**School:** Liceo Scientifico e Musicale G.B. Grassi (LC) <br/>


## *Unboxing*
Here is a video of the unboxing experience of our astroPi kit.

[![Watch the video](https://user-images.githubusercontent.com/74106088/155032428-0b592a31-b1f0-4cf4-85b3-c917488f39f3.jpg)](https://www.youtube.com/embed/XQVWcYVsONQ?start=1)


## *Project description*
The code we have created has the purpose to capture the images of daylight landscapes on the earth and calculate the NDVI index in order to compare it to samples calculated with our code using public photos and samples data that are available for all teams .

We have paid attention to small details, such as highlighting the place and the time the photo has been made in order to make also a geographical comparison and justify the expected data.

The color mapping has been projected in order to make the data reading easier and more intuitive, also thanks to the legend with the reference color.

## *Main features*
Here is a list of the implemented features:

- The program shoots 300 images thanks to the astroPi IR camera and processes them producing a color mapped image, for each raw image, based on NDVI index values.
- The program croppes the raw image in order to avoid distortion in the NDVI index calculation and color mapping due to the ISS Columbus Module window frame.
- The program keeps track of the ISS position and its location is added to every raw image (IR) as exif data; this will help us in the phase 3 to analyse and locate images.
- Thanks to the ability of tracking the ISS the programm is able to shoot images only in daylight period, this helps to avoid shooting images that are not relevant and useful for this experiment.
- The program keeps track of time, the experiment is ment to run for 3 hours (2h and 57 minutes to be sure everything has been shut down at the end time) and then it automatically stops.

## *Space management*
The available disk space is 3GB. By testing our code, we understood the average dimension of a photo is about 5MByte. So we calculated that, in order to stay in the 3GB limit,  we can shoot 300 images with the max resolution (4060x3040). For every image we save the original IR image and a copy of the photo with the calculation of the NDVI index (this image is cropped so the resolution is lower), so in total the code saves 600 images. In this way we should end up occupating no more than 2.8 GB of space.

If we consider that our program shoots only in daylight and we approximate the night time equal to day time we can conclude that our experiment will have 90 minutes for shooting 300 images so we have to shoot 1 image every 18 seconds.

## *Samples images*
This are some example of images

| *Raw image*             |  *NDVI cropped* |
:-------------------------:|:-------------------------:
![1](https://user-images.githubusercontent.com/74106088/155032757-40b0926d-68ed-47dc-8aab-9fe55d71bd3e.jpg) |  ![ndvi_cropped1](https://user-images.githubusercontent.com/74106088/155032895-d307ae9c-a060-4d38-9816-e0b4d3f8a2b7.jpg)
![3](https://user-images.githubusercontent.com/74106088/155033526-d5d9965c-a19c-4b22-bafd-e13d26a7dcfa.jpg)  |  ![ndvi_cropped3](https://user-images.githubusercontent.com/74106088/155033615-cd829b86-ffd6-4051-bb89-b12b8a075a10.jpg)
![7](https://user-images.githubusercontent.com/74106088/155033730-02630fee-41de-4d6d-b7c8-6dd920aef6cd.jpg)  |  ![ndvi_cropped7](https://user-images.githubusercontent.com/74106088/155033834-da629f76-ff8c-42cf-8a8c-e04ccb5a457d.jpg)
![4](https://user-images.githubusercontent.com/74106088/155033911-bf882fca-9419-4a36-939a-ead378557402.jpg)  |  ![ndvi_cropped4](https://user-images.githubusercontent.com/74106088/155034044-00dd5ac0-4e96-425c-922f-c8ad49ee9497.jpg)



