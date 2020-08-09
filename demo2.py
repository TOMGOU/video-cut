# 导入需要的库
from moviepy.editor import *

# 读取视频到内存
vfc = VideoFileClip(r'C:\demo\02_SUMMARY\29_automation\video-cut\videos\test.mp4')

# 对视频时长进行剪切
clip = vfc.subclip(50, 60)
 
# 调低音频音量 (volume x 0.8)
clip = clip.volumex(0.8)
 
# 做一个txt clip. 自定义样式，颜色.
txt_clip = TextClip("TOMGOU 2020", fontsize=70, color='white')
 
# 文本clip在屏幕正中显示持续10秒
txt_clip = txt_clip.set_pos('center').set_duration(5)
 
# 把 text clip 的内容覆盖 video clip
video = CompositeVideoClip([clip, txt_clip])
 
# 把最后生成的视频导出到文件内
video.write_videofile(r'C:\demo\02_SUMMARY\29_automation\video-cut\videos\target.mp4', codec='mpeg4', verbose=False, audio=True)