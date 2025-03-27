import cv2 as cv


def rescaleFrame( frame, scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


    # resizing the  video

capture=cv.VideoCapture('videos/cati.mp4')  # Read the video from the file
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()  # Release the video
cv.destroyAllWindows()  # Destroy all the windows

