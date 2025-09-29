# Camera Calibration

## Undistortion of images using OpenCV

OpenCV offers useful tools for correcting the distortion effects resulting from cameras. Through pictures of chessboards as references, this project seeks to counteract radial and tangential distortion from camera images. By acquiring the corresponding 2D and 3D coordinates of the chessboard in addition to providing the dimensions, OpenCV can provide information such as the camera matrix, distortion coefficients, rotation vectors, and translation vectors. These details allow for undistortion and remapping from the distorted image to the undistorted image.
