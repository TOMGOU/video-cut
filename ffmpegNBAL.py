import win_unicode_console
win_unicode_console.enable()
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QProgressBar, QApplication, QColorDialog, QFileDialog)
from PyQt5.QtGui import QColor

class VideoClip(QWidget):
  def __init__(self):
    super(VideoClip, self).__init__()
    self.switch = True
    self.initUI()

  def initUI(self):
    # 视频源文件路径
    self.source_btn = QPushButton('源文件：', self)
    self.source_btn.move(20, 30)
    self.source_btn.resize(100,30)
    self.source_btn.clicked.connect(self.select_source)
    self.source_le = QLineEdit(r'/Users/tangyong/test/automation/video-cut/nba/top5.mp4', self)
    self.source_le.move(120, 30)
    self.source_le.resize(450,30)

    # 处理后的视频存储路径
    self.save_btn = QPushButton('存储路径：', self)
    self.save_btn.move(20, 75)
    self.save_btn.resize(100,30)
    self.save_btn.clicked.connect(self.select_save)
    self.save_le = QLineEdit(r'/Users/tangyong/test/automation/video-cut/nba/finished/top2.mp4', self)
    self.save_le.move(120, 75)
    self.save_le.resize(450,30)

    # 背景颜色调色板
    self.bg_color_btn = QPushButton('背景颜色：', self)
    self.bg_color_btn.move(20, 120)
    self.bg_color_btn.resize(100,30)
    self.bg_color_btn.clicked.connect(self.showBgColorDialog)
    self.bg_color_le = QLineEdit('#6f00a7', self)
    self.bg_color_le.move(120, 120)
    self.bg_color_le.resize(60,30)

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
    self.start_size_le = QLineEdit('50', self)
    self.start_size_le.move(530, 120)
    self.start_size_le.resize(40,30)

    # 视频裁剪开始时间参数
    self.startLabel = QLabel(self)
    self.startLabel.move(30, 165)
    self.startLabel.resize(100, 30)
    self.startLabel.setText("开始时间(s)：")
    self.start_le = QLineEdit('0', self)
    self.start_le.move(120, 165)
    self.start_le.resize(150, 30)

    # 视频裁剪总时长参数
    self.durationLabel = QLabel(self)
    self.durationLabel.move(330, 165)
    self.durationLabel.resize(100, 30)
    self.durationLabel.setText("视频时间(s)：")
    self.duration_le = QLineEdit('10', self)
    self.duration_le.move(420, 165)
    self.duration_le.resize(150, 30)

    # 视频裁剪宽
    self.widthLabel = QLabel(self)
    self.widthLabel.move(30, 210)
    self.widthLabel.resize(100, 30)
    self.widthLabel.setText("剪切宽度：")
    self.width_le = QLineEdit('800', self)
    self.width_le.move(120, 210)
    self.width_le.resize(150, 30)

    # 视频裁剪高
    self.heightLabel = QLabel(self)
    self.heightLabel.move(330, 210)
    self.heightLabel.resize(100, 30)
    self.heightLabel.setText("剪切高度：")
    self.height_le = QLineEdit('130', self)
    self.height_le.move(420, 210)
    self.height_le.resize(150, 30)

    # 视频裁剪宽
    self.startXLabel = QLabel(self)
    self.startXLabel.move(30, 255)
    self.startXLabel.resize(100, 30)
    self.startXLabel.setText("X开始坐标：")
    self.startX_le = QLineEdit('400', self)
    self.startX_le.move(120, 255)
    self.startX_le.resize(150, 30)

    # 视频裁剪高
    self.startYLabel = QLabel(self)
    self.startYLabel.move(330, 255)
    self.startYLabel.resize(100, 30)
    self.startYLabel.setText("Y开始坐标：")
    self.startY_le = QLineEdit('0', self)
    self.startY_le.move(420, 255)
    self.startY_le.resize(150, 30)

    # 第一段文案
    self.text1Label = QLabel(self)
    self.text1Label.move(30, 300)
    self.text1Label.resize(100, 30)
    self.text1Label.setText("第一段文案：")
    self.text1_le = QLineEdit('湖人大胜马赛克', self)
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
    self.text2height_le = QLineEdit('400', self)
    self.text2height_le.move(525, 345)
    self.text2height_le.resize(45, 30)

    # 第三段文案
    self.text3Label = QLabel(self)
    self.text3Label.move(30, 390)
    self.text3Label.resize(100, 30)
    self.text3Label.setText("第三段文案：")
    self.text3_le = QLineEdit('', self)
    self.text3_le.move(120, 390)
    self.text3_le.resize(400, 30)
    self.text3height_le = QLineEdit('550', self)
    self.text3height_le.move(525, 390)
    self.text3height_le.resize(45, 30)

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

  def select_source(self):
    dir_path, fileType = QFileDialog.getOpenFileName(self, "请选择源文件夹路径", "C:/")
    self.source_le.setText(str(dir_path))

  def select_save(self):
    dir_path = QFileDialog.getExistingDirectory(self, "请选择处理后视频保存路径", "C:/")
    self.save_le.setText(str(dir_path))

  def set_label_func(self, text):
    self.result_le.setText(text)

  def switch_func(self, bools):
    self.switch = bools

  def showBgColorDialog(self):
    col = QColorDialog.getColor()
    if col.isValid():
      self.bg_color_le.setText(str(col.name()))

  def showFontColorDialog(self):
    col = QColorDialog.getColor()
    if col.isValid():
      self.font_color_le.setText(str(col.name()))

  def kick(self):
    sourcePath = self.source_le.text().strip()
    savePath = self.save_le.text().strip()
    bgColor = self.bg_color_le.text().strip()
    fontColor = self.font_color_le.text().strip()
    fontSize = int(self.start_size_le.text().strip())
    startTime = int(self.start_le.text().strip())
    durationTime = int(self.duration_le.text().strip())
    width = int(self.width_le.text().strip())
    height = int(self.height_le.text().strip())
    startX = int(self.startX_le.text().strip())
    startY = int(self.startY_le.text().strip())
    text1 = self.text1_le.text().strip()
    text1height = int(self.text1height_le.text().strip())
    text2 = self.text2_le.text().strip()
    text2height = int(self.text2height_le.text().strip())
    text3 = self.text3_le.text().strip()
    text3height = int(self.text3height_le.text().strip())
    print(sourcePath, savePath, bgColor, fontColor, text1, text2, text3)
    if self.switch and sourcePath != '' and savePath != '' and bgColor != '' and fontColor != '':
      self.switch = False
      self.set_label_func('请耐心等待，正在打开浏览器！')
      self.my_thread = MyThread(sourcePath, savePath, bgColor, fontColor, fontSize, startTime, durationTime, width, height, startX, startY, text1, text1height, text2, text2height, text3, text3height, self.set_label_func)#实例化线程对象
      self.my_thread.start()#启动线程
      self.my_thread.my_signal.connect(self.switch_func)

