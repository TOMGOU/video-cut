from moviepy.editor import *

# 读取视频到内存
vfc = VideoFileClip(r'C:\demo\02_SUMMARY\29_automation\video-cut\videos\test.mp4')

# 对视频时长进行剪切
clip = vfc.subclip(50, 60)

# 调低音频音量 (volume x 0.8)
clip = clip.volumex(0.8)
 
# 做一个txt clip. 自定义样式，颜色.
txt_clip = TextClip("My Moviepy 2020", fontsize=70, color='white')
 
# 文本clip在屏幕正中显示持续10秒
txt_clip = txt_clip.set_pos('bottom').set_duration(5)
 
# 把 text clip 的内容覆盖 video clip
videos = CompositeVideoClip([clip, txt_clip])

# vfc_list为VideoFileClip的对象组成的list
# concatente_videoclips(vfc_list, method='compose')

# 对视频播放区域进行剪辑
# clip = vfc.crop(x_center=0, y_center=0, width=20, height=20)

# 保存视频
videos.write_videofile(r'C:\demo\02_SUMMARY\29_automation\video-cut\videos\target.mp4', codec='mpeg4', verbose=False, audio=True)