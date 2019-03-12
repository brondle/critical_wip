import time
import gaugette.gpio
import gaugette.rotary_encoder
import os
from omxplayer.player import OMXPlayer
# from pathlib import Path
import sys

player = OMXPlayer("./output.mov", args=[])
player.set_alpha(150)
player.set_rate(0.5)
rate = 0.5
print(player.minimum_rate())
print(player.rate())

A_PIN = 1
B_PIN = 16
gpio = gaugette.gpio.GPIO()
encoder = gaugette.rotary_encoder.RotaryEncoder(gpio, A_PIN, B_PIN)
encoder.start()
#FIXME: weird issue where, while only comparing to delta of 1, decrease function somehow manages to decrease speed below 0.25 - possibly a timing issue?
try:
  while True:
    delta = encoder.get_cycles()
    if delta!=0:
      print "rotate %d" % delta
      print "rate: " + str(rate)
      if delta >= 5 and rate <= 1:
        player.action(2)
	rate = rate + 0.125
    else:
      if rate > 0.25:
       print "rate: " + str(rate)
       player.action(1)
       rate = rate - 0.125
    time.sleep(0.325)
except KeyboardInterrupt:
  player.quit()
  sys.exit()
