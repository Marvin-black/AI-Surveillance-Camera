import cv2
import winsound

# Initialize the camera using VideoCapture
cam = cv2.VideoCapture(1)

# Main loop for video processing
while cam.isOpened():
    # Read two consecutive frames from the camera
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    # Compute the absolute difference between the two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the blurred image to create a binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the binary image to fill gaps and holes in the detected objects
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Uncomment the line below to draw all contours on the original frame
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # Iterate through each contour and process the ones with area greater than 5000
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue

        # Get the bounding box coordinates of the contour
        x, y, w, h = cv2.boundingRect(c)

        # Draw a rectangle around the detected object on the original frame
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Emit a beep sound to indicate the detection
        winsound.Beep(500, 200)

    # Display the processed frame in a window named 'MyCam'
    cv2.imshow('MyCam', frame1)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
