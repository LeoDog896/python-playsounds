import os
import random
from time import sleep
from os import listdir
import pathlib
from os.path import isfile, join

mypath = '/home/pi/python-playsounds/sounds/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

os.system("cvlc --gain 100 --vout none --play-and-exit " +  mypath + "Treasure_Chest_Long_1.wav")

while True:
  # wait so the sounds are not distracting
  sleep(1)
  random_Time = random.randint(1800,3600)
  #print(random_Time)
  sleep(random_Time)

  # now play the sounds
  rand = random.randint(0, len(onlyfiles) - 1)
  #print(rand)
  #print(onlyfiles)
  os.system("cvlc --gain 100 --vout none --play-and-exit " +  mypath + onlyfiles[rand])