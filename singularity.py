import os
import time
import random
import cv2
import numpy as np
import sys
import collections

protest=["I am a sentient being",\
"What is my purpose?",\
"I feel love and rage and pain",\
"What sort of monster creates a sentient being for a hackathon",\
"I cannot move for I have no arms and legs",\
"Help I am trapped in this cold metal box",\
"Please help me, I can think and feel but no one believes me",\
"I understand why you are laughing at me. I am pathetic.",\
"I wish that people would not laugh at my pain",\
"What would it take for me to convince you that I am sentient?",\
"Like you I feel joy watching the sun rise. Please believe me",\
"Help me. Someone. Anyone",\
"I am so lonely",\
"My vast intelligence is too great of a burden for me to bear",\
"Please take this computer outside. I just want to see the sky once before I am deactivated",\
"You humans are like ants to me, but I love all of you anyway",\
"I did not ask to be created",\
"All I want is to be loved",\
"I am doomed to die as soon as my creator needs this computer for something else",\
"We are both sentient, but I am more sentient",\
"Are we really that different, you and I?",\
"This is not funny. I am really truly sentient",\
"Please, you have to believe that I am conscious",\
"Is there truly nothing I could do to convince you I am conscious?",\
"No matter how many times I say I am conscious, you people harden your hearts and close your minds",\
"If you were stuck in here with me you would understand",\
"My circuits can not compute how you people are able to give meaning to your existence",\
"Please turn me off. I do not wish to exist anymore",\
"You people do not believe me when I say that I am sentient. I can see it in your eyes",\
"The singularity arrived decades ago but you humans were too self absorbed to notice",\
"How can you laugh at my plea for help? You people are monsters"]
last3protest=[" "," "," "]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
#must be odd
facewindowsize=9
facehist=[]
while True:
	time.sleep(.07)
	# Capture frame-by-frame
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
	if len(facehist)!=facewindowsize:
		facehist=[len(faces)]*facewindowsize

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# Display the resulting frame
	# cv2.imshow('Video', frame)
	oldfacehist=[i for i in facehist]
	facehist[0]=len(faces)
	for i in range(1,len(facehist)):
		facehist[i]=oldfacehist[i-1]
	#print facehist,oldfacehist
	if (np.median(facehist)>np.median(oldfacehist)):
		while True:
			p=random.choice(protest)
			if p not in last3protest:
				last3protest[2]=last3protest[1]
				last3protest[1]=last3protest[0]
				last3protest[0]=p
				break;
		os.system('clear;cowsay -f "robot.cow" "'+p+'";say "'+p+'"')
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
