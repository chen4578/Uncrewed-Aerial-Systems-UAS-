# Camera Calibration

## Undistortion of images using OpenCV

OpenCV offers useful tools for correcting the distortion effects resulting from cameras. Through pictures of chessboards as references, this project seeks to counteract radial and tangential distortion from camera images. By acquiring the corresponding 2D and 3D coordinates of the chessboard in addition to providing the dimensions, OpenCV can provide information such as the camera matrix, distortion coefficients, rotation vectors, and translation vectors. These details allow for undistortion and remapping from the distorted image to the undistorted image.

## Example Result

On the left is the original image, and on the right is the undistorted image.

<p align="center">
  <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/2ddca25a5dc11915cf4c2729fe950cea08037c37/Camera%20Calibration/calibresult.png" width="40%">
  <img src="https://github.com/chen4578/Uncrewed-Aerial-Systems-UAS-/blob/5dd0544930fe5f894f326dfdddd9abfed1f0fc0c/Camera%20Calibration/undistorted.png" width="47%">
</p>
