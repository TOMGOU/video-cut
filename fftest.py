from moviepy.editor import *
FONT_URL = './仿宋_GB2312.ttf'
import os

class VideoCut:
  def __init__(self):
    super(VideoCut, self).__init__()
    self.initCut()

  def initCut(self):
    videoList = self.file_name(r'/Users/tangyong/test/automation/video-cut/original_videos')
    videoUrlList = videoList['url_name']
    videoNameList = videoList['full_file_name']
    for index in range(len(videoUrlList)):
      clipStr = 'crop=iw:ih/2'
      padStr = 'pad=iw:ih+588:0:294:yellow'
      text1 = 'drawtext="fontfile=gb.ttf:text=慢下来，在微观世界里看诗和远方:x=(w-tw)/2:y=h-270:fontcolor=red:fontsize=30"'
      text2 = 'drawtext="fontfile=gb.ttf:text=一个相机分隔出两个世界:x=(w-tw)/2:y=70:fontcolor=green:fontsize=30"'
      text3 = 'drawtext="fontfile=gb.ttf:text=门外是繁华的现代都市:x=(w-tw)/2:y=140:fontcolor=green:fontsize=30"'
      text4 = 'drawtext="fontfile=gb.ttf:text=门里是幽静如画的世外桃源:x=(w-tw)/2:y=210:fontcolor=green:fontsize=30"'
      output = f'/Users/tangyong/test/automation/video-cut/finished/{ videoNameList[index] }'
      cmdStr = f'ffmpeg -y  -i  { videoUrlList[index] }  -vf [in]{ clipStr },{ padStr },{ text1 },{ text2 },{ text3 },{ text4 }[out] { output }'
      os.popen(cmdStr)

  def file_name(self, file_dir):   
    L={'file_name': [], 'url_name': [], 'full_file_name': []}  
    for root, dirs, files in os.walk(file_dir):
      for file in files:  
        if os.path.splitext(file)[1] == '.mp4' or os.path.splitext(file)[1] == '.webm':  
          L['url_name'].append(os.path.join(root, file))
          L['file_name'].append(os.path.splitext(file)[0])         
          L['full_file_name'].append(os.path.splitext(file)[0] + os.path.splitext(file)[1])    
    return L

VideoCut()