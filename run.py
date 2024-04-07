import os
import random
from time import sleep
from os import listdir
from os.path import isfile, join

sound_path = os.path.dirname(os.path.realpath(__file__)) + "/sounds/"
effect_path = os.path.dirname(os.path.realpath(__file__)) + "/effects/"

files = [f for f in listdir(sound_path) if isfile(join(sound_path, f))]

os.system("paplay " + effect_path + "open.ogg")

print("Playing sounds every 30-60 minutes")
print("Sound directory: " + sound_path)
print("Sounds available: " + str(files))
print("Ctrl + C to stop")

lower = 60 * 30
upper = 60 * 60

while True:
  time = random.randint(lower, upper)
  print("Sleeping for " + str(time) + " seconds")
  sleep(time)

  # now play the sounds
  rand = random.randint(0, len(files) - 1)
  file = files[rand]
  print("Playing " + file)
  os.system("paplay " +  sound_path + files[rand])
