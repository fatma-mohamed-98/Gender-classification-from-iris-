# Problem statement:
- Gender prediction from iris recognition techniques is  widely used in human identification process which is called Biometric identification.
- As the iris of the two eyes of same individual aren’t comparative, the iris recognition gives more accurate result comparing with other biometric verifications.
so, it is considered as the most accurate biometric identification system.
- The performance of iris recognition system enhanced the gender prediction from their iris images . 
- Because of its high recognition rate, the iris recognition is one of the most meticulous biometric modality.

# Dataset
CVBL IRIS Gender Classification Database Image Processing and Biometric Research, Computer Vision and Biometric Laboratory (CVBL)
References: Saeed Aryanmehr, Mohsen Karimi, and Farsad Zamani Boroujeni. "CVBL IRIS Gender Classification Database Image Processing and Biometric Research, Computer Vision and Biometric Laboratory (CVBL)." 2018 IEEE 3rd International Conference on Image, Vision and Computing (ICIVC). IEEE, 2018.\
Dataset sample:

<img src="https://github.com/fatma-mohamed-98/gender-classification-from-iris/blob/main/REDME_images/L1.JPG" width="320" height="200" />

# Segmentation:
on this dataset I faced a problem during segmentation phase when I try to apply the methods mentioned in the previous paper, so I try many different ways to solve it.
#### Problem:
The difference between Iris and pupil Intensities is very small and the Daugman’s operator searches for the circular path where there is maximum change in pixel values, so I need to increase the difference between iris and eye pupil intensities.
<img src="https://github.com/fatma-mohamed-98/gender-classification-from-iris/blob/main/REDME_images/gray_img.png"  width="500" height="300"/> <img src="https://github.com/fatma-mohamed-98/gender-classification-from-iris/blob/main/REDME_images/wrong_segmentation.png"  width="280" height="300" />
#### Solution:
my invented solution is 'converting RGB image to HSV then to Gray scale as shown below, then apply Daugman’s filter for the inner radius'.\
on the other hand 'Applying CLAHE filter then applying Daugman’s filter  for the outer raduis'.
<img src="https://github.com/fatma-mohamed-98/gender-classification-from-iris/blob/main/REDME_images/HSV2GRAY.png"  width="500" height="300"/> <img src="https://github.com/fatma-mohamed-98/gender-classification-from-iris/blob/main/REDME_images/Right_segmentation.png"  width="280" height="300" />
