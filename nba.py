import os

inputVideo = r'nba\lbj.mp4'
outputVideo = r'nba\finished\lbjvideo.mp4'
startTime = 65
videoDuration = 20
# cutCmdStr = f'ffmpeg -y -ss{ startTime } -i { inputVideo } -to { videoDuration } -c copy { outputVideo }'
# os.popen(cutCmdStr)

bgColor = '#6f00a7'
fontColor = '#ffff00'
clip = 'crop=iw-400:ih-150:200:0'
padStr = f'pad=iw:ih+1000:0:500:{ bgColor }'
text1 = f'drawtext="fontfile=gb.ttf:text=湖人大胜马赛克:x=(w-tw)/2:y=200:fontcolor={ fontColor }:fontsize=60"'
text2 = f'drawtext="fontfile=gb.ttf:text=同情威少5分钟:x=(w-tw)/2:y=300:fontcolor={ fontColor }:fontsize=60"'
text3 = f'drawtext="fontfile=gb.ttf:text=湖人总冠军，没人有异议吧？:x=(w-tw)/2:y=400:fontcolor={ fontColor }:fontsize=60"'
cmdStr = f'ffmpeg -y -ss { startTime } -i  { inputVideo } -to { videoDuration } -vf [in]{ clip },{ padStr },{ text1 },{ text2 },{ text3 }[out] { outputVideo }'

os.popen(cmdStr)