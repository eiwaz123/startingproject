from cv2 import cv2

# Get the first webcam on the system
camera = cv2.VideoCapture(0) #Kahit wala na to eh para lang naman yan sa number ng device
# yung 0 para sa default camera
# ry mo

# Check if a camera was found
if not camera.isOpened():
    raise IOError("No camera found")

# Do something with the camera, like capturing frames
while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Display the frame (you can also process it in any way you like here)
    cv2.imshow("Camera", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()


