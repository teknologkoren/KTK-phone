import json
from pprint import pprint
import sys
import os
import subprocess

songs = json.loads(open("songs.json", "r").read())


for song in songs:
    pprint(song)
    tempfile = open("tones.tmp", "w")

    file_prefix = "file media/notes/"    

    filemapper = {
        "Ab": "giss-1s.wav",
        "A": "a-1s.wav",
        "A#": "aiss-1s.wav",
        "Bb": "aiss-1s.wav",
        "B": "b-1s.wav",
        "B#": "c-1s.wav",
        "Cb": "b-1s.wav",
        "C": "c-1s.wav",
        "C#": "ciss-1s.wav",
        "Db": "ciss-1s.wav",
        "D": "d-1s.wav",
        "D#": "diss-1s.wav",
        "Eb": "diss-1s.wav",
        "E": "e-1s.wav",
        "E#": "f-1s.wav",
        "Fb": "e-1s.wav",
        "F": "f-1s.wav",
        "F#": "fiss-1s.wav",
        "Gb": "fiss-1s.wav",
        "G": "g-1s.wav",
        "G#": "giss-1s.wav",
    }
        
    if len(song["tones"]) <= 1:
        
        file_prefix = "media/notes/"    
        command = ["cp", "{}{}".format(file_prefix, filemapper[song["tones"][0]]), "media/songstarts/{}.wav".format(song["page"])]
        pprint(command)
        subprocess.run(command)
        continue
     
    for tone in song["tones"]:
        tempfile.write("{}{}\n".format(file_prefix, filemapper[tone])) 
    tempfile.close()

    subprocess.run(["ffmpeg",  "-y", "-f", "concat",  "-i", "tones.tmp",  "-c", "copy",  "one_at_a_time.wav"])
    
    file_prefix = "media/notes/"    
    
    command = ["ffmpeg",  "-y"]
    for tone in song["tones"]:
        command.append("-i")
        command.append("{}{}".format(file_prefix, filemapper[tone])) 
    #command.extend(["-filter_complex", "amerge", "-ac", "1", "-c", "copy", "chord.wav"])
    command.extend(["-filter_complex", "amerge", "-ac", "1", "chord.wav"])
    pprint(command)
    subprocess.run(command)
    tempfile = open("tones.tmp", "w").write("file one_at_a_time.wav\nfile chord.wav")
 
    subprocess.run(["ffmpeg",  "-f", "concat",  "-i", "tones.tmp", "-c", "copy",  "media/songstarts/{}.wav".format(song["page"])])
    
