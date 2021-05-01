
#!/bin/bash
# Author: Frenzoid
# This script is meant to be ran on a rapsberry, but it should work on any system with a camera attached to it.

# $1: time to wait until next loop.
# $2: path/name to give to the outpit image.
# $3: gaussianDistortion degree.

apt-get -y update && apt-get -y upgrade && apt-get -y install python3 python3-opencv screen fswebcam;
chmod +x screen_script.sh;
screen -d -S IMAGE_LOOP_PROCESS -m ./screen_script.sh $1 $2 $3;