# AI Project: Lane Line Tracking Using OpenCV

## Description
This project focuses on detecting lane lines in a road-driving video using OpenCV and basic image processing techniques. It simulates the early stages of a lane-assist system used in self-driving cars.

## How It Works
The program processes each frame of the video through the following steps:
- Convert the frame to grayscale  
- Apply Gaussian Blur to reduce noise  
- Detect edges using the Canny Edge Detector  
- Define a Region of Interest (ROI) to isolate the road area  
- Use the Hough Line Transform to detect and draw lane lines  

## Output
- The left lane line is successfully detected and drawn in yellow  
- The right lane line is drawn in white, but the accuracy still needs improvement and may not always align correctly with the actual road lane  

**Note**: This version is considered a working draft. The right lane detection is still under development.

## Requirements
- Python 3  
- OpenCV  
- NumPy  

Install the required libraries using the following command:
<pre>
  pip install opencv-python numpy
</pre>

## How to Run
1. Place the input video in the project directory with the name road.mp4  
2. Run the script using the following command:
<pre>
  python "line tracking.py"
</pre>
