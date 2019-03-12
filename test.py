import os

from omxplayer.player import OMXPlayer
# from pathlib import Path
from time import sleep
import sys

# VIDEO_PATH = Path("./vid.mp4")

player = OMXPlayer("./vid.mp4", args=[])
player.set_alpha(125)

try:
  sleep(5)
  player.pause()
  player.action(2)
  sleep(1)
  player.pause()
  player.action(2)
  player.play()
  sleep(1)
  player.action(2)
  sleep(1)
  player.action(2)
  sleep(1)
except KeyboardInterrupt:
  player.quit()
  sys.exit()
# os.system('mkfifo t cat t | omxplayer --no-osd -b vid.mp4 &')
# os.system('echo p > t rm t')


# time.sleep(1)
# play_pause()
# time.sleep(1)
# play_pause()
