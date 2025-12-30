# Object Segmentation

## Overview

In this notebook, we segment blue ovals from three different images via blurring, finding edges and contours, and masking.

## Original Images

The following images are the original images used for segmentation:

| Image 1 | Image 2 | Image 3 |
|--------|--------|--------|
| <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/773e6daf7bf3e673c78f7ce135a4cbb7695f1b01/assets/i1%20(1).jpg" width="100%"/> | <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/773e6daf7bf3e673c78f7ce135a4cbb7695f1b01/assets/i2%20(1).jpg" width="100%"/> | <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/773e6daf7bf3e673c78f7ce135a4cbb7695f1b01/assets/i3%20(1).jpg" width="100%"/> |


## Implementation

### Blurring

The first step is to blur our images using a median blur. A 25 x 25 kernel was chosen for all three images to strongly remove noise and to achieve higher confidence in edge discrimination. The blurred image is converted to HSV, and we extract the value channel to obtain the intensity.

### Edge and Contour Detection

Next, use the Sobel operator to calculate the derivatives of an image. The magnitude of the gradient is obtained and compared with a threshold value. If the gradient magnitude is greater than the threshold, an edge is considered detected. After some experimentation, the edge thresholds chosen were 25, 31, and 20 for Images 1, 2, and 3, respectively. Image 3 had the lowest threshold because of the homogenous background. Image 2 had the highest threshold due to the edges from the bench and the varying hues. In between was Image 1, which had two different surfaces, each with somewhat homogenous characteristics but still different texturing between the two surfaces.

Then, using `cv2.findContours` we find the contours and keep the largest contour. Using `cv2.drawContours(..., cv2.FILLED)` to produce a mask to isolate the largest contour. Perform morphological erosion to reduce background leakage and shrink the mask inward. Finally, apply the mask to segment the blue ovals.
 
## Results

Here are the results:

<p float="left">
  <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/f58a8cfabaca5fa0b64f9b2172efb231e7b0a30a/assets/obj_segmentation_results.png" width=100%" />
</p>

