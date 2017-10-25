#Importing pyDub library
from pydub import AudioSegment

#Getting File Path to Audio from user
file_path = raw_input("Where is your chosen audio file?")

#Importing audio file into variable track
track = AudioSegment.from_mp3(file_path)

#Reversing track
track = track.reverse()

#Getting save path from user
save_path = raw_input("Where do you want to save the reversed file?")

#Exporting and saving track to chosen file location
track.export(save_path, format = "mp3")
