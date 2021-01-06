import cv2

# print("Package Imported")

# img = cv2.imread("Resources/Lenna.png")

# cv2.imshow("Output", img)
# cv2.waitKey(2000)

cap = cv2.VideoCapture("Resources/Ch10_Step02_Simulation.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break 
    
    





