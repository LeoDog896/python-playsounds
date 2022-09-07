import os
import random
from time import sleep
from os import listdir
import pathlib
from os.path import isfile, join

mypath = '/home/pi/python-playsounds/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

while True:
  rand = random.randint(0, len(onlyfiles))
  print(rand)
  print(onlyfiles)
  os.system("cvlc --gain 1000 --vout none --play-and-exit /home/pi/sound/" + str(rand))
  sleep(1)
 #sleep(random.randint(30,3600))