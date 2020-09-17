import os

inputVideo = r'nba/top5.mp4'
outputVideo = r'nba/finished/top1.mp4'
startTime = 10
videoDuration = 20
# cutCmdStr = f'ffmpeg -y -ss{ startTime } -i { inputVideo } -to { videoDuration } -c copy { outputVideo }'
# os.popen(cutCmdStr)

bgColor = '#6f00a7'
fontColor = '#ffff00'
clip = 'crop=iw-474:ih:937:0'
padStr = f'pad=iw:16*iw/9:0:"(16*iw/9-ih)/2":{ bgColor }'
text1 = f'drawtext="fontfile=es.ttf:text=Kawhi wanted a "DOC":x=(w-tw)/2:y=200:fontcolor={ fontColor }:fontsize=60"'
text2 = f'drawtext="fontfile=es.ttf:text=But what needs is a "NURSE":x=(w-tw)/2:y=300:fontcolor={ fontColor }:fontsize=60"'
text3 = f'drawtext="fontfile=es.ttf:text=LAKERS VS NUGGETS:x=(w-tw)/2:y=400:fontcolor={ fontColor }:fontsize=60"'
# cmdStr = f'ffmpeg -y -ss { startTime } -i  { inputVideo } -to { videoDuration } -vf [in]{ clip },{ padStr },{ text1 },{ text2 },{ text3 }[out] { outputVideo }'
cmdStr = f'ffmpeg -y -ss { startTime } -i  { inputVideo } -to { videoDuration } -vf [in]{ clip },{ padStr }[out] { outputVideo }'

os.popen(cmdStr)