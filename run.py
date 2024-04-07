import os
import random
from time import sleep
from os import listdir
from os.path import isfile, join

my_path = os.path.dirname(os.path.realpath(__file__)) + "/sounds/"

files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

os.system("aplay " +  my_path + "Treasure_Chest_Long.wav")

print("Playing sounds every 30-60 minutes")
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
  os.system("aplay " +  my_path + files[rand])
