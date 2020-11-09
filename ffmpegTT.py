import win_unicode_console
win_unicode_console.enable()
import sys
import os
import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QProgressBar, QApplication, QColorDialog, QFileDialog, QRadioButton)
from PyQt5.QtGui import QColor
from moviepy.editor import VideoFileClip

class VideoClip(QWidget):
  def __init__(self):
    super(VideoClip, self).__init__()
    self.switch = True
    self.initUI()

  def initUI(self):
    # 视频源文件夹路径
    self.source_btn = QPushButton('源文件夹：', self)
    self.source_btn.move(20, 30)
    self.source_btn.resize(100,30)
    self.source_btn.clicked.connect(self.select_source)
    self.source_le = QLineEdit('/Users/tangyong/test/automation/video-cut/original_videos', self)
    self.source_le.move(120, 30)
    self.source_le.resize(450,30)

    # 处理后的视频存储路径
    self.save_btn = QPushButton('存储路径：', self)
    self.save_btn.move(20, 75)
    self.save_btn.resize(100,30)
    self.save_btn.clicked.connect(self.select_save)
    self.save_le = QLineEdit('/Users/tangyong/test/automation/video-cut/test', self)
    self.save_le.move(120, 75)
    self.save_le.resize(450,30)

    # 背景颜色调色板
    self.scale_rate_btn = QPushButton('缩小比例：', self)
    self.scale_rate_btn.move(20, 120)
    self.scale_rate_btn.resize(100,30)
    self.scale_rate_le = QLineEdit('0.99', self)
    self.scale_rate_le.move(120, 120)
    self.scale_rate_le.resize(60,30)

    # 字体颜色调色板
    self.font_color_btn = QPushButton('字体颜色：', self)
    self.font_color_btn.move(225, 120)
    self.font_color_btn.resize(100,30)
    self.font_color_btn.clicked.connect(self.showFontColorDialog)
    self.font_color_le = QLineEdit('#ffff00', self)
    self.font_color_le.move(325, 120)
    self.font_color_le.resize(60,30)

    # 字体大小设置
    self.start_size_btn = QPushButton('字体大小：', self)
    self.start_size_btn.move(430, 120)
    self.start_size_btn.resize(100,30)
    self.start_size_le = QLineEdit('30', self)
    self.start_size_le.move(530, 120)
    self.start_size_le.resize(40,30)

    # 视频裁剪开始时间参数
    self.startLabel = QLabel(self)
    self.startLabel.move(30, 165)
    self.startLabel.resize(100, 30)
    self.startLabel.setText("掐头时间(s)：")
    self.start_le = QLineEdit('1', self)
    self.start_le.move(120, 165)
    self.start_le.resize(150, 30)

    # 视频裁剪总时长参数
    self.durationLabel = QLabel(self)
    self.durationLabel.move(330, 165)
    self.durationLabel.resize(100, 30)
    self.durationLabel.setText("去尾时间(s)：")
    self.duration_le = QLineEdit('1', self)
    self.duration_le.move(420, 165)
    self.duration_le.resize(150, 30)

    # 视频裁剪宽
    self.speedupLabel = QLabel(self)
    self.speedupLabel.move(30, 210)
    self.speedupLabel.resize(100, 30)
    self.speedupLabel.setText("视频加速：")
    self.speedup_le = QLineEdit('0.99', self)
    self.speedup_le.move(120, 210)
    self.speedup_le.resize(150, 30)

    # 视频裁剪高
    self.contrastLabel = QLabel(self)
    self.contrastLabel.move(330, 210)
    self.contrastLabel.resize(100, 30)
    self.contrastLabel.setText("对比度：")
    self.contrast_le = QLineEdit('1', self)
    self.contrast_le.move(420, 210)
    self.contrast_le.resize(150, 30)

    # 视频裁剪宽
    self.brightnessLabel = QLabel(self)
    self.brightnessLabel.move(30, 255)
    self.brightnessLabel.resize(100, 30)
    self.brightnessLabel.setText("亮度：")
    self.brightness_le = QLineEdit('0', self)
    self.brightness_le.move(120, 255)
    self.brightness_le.resize(150, 30)

    # 视频裁剪高
    self.saturationLabel = QLabel(self)
    self.saturationLabel.move(330, 255)
    self.saturationLabel.resize(100, 30)
    self.saturationLabel.setText("饱和度：")
    self.saturation_le = QLineEdit('1', self)
    self.saturation_le.move(420, 255)
    self.saturation_le.resize(150, 30)

    # 第一段文案
    self.text1Label = QLabel(self)
    self.text1Label.move(30, 300)
    self.text1Label.resize(100, 30)
    self.text1Label.setText("第一段文案：")
    self.text1_le = QLineEdit('', self)
    self.text1_le.move(120, 300)
    self.text1_le.resize(400, 30)
    self.text1height_le = QLineEdit('50', self)
    self.text1height_le.move(525, 300)
    self.text1height_le.resize(45, 30)

    # 第二段文案
    self.text2Label = QLabel(self)
    self.text2Label.move(30, 345)
    self.text2Label.resize(100, 30)
    self.text2Label.setText("第二段文案：")
    self.text2_le = QLineEdit('', self)
    self.text2_le.move(120, 345)
    self.text2_le.resize(400, 30)
    self.text2height_le = QLineEdit('100', self)
    self.text2height_le.move(525, 345)
    self.text2height_le.resize(45, 30)

    # 第三段文案是否镜像
    self.minorLabel = QLabel(self)
    self.minorLabel.move(30, 390)
    self.minorLabel.resize(100, 30)
    self.minorLabel.setText("是否镜像：")
    self.minor_le_yes = QRadioButton('是', self)
    self.minor_le_yes.move(120, 390)
    self.minor_le_yes.resize(50, 30)
    self.minor_le_yes.clicked.connect(lambda: self.radioBeClicked(self.sender().text()))
    self.minor_le_no = QRadioButton('否', self)
    self.minor_le_no.move(180, 390)
    self.minor_le_no.resize(50, 30)
    self.minor_le_no.clicked.connect(lambda: self.radioBeClicked(self.sender().text()))
    self.minor_le_no.setChecked(True)
    self.minor = False

    #开始剪辑按钮
    self.save_btn = QPushButton('开始剪辑视频',self)
    self.save_btn.move(450, 435)
    self.save_btn.resize(120, 50)
    self.save_btn.clicked.connect(self.kick)

    #用户提示区
    self.result_le = QLabel('请填写视频剪辑相关参数', self)
    self.result_le.move(30, 480)
    self.result_le.resize(340, 30)
    self.result_le.setStyleSheet('color: blue;')

    # 整体界面设置
    self.resize(600, 600)
    self.center()
    self.setWindowTitle('抖音视频自动化剪辑')#设置界面标题名
    self.show()
  
  # 窗口居中函数
  def center(self):
    screen = QtWidgets.QDesktopWidget().screenGeometry()#获取屏幕分辨率
    size = self.geometry()#获取窗口尺寸
    self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))#利用move函数窗口居中
  
  def radioBeClicked(self, btnText):
    self.minor = btnText == '是'
    return self.minor

  def select_source(self):
    dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件夹路径", "C:/")
    self.source_le.setText(str(dir_path))

  def select_save(self):
    dir_path = QFileDialog.getExistingDirectory(self, "请选择处理后视频保存路径", "C:/")
    self.save_le.setText(str(dir_path))

  def set_label_func(self, text):
    self.result_le.setText(text)

  def switch_func(self, bools):
    self.switch = bools

  def showFontColorDialog(self):
    col = QColorDialog.getColor()
    if col.isValid():
      self.font_color_le.setText(str(col.name()))

  def kick(self):
    sourcePath = self.source_le.text().strip()
    savePath = self.save_le.text().strip()
    scaleRate = self.scale_rate_le.text().strip()
    fontColor = self.font_color_le.text().strip()
    fontSize = int(self.start_size_le.text().strip())
    startTime = float(self.start_le.text().strip())
    durationTime = float(self.duration_le.text().strip())
    speedup = float(self.speedup_le.text().strip())
    contrast = float(self.contrast_le.text().strip())
    brightness = float(self.brightness_le.text().strip())
    saturation = float(self.saturation_le.text().strip())
    text1 = self.text1_le.text().strip()
    text1height = int(self.text1height_le.text().strip())
    text2 = self.text2_le.text().strip()
    text2height = int(self.text2height_le.text().strip())
    minor = self.minor
    if self.switch and sourcePath != '' and savePath != '' and scaleRate != '' and fontSize != '' and startTime != '' and durationTime != '' and speedup != '' and contrast != '' and brightness != '' and saturation != '' and minor != '':
      self.switch = False
      self.set_label_func('请耐心等待，正在打开浏览器！')
      self.my_thread = MyThread(sourcePath, savePath, scaleRate, fontColor, fontSize, startTime, durationTime, speedup, contrast, brightness, saturation, text1, text1height, text2, text2height, minor, self.set_label_func)#实例化线程对象
      self.my_thread.start()#启动线程
      self.my_thread.my_signal.connect(self.switch_func)

