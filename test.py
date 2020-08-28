from moviepy.editor import *
FONT_URL = './仿宋_GB2312.ttf'

class VideoCut:
  def __init__(self):
    super(VideoCut, self).__init__()
    self.initCut()

  def initCut(self):
    videoList = self.file_name(r'/Users/tangyong/test/automation/video-cut/original_videos')
    videoUrlList = videoList['url_name']
    videoNameList = videoList['full_file_name']
    for index in range(len(videoUrlList)):
      vfc = VideoFileClip(videoUrlList[index])
      size = vfc.size
      duration = vfc.duration
      clip = vfc.crop(x_center = size[0] / 2, y_center = size[1] / 2, width = size[0], height = size[1] - 200)
      txt_clip = TextClip("@九月半a", font=FONT_URL, fontsize=35, color='red', bg_color='white')
      txt_clip = txt_clip.set_pos((0.02, 0.84), relative=True).set_duration(duration)
      videos = CompositeVideoClip([clip, txt_clip])
      videos.write_videofile(r'/Users/tangyong/test/automation/video-cut/videos/' + videoNameList[index], fps=120, codec='mpeg4', bitrate='10000k', audio=False)

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