class MyThread(QThread):
  my_signal = pyqtSignal(bool)
  def __init__(self, sourcePath, savePath, bgColor, fontColor, fontSize, startTime, durationTime, width, height, startX, startY, text1, text1height, text2, text2height, text3, text3height, set_label_func):
    super(MyThread, self).__init__()
    self.sourcePath = sourcePath
    self.savePath = savePath
    self.bgColor = bgColor
    self.fontColor = fontColor
    self.fontSize = fontSize
    self.startTime = startTime
    self.durationTime = durationTime
    self.width = width
    self.height = height
    self.startX = startX
    self.startY = startY
    self.text1 = text1
    self.text1height = text1height
    self.text2 = text2
    self.text2height = text2height
    self.text3 = text3
    self.text3height = text3height
    self.set_label_func = set_label_func

  def run(self): #线程执行函数
    string = self.videoCut()
    self.set_label_func(string)
    self.my_signal.emit(True)  #释放自定义的信号

  def videoCut(self):
    clip = f'crop=iw-{ self.width }:ih-{ self.height }:{ self.startX }:{ self.startY }'
    padStr = f'pad=iw:16*iw/9:0:"(16*iw/9-ih)/2":{ self.bgColor }'
    text1 = f'drawtext="fontfile=gb.ttf:text={ self.text1 }:x=(w-tw)/2:y={ self.text1height }:fontcolor={ self.fontColor }:fontsize={ self.fontSize }"'
    text2 = f'drawtext="fontfile=gb.ttf:text={ self.text2 }:x=(w-tw)/2:y={ self.text2height }:fontcolor={ self.fontColor }:fontsize={ self.fontSize }"'
    text3 = f'drawtext="fontfile=gb.ttf:text={ self.text3 }:x=(w-tw)/2:y={ self.text3height }:fontcolor={ self.fontColor }:fontsize={ self.fontSize }"'
    cmdStr = f'ffmpeg -y -ss { self.startTime } -i  { self.sourcePath } -to { self.durationTime } -vf [in]{ clip },{ padStr },hflip,{ text1 },{ text2 },{ text3 }[out] { self.savePath }'
    os.popen(cmdStr)
    return '视频剪辑中...'

if __name__=="__main__":
  app = QApplication(sys.argv)
  ex = VideoClip()
  ex.show()
  sys.exit(app.exec_())
