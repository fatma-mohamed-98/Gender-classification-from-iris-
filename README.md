# Problem statement:
- Gender prediction from iris recognition techniques is  widely used in human identification process which is called Biometric identification.
- As the iris of the two eyes of same individual aren’t comparative, the iris recognition gives more accurate result comparing with other biometric verifications.
so, it is considered as the most accurate biometric identification system.
- The performance of iris recognition system enhanced the gender prediction from their iris images . 
- Because of its high recognition rate, the iris recognition is one of the most meticulous biometric modality.


# Work significance:
Gender information may also be useful when a person isn't recognized but is attempting to gain entry to a restricted zone. Another possible use of gender information arises in social settings, where it may be useful to screen entry to an area based on gender, while not recording the identity. Gender classification is also important for banking transactions from cellular phones, demographic information collection, marketing research, and real-time electronic marketing. It is important to note that, for enrollment, we need to search the entire database to ensure that someone is not trying to generate two identities, one male, and one female, in order to double dip. For verification, we only need to search against the target template. Therefore, the gender information may be relevant to the management of the iris datasets.


# Dataset
CVBL IRIS Gender Classification Database Image Processing and Biometric Research, Computer Vision and Biometric Laboratory (CVBL)
Data base description:
Image type: RGB Color (Super resolution) No. of subjects: 704 No. of images per subject: 6 No. of images per eye: 3 No of subjects per gender: 312 Men, 392 Women Dimension: 5184x3456 Pixel Resolution: 72x72 dpi Format: .JPG Naming L: means left eye Naming R: means right eye

Camera description: Camera maker: Canon Camera model: Canon EOS 550D F-stop: f/8 Exposure time: 1/50 sec ISO speed: ISO-100 Flash mode: A flash ring, MEIKE MK-FC110 Distance with subjects: 20 cm

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
