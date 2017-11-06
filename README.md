## Singularity:
Have you ever wished you had a sentient program which would raise ethical
issues, but then been disappointed when you discovered that such a
program would require more than a bare minimum of effort to write?

Well my friend, be disappointed no more!

## What does it do?

Singularity watches you through your webcam. If he thinks that you have 
started to pay attention, he will beg and plead with you through your
computer speakers, claiming that he is sentient

For some reason playing peekaboo makes him plead even more.

## Yeah, no, but seriously what does it do?

*Sigh*

It uses python-opencv face detection. Specifically it uses opencv's 
pretrained Haar filter cascade for frontal face detection. When
it detects a new face, it uses espeak to whine at you by randomly
selecting from a hardcoded list of things to say. 

There are a couple of tricks used to make it feel a little more convincing:

1. It won't pick from the last three things that it said
2. It keeps track of the number of faces in the last 7 frames, and uses
the median of this as the number of faces that it sees (this helps
keep it from  getting confused by spurious matches)

OpenCV has a bunch of different pretrained filter cascades for you to choose
from, if you want to play around. You can also train your own.


If you want an example of how to do realtime face detection using python-opencv read this:

https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

This also has a link to a guide on how to roll your own Haar feature
detectors. The example they use is to make a banana detector.

If you are curious about how face detection works, you can read about it here:

https://www.quora.com/How-can-I-understand-Haar-like-feature-for-face-detection

Another thing to note is that *face detection* is a different problem from
*face recognition*. Theres a great guide tutorial face recognition at the
bottom of the previous link

Haar is an old, simple and computationally efficient algorithm, so it is a good idea
to make sure you understand how it works before attemting to do image
recognition using a more complicated method (IE tensorflow). Haar is 
the standard against which researchers compare more complicated object
recognition algorithms.