class MyThread(QThread):
  my_signal = pyqtSignal(bool)
  def __init__(self, sourcePath, savePath, scaleRate, fontColor, fontSize, startTime, durationTime, speedup, contrast, brightness, saturation, text1, text1height, text2, text2height, minor, set_label_func):
    super(MyThread, self).__init__()
    self.sourcePath = sourcePath
    self.savePath = savePath
    self.scaleRate = scaleRate
    self.fontColor = fontColor
    self.fontSize = fontSize
    self.startTime = startTime
    self.durationTime = durationTime
    self.speedup = speedup
    self.contrast = contrast
    self.brightness = brightness
    self.saturation = saturation
    self.text1 = text1
    self.text1height = text1height
    self.text2 = text2
    self.text2height = text2height
    self.minor = minor
    self.set_label_func = set_label_func

  def run(self): #线程执行函数
    string = self.videoCut()
    self.set_label_func(string)
    self.my_signal.emit(True)  #释放自定义的信号
  
  def file_name(self, file_dir):   
    L={'file_name': [], 'url_name': [], 'full_file_name': []}
    for root, dirs, files in os.walk(file_dir):
      for file in files:  
        if os.path.splitext(file)[1] == '.mp4' or os.path.splitext(file)[1] == '.webm':  
          L['url_name'].append(os.path.join(root, file))
          L['file_name'].append(os.path.splitext(file)[0])         
          L['full_file_name'].append(os.path.splitext(file)[0] + os.path.splitext(file)[1])    
    return L
  
  def videoCut(self):
    videoList = self.file_name(self.sourcePath)
    videoUrlList = videoList['url_name']
    videoNameList = videoList['full_file_name']
    for index in range(len(videoUrlList)):
      duration = VideoFileClip(videoUrlList[index]).duration
      clip = f'crop="{ self.scaleRate }*iw":"{ self.scaleRate }*ih":iw/2:ih/2'
      # text1 = f'drawtext="fontfile=ff.ttf:text={ self.text1 }:x=(w-tw)/2:y={ self.text1height }:fontcolor={ self.fontColor }:fontsize={ self.fontSize }"'
      # text2 = f'drawtext="fontfile=ff.ttf:text={ self.text2 }:x=(w-tw)/2:y={ self.text2height }:fontcolor={ self.fontColor }:fontsize={ self.fontSize }"'
      output = f'{ self.savePath }/{ videoNameList[index] }'
      # videoFilter = f'[in]{ clip },{ text1 },{ text2 },eq=contrast={ self.contrast }:brightness={ self.brightness }:saturation={ self.saturation },unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5,fade=in:0:90,vignette="PI/4+random(1)*PI/50":eval=frame,hue="H=2*PI*t:s=sin(2*PI*t)+1",noise=alls=20:allf=t+u,delogo=x=10:y=10:w=150:h=100[out]'
      VF = f'[in]{ clip },eq=contrast={ self.contrast }:brightness={ self.brightness }:saturation={ self.saturation }'
      videoFilter = f'{ VF },hflip' if self.minor else VF
      cmdStr = f'ffmpeg -y -ss { self.startTime } -i { videoUrlList[index] } -to { duration - self.startTime - self.durationTime } -filter:v "setpts={ round(1/self.speedup, 2) }*PTS" -filter:a "atempo={ self.speedup }" -vf { videoFilter } { output }'
      # print(cmdStr)
      os.popen(cmdStr)
      self.set_label_func(f'当前视频加载进度：{index + 1} / { len(videoUrlList) }')
    return '视频剪辑中...'

