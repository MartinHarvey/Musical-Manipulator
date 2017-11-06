#Importing pyDub library
from pydub import AudioSegment
#importing Tkinter modules for filedialog
from Tkinter import *
from tkFileDialog import *

#Importing Functions from file Functions.py
from Functions import *
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
    print "You can reverse, length-check and exit"
    #User command choice put into userChoice variable
    userChoice = raw_input("Please type in your choice. ")

    #Calls reverse function if chosen
    if userChoice == "reverse":
        track = track.reverse()

    if userChoice == "length-check":
        length(track)



    #Exits loop if exit is chosen
    if userChoice == "exit":
        loop = "FALSE"


#Getting save path from user
save_path = asksaveasfilename(initialdir = "/home/", title = "Where do you want to save the modified file?", filetypes = (("mp3 Files", "*.mp3"), ("all files", "*.*" )))

#Exporting and saving track to chosen file location
track.export(save_path, format = "mp3")
