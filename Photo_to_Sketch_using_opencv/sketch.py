import cv2

#load the image from the file and show it in a window.
#Use the ‘Esc’ key to close the window.

color_image = cv2.imread("camel.jpg")
cv2.imshow("camel",color_image)
cv2.waitKey()
cv2.destroyAllWindows() 

#stylization function to create the effect of smoothing out the colors and the image.

cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)
cv2.imshow('cartoon', cartoon_image)
cv2.waitKey()
cv2.destroyAllWindows() 

#Create a pencil and colour pencil sketch effect

cartoon_image1, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
cv2.imshow('pencil', cartoon_image1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('pencil', cartoon_image2)    
cv2.waitKey()    
cv2.destroyAllWindows()