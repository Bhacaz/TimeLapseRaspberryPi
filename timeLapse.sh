#!/bin/sh


for i in $( ls *.jpeg); do convert -resize 1280x720 $i $i; done

mencoder -nosound -mf fps=30 -o timeLapse_monter.avi -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=8000 mf://*jpeg
