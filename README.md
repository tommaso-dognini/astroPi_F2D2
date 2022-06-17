# AstroPi F2D2: Project documentation
![copertina](https://user-images.githubusercontent.com/74106088/174007246-b99d3270-4896-4358-bb20-38bcde70d221.PNG)


## *The team*
**Members:** Tommaso Dognini, Stefano Fanciosti, Pietro Donghi, Lorenzo Fumagalli <br/>
**Tutor:** Emanuela Magni <br/>
**School:** Liceo Scientifico e Musicale G.B. Grassi (LC) <br/>

## *The project*
Teams of young people design and program a scientific experiment to run on board the International Space Station.

## Phase 1: Design

## Phase 2: Create

## Phase 3: Deploy

## Phase 4: Analize
PDF report: [F2D2_Report_AstroPiProject.pdf](https://github.com/tommaso-dognini/astroPi_F2D2/files/8926594/F2D2_Report_AstroPiProject.pdf)

### 1. Introduction
Our team has created a code in order to shoot images of our planet’s landscapes, store the useful ones and calculate for them the NDVI index. To gauge the process, we compared our images with NDVI images we obtained from standard samples available for all teams.
Our aim was to have a good understanding of the photographed subjects and how they have been changing over time. We paid attention to details, such as where and when pictures were taken, to also make a comparison and link our data to events that have affected those particular geographical areas.
The colour mapping has been set to make dissemination and data reading and understanding easier.
The expected rate of images good enough for the described work was at least 10%.


### 2. Method  
Our program had the aim to shoot photographs of geographical areas and calculate the NDVI index. To make this possible we used the infrared camera provided with the astroPi kit and we obtained jpg images and .log  files of the program logs.
During the testing phase, we understood that the ideal number of images to be taken was 300 (eventually 600, because we had chosen to create an NDVI image from each IR image) to respect the 3.0 GB data limit.
Originally, we had thought that having the NDVI image would have made the analysis phase easier but, after having received the data, we acknowledged that the results had some problems. This happened because the NDVI images were cropped in a square that was not centred, due to the camera position on the ISS which was different from what we expected. Therefore, black portions in the image altered both contrast and colour mapping process, as we had predicted and tried to avoid. 
However, we believe that our original idea still works perfectly with the changes we made during the analysis phase on the Earth.


### 3. Experiment results 
From phase 3 we received 300 images. 80 (26.7%) were black or very dark because we used the .is_sunlit() method of the skyfield library to shoot during light time, but we could not avoid getting images during twilight. Of the 220 photos left, only 40 (13.4%) were distinguishable and had a clear and cloudless subject.

![pie_chart](https://user-images.githubusercontent.com/74106088/174275948-e23a10b3-670e-444e-af13-b5007948e5b5.jpg)

To perform the analysis we cropped the chosen images in a square to avoid black margins as we originally aimed to. 
We then wrote a program that calculates the NDVI and creates the colour-mapped image. For this purpose, we looked for a better colour map that could enhance the variation of the NDVI index values. After some testing, we found that YlGn from matplotlib library suited our needs the best. 
The legend shown in every image goes from -1 to +1, which are the min and max values of the index, where +1 represents very flourishing vegetation. 
Here is what we obtained:

![130](https://user-images.githubusercontent.com/74106088/174275278-ea65e472-e43f-4c0a-a9e2-9a4e67d83f9e.png)
![299](https://user-images.githubusercontent.com/74106088/174275627-7fb5e1d7-c92f-4605-826c-62d84ea85326.png)
![90](https://user-images.githubusercontent.com/74106088/174275227-d8b6145d-100c-48a9-9460-fad22a922745.png)
![278](https://user-images.githubusercontent.com/74106088/174275306-27aa2921-3533-4458-91ed-84c833fe73fd.png)

The dark-green area in picture number one is due to the presence of the Yumori National Park, a wooded area. Here the coloration is uniform, while the third picture presents different shades of green because the forest is rich in swamps and lakes. The second and third NDVI images are very defined, so it is possible to recognise the lakes in the forest and the islands in the Volga river. The second image is also interesting because the dark-green area in the upper part is due to the presence of flourishing fields while in the down part the colouration is lighter for the presence of cities, as along the Japanese coast. Using the NDVI index in the Gargano image we can understand the wood is now completely reborn after the wildfire happened in 2007 which destroyed 4.500ha of Mediterranean bush.


### 4. Learnings

While working together on this project, we developed skills and learned much more than we thought.
In the first phases of the project, we had to reach the same Python coding level and learn how to collaborate on the same code project using GIT and Github. We also had to learn Markdown and, obviously, how to use RaspberryPi OS.
To overcome the numerous challenges, we learnt to split them into smaller tasks according to our points of strength. 
Having to face the same problems altogether led us to share our knowledge and learn something new from each other. For example, we tried to cancel lens reflection rings from pictures. We found out that one possible solution was to operate a subtraction of a chosen image and a white image with the reflection blemish. Despite our efforts, we could not solve this problem due to the lack of a blemished white image. 
Looking back we should have focused more on the raw IR images, leaving the NDVI calculation and colour mapping to the phase4 analysis on Earth.
We also strengthened our communication skills to describe our work in an efficient way.

### 5. Conclusion  
Our aim was to analyse the effects of climate change using the IR camera and NDVI index. In particular, we expected to photograph some natural disasters such as wildfires, floods or other issues caused by human activity, such as deforestation. 
The biggest problem with our experiment is the great variety of libraries with detailed NDVI images useful for comparison with the past to understand how vegetation health changes year by year, but despite this issue we are very satisfied with the final result. 
By using international libraries and code standards, we are now able to share our project and discoveries, and make the data collection easier to anybody who would like to use our work.
We would like to thank the ESA and the Raspberry Pi Foundation for giving us the possibility to work on such a unique project which led us to develop new skills and knowledge. 
This project has been a great opportunity for our career as students and worked for us as a compass in the process of choosing our future studies.

