#Importing pyDub library
from pydub import AudioSegment
#importing Tkinter modules for filedialog
from Tkinter import *
from tkFileDialog import *

#Initilising variables
userChoice = ""
file_path = ""
save_path = ""
loop = "TRUE"

#Getting File Path to Audio from user
file_path = askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))

#Importing audio file into variable track
track = AudioSegment.from_mp3(file_path)

#Loop continues until exit command is given
while loop == "TRUE":
    #Users given choice of commands
    print "You can reverse, duration, repeat, edit volume, merge tracks, check volume and exit"
    #User command choice put into userChoice variable
    userChoice = raw_input("Please type in your choice. ")

    #Calls reverse function if chosen
    if userChoice == "reverse":
        track = track.reverse()

    if userChoice == "duration":
        print "The track is " + str(int(track.duration_seconds)) + " seconds long."

    #Exits loop if exit is chosen
    if userChoice == "exit":
        loop = "FALSE"

    if userChoice == "repeat":
        track = track * 2

    if userChoice == "edit volume":
        gain = raw_input("By how many dB do you wish to edit volume? ")
        track = track + gain

    if userChoice == "merge tracks":
        file_path = askopenfilename(initialdir = "/home/", title = "What do you want to merge track with?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))
        mergeTrack = AudioSegment.from_mp3(file_path)
        track = track + mergeTrack

    if userChoice == "volume":
        print "Relative volume is " + str(int(track.dBFS)) + " dB."





#Getting save path from user
save_path = asksaveasfilename(initialdir = "/home/", title = "Where do you want to save the modified file?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))

#Exporting and saving track to chosen file location
track.export(save_path, format = "mp3")
