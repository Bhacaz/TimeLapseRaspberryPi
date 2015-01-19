#!/bin/sh
 
 
#for i in $( ls *.jpeg); do convert -resize 1280x720 $i $i; done
 
#mencoder -nosound -mf fps=30 -o timeLapse_monter.avi -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=8000 mf://*jpeg

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse.avi -mf type=jpeg:fps=30 mf://*jpeg
