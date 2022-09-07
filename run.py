import os
import random
from time import sleep

while True:
  rand = random.randint(0,30)
  print(rand)
  os.system("cvlc --gain 1000 --vout none --play-and-exit /home/pi/sound/" + str(rand) + ".ogg")
 #sleep(1)
  sleep(random.randint(30,3600))