import os
bgColor = '#000000'
fontColor = '#ffff00'
startTime = 0
videoDuration = 12
inputPath = 'nba/kobe.mp4'
outputPath = 'nba/finished/kobe.mp4'
clipStr = 'crop=iw:ih/1.3'
padStr = f'pad=iw:ih+236:0:118:{ bgColor }'
# text1 = 'drawtext="fontfile=gb.ttf:text=慢下来，在微观世界里看诗和远方:x=(w-tw)/2:y=h-270:fontcolor=red:fontsize=30"'
text2 = f'drawtext="fontfile=gb.ttf:text=:x=(w-tw)/2:y=100:fontcolor={ fontColor }:fontsize=30"'
text3 = f'drawtext="fontfile=gb.ttf:text=:x=(w-tw)/2:y=170:fontcolor={ fontColor }:fontsize=30"'
text4 = f'drawtext="fontfile=gb.ttf:text=:x=(w-tw)/2:y=240:fontcolor={ fontColor }:fontsize=30"'

cmdStr = f'ffmpeg -y -ss { startTime } -i  { inputPath } -to { videoDuration } -vf [in]{ clipStr },{ padStr },{ text2 },{ text3 },{ text4 }[out] { outputPath }'

os.popen(cmdStr)