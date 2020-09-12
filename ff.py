import os
bgColor = '#99FF33'
fontColor = '#000000'
clipStr = 'crop=iw:ih/2'
padStr = f'pad=iw:ih+588:0:294:{ bgColor }'
# text1 = 'drawtext="fontfile=gb.ttf:text=慢下来，在微观世界里看诗和远方:x=(w-tw)/2:y=h-270:fontcolor=red:fontsize=30"'
text2 = f'drawtext="fontfile=gb.ttf:text=学着让生活慢下来:x=(w-tw)/2:y=100:fontcolor={ fontColor }:fontsize=30"'
text3 = f'drawtext="fontfile=gb.ttf:text=静心去感受四周平凡的事物:x=(w-tw)/2:y=170:fontcolor={ fontColor }:fontsize=30"'
text4 = f'drawtext="fontfile=gb.ttf:text=你会惊奇的发现你的笔里有鱼:x=(w-tw)/2:y=240:fontcolor={ fontColor }:fontsize=30"'

cmdStr = f'ffmpeg -y  -i  paper.mp4  -vf [in]{ clipStr },{ padStr },{ text2 },{ text3 },{ text4 }[out] paperM.mp4'

os.popen(cmdStr)