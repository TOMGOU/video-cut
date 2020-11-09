import win_unicode_console
win_unicode_console.enable()
import sys
import os
import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QProgressBar, QApplication, QColorDialog, QFileDialog)
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
    self.source_le = QLineEdit(r'C:\demo\02_SUMMARY\29_automation\video-cut\origin', self)
    self.source_le.move(120, 30)
    self.source_le.resize(450,30)

    # 处理后的视频存储路径
    self.save_btn = QPushButton('存储路径：', self)
    self.save_btn.move(20, 75)
    self.save_btn.resize(100,30)
    self.save_btn.clicked.connect(self.select_save)
    self.save_le = QLineEdit(r'C:\demo\02_SUMMARY\29_automation\video-cut\PIP', self)
    self.save_le.move(120, 75)
    self.save_le.resize(450,30)

    # 定时器视频
    self.timerLabel = QPushButton('定时器视频：', self)
    self.timerLabel.move(20, 120)
    self.timerLabel.resize(100, 30)
    self.timerLabel.clicked.connect(self.select_timer)
    self.timer_le = QLineEdit(r'C:\demo\02_SUMMARY\29_automation\video-cut\tiktok\timer.mp4', self)
    self.timer_le.move(120, 120)
    self.timer_le.resize(400, 30)
    self.timeropacity_le = QLineEdit('0.02', self)
    self.timeropacity_le.move(525, 120)
    self.timeropacity_le.resize(45, 30)

    # 热点视频
    self.maskLabel = QPushButton('热点视频：', self)
    self.maskLabel.move(20, 165)
    self.maskLabel.resize(100, 30)
    self.maskLabel.clicked.connect(self.select_mask)
    self.mask_le = QLineEdit(r'C:\demo\02_SUMMARY\29_automation\video-cut\tiktok\mask.mp4', self)
    self.mask_le.move(120, 165)
    self.mask_le.resize(400, 30)
    self.maskopacity_le = QLineEdit('0.02', self)
    self.maskopacity_le.move(525, 165)
    self.maskopacity_le.resize(45, 30)

    #开始剪辑按钮
    self.save_btn = QPushButton('开始剪辑视频',self)
    self.save_btn.move(450, 235)
    self.save_btn.resize(120, 50)
    self.save_btn.clicked.connect(self.kick)

    #用户提示区
    self.result_le = QLabel('请填写视频剪辑相关参数', self)
    self.result_le.move(30, 280)
    self.result_le.resize(340, 30)
    self.result_le.setStyleSheet('color: blue;')

    # 整体界面设置
    self.resize(600, 400)
    self.center()
    self.setWindowTitle('抖音视频画中画剪辑')#设置界面标题名
    self.show()
  
  # 窗口居中函数
  def center(self):
    screen = QtWidgets.QDesktopWidget().screenGeometry()#获取屏幕分辨率
    size = self.geometry()#获取窗口尺寸
    self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))#利用move函数窗口居中
  
  def select_source(self):
    dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件夹路径", "C:/")
    self.source_le.setText(str(dir_path))
  
  def select_timer(self):
    dir_path, fileType = QFileDialog.getOpenFileName(self, "请选择源文件夹路径", "C:/")
    self.timer_le.setText(str(dir_path))

  def select_mask(self):
    dir_path, fileType = QFileDialog.getOpenFileName(self, "请选择源文件夹路径", "C:/")
    self.mask_le.setText(str(dir_path))

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
    timerPath = self.timer_le.text().strip()
    timerOpacity = float(self.timeropacity_le.text().strip())
    maskPath = self.mask_le.text().strip()
    maskOpacity = float(self.maskopacity_le.text().strip())
    if self.switch and sourcePath != '' and savePath != '' and timerPath != '' and timerOpacity != '' and maskPath != '' and maskOpacity != '':
      self.switch = False
      self.set_label_func('请耐心等待，正在打开浏览器！')
      self.my_thread = MyThread(sourcePath, savePath, timerPath, timerOpacity, maskPath, maskOpacity, self.set_label_func)#实例化线程对象
      self.my_thread.start()#启动线程
      self.my_thread.my_signal.connect(self.switch_func)

class MyThread(QThread):
  my_signal = pyqtSignal(bool)
  def __init__(self, sourcePath, savePath, timerPath, timerOpacity, maskPath, maskOpacity, set_label_func):
    super(MyThread, self).__init__()
    self.sourcePath = sourcePath
    self.savePath = savePath
    self.timerPath = timerPath
    self.timerOpacity = timerOpacity
    self.maskPath = maskPath
    self.maskOpacity = maskOpacity
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
      clip = VideoFileClip(videoUrlList[index])
      originWidth = int(clip.size[0])
      originHeight = int(clip.size[1])
      scale = f'{ int(originWidth / 2) }x{ int(originHeight / 2) }'
      full = f'{ 2 * originWidth }x{ 2 * originHeight }'
      output = f'{ self.savePath }/{ videoNameList[index] }'
      cmdStr = f'ffmpeg -y -re -i { videoUrlList[index] } -re -i { self.timerPath } -re -i { self.timerPath } -re -i { self.timerPath } -re -i { self.timerPath } -re -i { self.maskPath } -filter_complex "[0:v] format=rgb24,setpts=PTS-STARTPTS [base];[1:v] format=yuva444p,colorchannelmixer=aa={ self.timerOpacity },setpts=PTS-STARTPTS,scale={ scale },rotate=random(1)*PI:c=none [upperleft]; [2:v] format=yuva444p,colorchannelmixer=aa={ self.timerOpacity },setpts=PTS-STARTPTS,scale={ scale },rotate=random(1)*PI:c=none [upperright]; [3:v] format=yuva444p,colorchannelmixer=aa={ self.timerOpacity },setpts=PTS-STARTPTS,scale={ scale },rotate=random(1)*PI:c=none [lowerleft]; [4:v] format=yuva444p,colorchannelmixer=aa={ self.timerOpacity },setpts=PTS-STARTPTS,scale={ scale },rotate=random(1)*PI:c=none [lowerright]; [5:v] format=yuva444p,colorchannelmixer=aa={ self.maskOpacity },setpts=PTS-STARTPTS,scale={ full },rotate={ random.random() }*PI:c=none [mask]; [base][upperleft] overlay=shortest=1[tmp1];[tmp1][upperright] overlay=shortest=1:x={ int(originWidth / 2) } [tmp2]; [tmp2][lowerleft]overlay=shortest=1:y={ int(originHeight / 2) } [tmp3]; [tmp3][lowerright]overlay=shortest=1:x={ int(originWidth / 2) }:y={ int(originHeight / 2) } [tmp4]; [tmp4][mask]overlay=shortest=1:x={ -int(originWidth / 2) }:y={ -int(originHeight / 2) }" -c:v libx264 { output }'
      # print(cmdStr)
      os.popen(cmdStr)
      self.set_label_func(f'当前视频加载进度：{index + 1} / { len(videoUrlList) }')
    return '视频剪辑中...'

if __name__=="__main__":
  app = QApplication(sys.argv)
  ex = VideoClip()
  ex.show()
  sys.exit(app.exec_())
