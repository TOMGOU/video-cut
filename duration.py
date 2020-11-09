from moviepy.editor import VideoFileClip
import random
import numpy

videoPath = r'nba/finished/HC.mp4'
clip = VideoFileClip(videoPath)
print( int(clip.size[0]) )
print( numpy.trunc(clip.size)[0] )
print(round(1/0.99, 2))
print(random.random())