if __name__=="__main__":
  app = QApplication(sys.argv)
  ex = VideoClip()
  ex.show()
  sys.exit(app.exec_())

# ffmpeg -y -re -i HC.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS,scale=664x1180,rotate=PI/6 [base];[1:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=332x590,rotate=5*PI/6 [upperleft]; [2:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=332x590,rotate=PI/6 [upperright]; [3:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=332x590,rotate=5*PI/6 [lowerleft]; [4:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=332x590 [lowerright]; [base][upperleft] overlay=shortest=1[tmp1];[tmp1][upperright] overlay=shortest=1:x=332 [tmp2]; [tmp2][lowerleft]overlay=shortest=1:y=590 [tmp3]; [tmp3][lowerright]overlay=shortest=1:x=332:y=590" -c:v libx264 output2.mp4

# ffmpeg -y -re -i HC.mp4 -re -i timer.mp4 -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS,scale=332x590 [base];[1:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=213x120 [upperleft]; [base][upperleft] overlay=shortest=1" -c:v libx264 output.mp4

# ffmpeg -y -re -i HC.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS,scale=664x1180 [base];[1:v] format=yuva444p,colorchannelmixer=aa=0.05,setpts=PTS-STARTPTS,scale=332x590 [upperleft]; [2:v] format=yuva444p,colorchannelmixer=aa=0.05,setpts=PTS-STARTPTS,scale=332x590 [upperright]; [3:v] format=yuva444p,colorchannelmixer=aa=0.05,setpts=PTS-STARTPTS,scale=332x590 [lowerleft]; [4:v] format=yuva444p,colorchannelmixer=aa=0.05,setpts=PTS-STARTPTS,scale=332x590 [lowerright]; [base][upperleft] overlay=shortest=1[tmp1];[tmp1][upperright] overlay=shortest=1:x=332 [tmp2]; [tmp2][lowerleft]overlay=shortest=1:y=590 [tmp3]; [tmp3][lowerright]overlay=shortest=1:x=332:y=590" -c:v libx264 output2.mp4

