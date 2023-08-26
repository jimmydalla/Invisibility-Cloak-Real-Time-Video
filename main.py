import cv2

img = cv2.imread("bg_img.jpg")

video = cv2.VideoCapture("Aman visible.mp4")

output = cv2.VideoWriter("output_face.mp4",cv2.VideoWriter_fourcc(*'H.264'),29.13,(1280,720))

bg_img = cv2.cvtcolor(img,cv2.COLOR_BGR2RGB)

bg_img=cv2.resize(img,(450,800))
while(video.isOpened()):
  status,frame=video.read()
