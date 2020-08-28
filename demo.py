from moviepy.editor import *
# from moviepy.editor import TextClip
FONT_URL = './仿宋_GB2312.ttf'
# print ( TextClip.list("font") )

# 读取视频到内存
vfc = VideoFileClip(r'/Users/tangyong/test/automation/video-cut/original_videos/paper.mp4')

# 对视频播放区域进行剪辑
size = vfc.size
duration = vfc.duration
clip = vfc.crop(x_center = size[0] / 2, y_center = size[1] / 2, width = size[0], height = size[1] - 200)
print(size, duration)

# 对视频时长进行剪切
# clip = vfc.subclip(10, 60)

# 调低音频音量 (volume x 0.8)
# clip = clip.volumex(0.8)
 
# 做一个txt clip. 自定义样式，颜色. 'Century-Schoolbook-Italic'
txt_clip = TextClip("@九月半a", font=FONT_URL, fontsize=35, color='red', bg_color='white')
 
# 文本clip在屏幕正中显示持续10秒
txt_clip = txt_clip.set_pos((0.01, 0.88), relative=True).set_duration(duration)
 
# 把 text clip 的内容覆盖 video clip
videos = CompositeVideoClip([clip, txt_clip])

# vfc_list为VideoFileClip的对象组成的list
# concatente_videoclips(vfc_list, method='compose')

# 保存视频
videos.write_videofile(r'/Users/tangyong/test/automation/video-cut/videos/target.mp4', fps=120, codec='mpeg4', bitrate='8000k', audio=True)
# audio_fps=44100,
# preset="medium",
# audio_nbytes=4, audio_codec=None,
# audio_bitrate=None, audio_bufsize=2000,
# temp_audiofile=None,
# rewrite_audio=True, remove_temp=True,
# write_logfile=True, verbose=True,
# threads=None, ffmpeg_params=None