#importing pyDub library
from pydub import AudioSegment
import pydub
from __main__ import *
#Takes in variable, before reversing and passing it back out


#Takes length of track, and prints it to command line
def length(track):
    print track.duration_seconds
