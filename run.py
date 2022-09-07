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
  rand = random.randint(0, len(onlyfiles) - 1)
  sleep(random.randint(30,3600))
  
  #print(rand)
  #print(onlyfiles)
  os.system("cvlc --gain 100 --vout none --play-and-exit " +  mypath + onlyfiles[rand])
  sleep(1)
  #sleep(random.randint(30,3600))