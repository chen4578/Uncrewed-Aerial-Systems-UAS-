import cv2 
import numpy as np
import glob

# Define the chess board rows and columns
rows = 6
cols = 8

# Termination criteria for corner refinement
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare the object points: (0,0,0), (1,0,0), (2,0,0), ..., (6,5,0). They are the same for all images
obj_3D = np.zeros((rows * cols, 3), np.float32)
obj_3D[:, :2] = np.mgrid[0:rows, 0:cols].T.reshape(-1, 2)

obj_points_3D = []  # 3D points in real world space
img_points_2D = []  # 2D points in image plane

path = "images/*.png"
# img = cv2.imread(path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load calibration images
image_files = glob.glob(path)  # Use your actual image path/pattern

for image_path in image_files:
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load {image_path}")
        continue
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (rows, cols), None)
    print(ret, corners)
    if ret:
    # Refine the corner position
        corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        
        # Add the object points and the image points to the arrays
        obj_points_3D.append(obj_3D)
        img_points_2D.append(corners)
    # Draw and display corners
    # img_display = img.copy()
    # cv2.drawChessboardCorners(img_display, Ch_Dim, corners2, ret)
    # cv2.imshow('Chessboard Corners', img_display)
    # cv2.waitKey(0)  # Display for 500ms
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points_3D, img_points_2D, gray.shape[::-1], None, None)
    h, w = gray.shape
    newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newCameraMtx)
    
    # crop the image
    #x, y, w, h = roi
    #dst = dst[y:y+h, x:x+w]
    cv2.imwrite('calibresult.png', dst)

    cv2.imshow('chess board', np.hstack((img, dst)))    
    cv2.waitKey(0)
    cv2.destroyAllWindows()