#!/usr/bin/python3
import os
from datetime import datetime

folderName = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
os.system("mkdir ~/Desktop/" + folderName)
os.chdir("/home/pi/Desktop/" + folderName)

#nbPhotoSec = input ('Combien de seconde entre chaque photo : ')
#nbPhotoSec = 1 / int(nbPhotoSec)
#nbPhoto = input('Combien de photo voulez-vous prendre : ')

nbPhotoSec = 1
nbPhoto = 100

commande = 'streamer -t bbb -r aaa -o image0000.jpeg -c /dev/video0'
commande = commande.replace('aaa', str(nbPhotoSec))
commande = commande.replace('bbb', str(nbPhoto))

print(commande)

os.system(commande)
os.system("timeLapse.sh")
