from cv2 import *
vc = VideoCapture(0);
while True:
    next, frame = vc.read()

  #  gray = cvtColor(frame, COLOR_BGR2GRAY)
  #  gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
  #  can = Canny(gauss, 0, 30, 3)

    imshow("webcam", frame)
    if waitKey(50) >= 0:
        break;
