import cv2 as cv
# Sample images https://homepages.cae.wisc.edu/~ece533/images/
image=cv.imread('..\samples\Lenna.png') #Load the image and store it in a variable 
cv.imshow('image',image) #Show image with window name as 'image'
cv.moveWindow("image",0,0); #Move the window to x-0 y-0 
cv.waitKey(5000) #Wait untill user user click anykey in window. 0 millisecond will wait forever untill key pressed, If its 1000 it will wait for 1second 
cv.destroyAllWindows() #When key press identified from the above command it will execute next statement. This statement will close all windows 