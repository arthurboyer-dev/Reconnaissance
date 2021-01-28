from cv2 import*

#Rajouter un dossier contenant des visages .xml
visage = cv2.CascadeClassifier("test\frontfacealt2.xml")
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if vid.isOpened():
  print ("Connected....")
  while True:
    ret, frame = vid.read()
    tickmark=cv2.getTickCount() #Frame rate
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = visage.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=0)

    for x, y, w, h in face:
      cv2.rectangle(frame, (x,y), (x+y, y+h), (255,0,0) ,2)

    if ret:
      cv2.imshow("video", frame)

    else:
      print ("Error aqcuiring the frame")
      break

    if cv2.waitKey(1)==ord('q'):
      break

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame,"IPS: {:05.2F}".format(fps), (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    cv2.imshow('video', frame)

else:
  print ("Not Connected....")

vid.release()
cv2.destroyAllWindows()