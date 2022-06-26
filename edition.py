import cv2
image1=cv2.imread('C:/Users/khada/Downloads/python/image edition/1-500x250-3.jpg')
image2=cv2.imread('C:/Users/khada/Downloads/python/image edition/2-500x250-2.jpg')
addedimage=cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imshow('addedimage',addedimage)
cv2.waitKey()