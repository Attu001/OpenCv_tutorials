import cv2 as cv

# Function to rescale a frame to a specified scale
def rescaleFrame(frame, scale=0.2):
    # Calculate new width and height based on the scale
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the frame and return it
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Open the video file
capture = cv.VideoCapture('videos/cati.mp4')  # Read the video from the file

# Loop through each frame of the video
while True:
    isTrue, frame = capture.read()  # Read a frame from the video
    if not isTrue:  # Break the loop if no frame is read (end of video)
        break

    # Rescale the frame
    frame_resized = rescaleFrame(frame)

    # Display the original and resized frames
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # Break the loop if the 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv.destroyAllWindows()
