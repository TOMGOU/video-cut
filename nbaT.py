import os

inputVideo = r'nba\HC.mp4'
outputVideo = r'nba\finished\HC5.mp4'
startTime = 1
videoDuration = 19
# cutCmdStr = f'ffmpeg -y -ss{ startTime } -i { inputVideo } -to { videoDuration } -c copy { outputVideo }'
# os.popen(cutCmdStr)

bgColor = '#55007f'
fontColor = '#ffff00'
clip = 'crop=iw-560:ih:280:0'
padStr = f'pad=iw:ih+560:0:280:{ bgColor }'
t1 = 'Jimmy. Buckets.'
t2 = 'Clutch Mode. GG.'
t3 = 'Imagine if Tatum made'
t4 = 'that last second 3 pointer'
text1 = f'drawtext="fontfile=ff.ttf:text={ t1 }:x=(w-tw)/2:y=130:fontcolor={ fontColor }:fontsize=50"'
text2 = f'drawtext="fontfile=ff.ttf:text={ t2 }:x=(w-tw)/2:y=200:fontcolor={ fontColor }:fontsize=50"'
cmdStr = f'ffmpeg -y -ss { startTime } -i  { inputVideo } -to { videoDuration } -vf [in]{ clip },{ padStr },{ text1 },{ text2 }[out] { outputVideo }'

os.popen(cmdStr)