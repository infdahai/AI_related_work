import  cv2
img = cv2.imread('./bw.jpg')
print(img.shape)
cropped = img[375:465,190:275]
cv2.imwrite("./res.jpg",cropped)