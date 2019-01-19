import json
from pprint import pprint


data  = open("sidnummer.csv", "r").readlines()

songs = []

for line in data:
    
    line = line.strip().split(",")
    song = {}
    
    song["name"] = line[0]
    song["page"] = line[1]
    song["tones"], song["chord"] = line[2].split("(")
    
    song["tones"] = song["tones"].strip().split(" ")

    song["chord"] = song["chord"][:-1]
    
    songs.append(song)    
    
    pprint(song)

open("out.json", "w").write(json.dumps(songs, ensure_ascii=False)) 
