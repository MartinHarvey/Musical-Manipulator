#This program was originally designed to help improve my python programming. Althouh still very elementary, it also helped me with
#using Git for version control. An external library, pyDub is used for all sound operations. It is very high level and is similar to
#regular Python. It has various functions for reversing, repeating audio, to name a few. I hope to implement more functions in the
#future. The file dialog ability comes from Tkinter, which allows GUI functions to be implemented in Python. It may be replaced by PyQt
#as I create a proper GUI, rather than having a CLI.

#Importing pyDub library
from pydub import AudioSegment
#importing Tkinter modules for filedialog
from Tkinter import *
from tkFileDialog import *

#Initilising variables
userChoice = ""
file_path = ""
save_path = ""
loop = True

#Getting File Path to Audio from user
file_path = askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))

#Importing audio file into variable trackusing Got
track = AudioSegment.from_mp3(file_path)

#Loop continues until exit command is given
while loop == True:
    #Users given choice of commands
    print "You can reverse, duration, repeat, edit volume, merge tracks, check volume and exit"
    #User command choice put into userChoice variable
    userChoice = raw_input("Please type in your choice. ")

    #Calls reverse function if chosen
    if userChoice == "reverse":
        #Track then becomes the reverse of itself
        track = track.reverse()
        print "Track Reversed."

    if userChoice == "duration":
        #The duration_seconds function in pyDub returns the track length as a decimal value. This is better reoresented to the user as an integer in my personal opinion.
        #As result, the int function is then called to round the output of the duration_seconds seconds function to an easier to digest integer.
        print "The track is " + str(int(track.duration_seconds)) + " seconds long."

    #Exits loop if exit is chosen
    if userChoice == "exit":
        loop = False

    if userChoice == "repeat":
        #repeats the contents of track
        track = track * 2
        print "Track Repeated."

    if userChoice == "edit volume":
        #feature allows user to change volume of entire contents of track
        #Receiving input for 'gain' variable
        gain = raw_input("By how many dB do you wish to edit volume? ")
        #pyDub allows you to change volume using simple syntax outlined below
        track = track + gain
        print "Gain changed by " + gain "."

    if userChoice == "merge tracks":
        # This feature allows the user to concantenate a track onto the end of what they originally imported into the program
        #THe following line calls in a fileDialog widget from Tkinter, allowing the user to select a file from any part of the users directory
        #The path of the imported file is stored in the variable 'file_path'
        file_path = askopenfilename(initialdir = "/home/", title = "What do you want to merge track with?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))
        #The file is imported into pyDub using the AudioSegment function, allowing it to be edited using PyDub functions
        mergeTrack = AudioSegment.from_mp3(file_path)
        #The imported audio is concantenated onto the end of the original track
        track = track + mergeTrack
        print "Tracks merged"

    if userChoice == "volume":
        #This returns the relative volume of the variable 'track' as an integer
        print "Relative volume is " + str(int(track.dBFS)) + " dB."

#Getting save path from user
save_path = asksaveasfilename(initialdir = "/home/", title = "Where do you want to save the modified file?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))

#Exporting and saving track to chosen file location
track.export(save_path, format = "mp3")
