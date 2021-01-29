from  __future__ import print_function
import cv2 as cv
import argparse

def detectAndDisplay(frame):
  frame_gray=cv.cvtColor(frame, cv.COLOR_BAYER_BG2GRAY)
  frame_gray=cv.equalizeHist(frame_gray)
  
  #Detection de visage
  faces=face_cascade.detectMultiScale(frame_gray)
  for (x,y,w,h) in faces:
    center = (x + w//2, y + h//2)
    frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
    faceROI = frame_gray[y:y+h,x:x+w]
  cv.imshow('EYES EYES EYES EYES EYS EYS EYS EYS YESY EYS EYSYESY ')

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='C:/Users/Arthur/AppData/Local/Programs/Python/Python37-32/Lib/haarcascade/frontfacealt2')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = vars(parser.parse_args())

face_cascade =args.face_cascade()
face_cascade =cv.CascadeClassifier()

if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
  print('--(!)Erreur de chargement des fichiers du visage')
  exit(0)

camera_device =args.camera

cap =cv.VideoCapture(camera_device)
if not cap.isOpened:
  print('--(!)Erreur de connection video')
  exit(0)

while True:
  ret, frame = cap.read()
  if frame is None:
    print("--(!)Pas de capture d'images")
    break

  detectAndDisplay(frame)

  if cv.waitKey(10) == 27:
    break

vid.release()
cv2.destroyAllWindows()