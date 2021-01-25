import cv2

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if vid.isOpened():
  print ("Connected....")
  while True:
    ret, frame = vid.read()
    if ret:
      cv2.imshow("video", frame)
    else:
      print ("Error aqcuiring the frame")
      break
    if cv2.waitKey(10000) & 0xFF:
      break
else:
  print ("Not Connected....")

vid.release()
cv2.destroyAllWindows()