# ffmpeg -y -re -i output.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS,scale=664x1180 [base];[1:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590 [upperleft]; [2:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590 [upperright]; [3:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590 [lowerleft]; [4:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590 [lowerright]; [base][upperleft] overlay=shortest=1[tmp1];[tmp1][upperright] overlay=shortest=1:x=332 [tmp2]; [tmp2][lowerleft]overlay=shortest=1:y=590 [tmp3]; [tmp3][lowerright]overlay=shortest=1:x=332:y=590" -c:v libx264 output2.mp4

# ffmpeg -y -re -i origin.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i timer.mp4 -re -i mask.mp4 -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS,scale=664x1180 [base];[1:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590,rotate=PI/4:c=none [upperleft]; [2:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590,rotate=PI/3:c=none [upperright]; [3:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590,rotate=PI/6:c=none [lowerleft]; [4:v] format=yuva444p,colorchannelmixer=aa=0.02,setpts=PTS-STARTPTS,scale=332x590 [lowerright]; [5:v] format=yuva444p,colorchannelmixer=aa=0.1,setpts=PTS-STARTPTS,scale=664x1180,rotate=PI/4:c=none [mask]; [base][upperleft] overlay=shortest=1[tmp1];[tmp1][upperright] overlay=shortest=1:x=332 [tmp2]; [tmp2][lowerleft]overlay=shortest=1:y=590 [tmp3]; [tmp3][lowerright]overlay=shortest=1:x=332:y=590 [tmp4]; [tmp4][mask]overlay=shortest=1:x=0:y=0" -c:v libx264 output2.mp4