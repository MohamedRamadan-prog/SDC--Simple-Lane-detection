# SDC--Simple-Lane-detection
- Identifying lanes of the road is important to keep the vehicle in the constraints of the lane, it acts as a guiding reference to know the direction of steering the vehicle. It is a challenging task because of the varying road conditions. - This module will describe the various methods that can be used for lane detection using Python and OpenCV.

# Introduction
- Lane detection can be implemented using various methods that might include Simple operations such as: Color thresholding, Edge detection Then Hough transform. That implementation has many flaws, such as the presence of image distortion, and the inability to accurately measure the lane curvature.


![exit-ramp](https://user-images.githubusercontent.com/53750465/62503974-db43c400-b7f6-11e9-90ce-c9e8ada9fc75.jpg)

# Canny edge detection:
- Edge detection is used to identify the boundaries of an object in an image.
We convert the image to grayscale then get the gradient of the image, the gradient is to take the derivative with respect to x and y simultaneously.
- We find edges by tracing out the pixels that follow the strongest gradients.
- Low threshold and high threshold are defined to determine how strong the edges must be to be detected.
- Finally, canny edge detection algorithm finds all points associated with edges in the image.


![CannyOutput](https://user-images.githubusercontent.com/53750465/62503961-cd8e3e80-b7f6-11e9-9e7f-a5bcd5a8d07c.PNG)

# Hough transform:

![Hough space without ROI](https://user-images.githubusercontent.com/53750465/62503987-e72f8600-b7f6-11e9-8e03-b192e3aa1ae0.PNG)

![Output](https://user-images.githubusercontent.com/53750465/62503995-ed256700-b7f6-11e9-8350-6e3ea4c65f36.PNG)
 
# Region masking:

![image](https://user-images.githubusercontent.com/53750465/62555961-35cf3580-b874-11e9-813b-ea421075753a.png)



