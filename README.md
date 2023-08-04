<!DOCTYPE html>
<html>

<head>
   
</head>

<body>
    <h1>Real-time Moving Object Detection with Sound Alert</h1>
    <p>This repository contains a Python script that implements real-time moving object detection with sound alert capabilities using the OpenCV library. The application captures video from the camera, processes consecutive frames, and highlights moving objects by drawing rectangles around them. Additionally, it emits a distinct beep sound for each detected movement, providing immediate auditory feedback to the user.</p>

  <h2>How to Run</h2>
  <p>Follow the instructions below to run the script:</p>
  <ol>
      <li>Install the necessary dependencies by running the following command in your terminal or command prompt:</li>
      <pre><code>pip install opencv-python</code></pre>
      <li>Clone this repository to your local machine by executing:</li>
      <pre><code>git clone https://github.com/your_username/moving-object-detection.git</code></pre>
      <li>Navigate to the project directory:</li>
      <pre><code>cd moving-object-detection</code></pre>
      <li>Run the Python script:</li>
      <pre><code>python moving_object_detection.py</code></pre>
  </ol>

  <h2>Functionality</h2>
  <p>The script operates as follows:</p>
  <ol>
      <li>It initializes the camera by utilizing the VideoCapture class from OpenCV.</li>
      <li>Consecutively reads two frames from the camera to detect movement.</li>
      <li>Computes the absolute difference between the two frames, identifying areas with motion.</li>
      <li>Converts the difference image to grayscale for further processing.</li>
      <li>Applies Gaussian blur to the grayscale image, reducing noise and enhancing object detection.</li>
      <li>Thresholds the blurred image to create a binary image, simplifying object boundaries.</li>
      <li>Dilates the binary image, filling gaps and holes in detected objects.</li>
      <li>Identifies contours in the dilated image to outline the moving objects.</li>
      <li>For each detected object with an area greater than 5000 pixels:</li>
      <ul>
          <li>Draws a green rectangle around it on the original frame.</li>
          <li>Emits a beep sound to indicate the detection to the user.</li>
      </ul>
      <li>Displays the processed frame in a window named 'MyCam'.</li>
      <li>Continues this process until the user presses the 'q' key, upon which the script releases the camera and closes all OpenCV windows.</li>
  </ol>
  <p>Note: The line to draw all contours on the original frame is commented out by default. You can uncomment it if you wish to visualize the contours.</p>

  <h2>Contributions and Future Enhancements</h2>
  <p>Contributions to this project are welcome. If you would like to contribute, consider the following potential enhancements:</p>
  <ul>
      <li>Implementing advanced object tracking algorithms for improved detection accuracy.</li>
      <li>Supporting multi-camera setups to monitor multiple views simultaneously.</li>
      <li>Developing a user-friendly graphical user interface (GUI) for configuration and control.</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. You can find more details in the <a href="LICENSE">LICENSE</a> file.</p>

  <h2>Acknowledgments</h2>
  <p>The implementation of this project was inspired by various computer vision and image processing techniques available in the OpenCV library. Special thanks to the OpenCV community for their valuable contributions and support.</p>

  <p>Happy object detection!</p>
</body>

</html>
