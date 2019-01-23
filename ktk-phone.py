#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, send_from_directory
import json

import config

app = Flask(__name__)

@app.route('/media/<path:path>')
def send_media(path):
    return send_from_directory('media', path)

@app.route('/new-call', methods=['POST'])
def newCall():
  out = {
    "ivr": "{}/media/main-menu.wav".format(config.base_url),
    "digits": 1, 
    #"timeout": 10,
    "repeat": 3,
    "next": "{}/handle-welcome-ivr".format(config.base_url)
  }
  return json.dumps(out) 


@app.route('/handle-welcome-ivr', methods=['POST'])
def handleWelcome():
  
  data = request.form
  result = data["result"]
  print(result)

  if result == None:
    return "Failed"

  out = {
    "next":   "{}/new-call".format(config.base_url)
  }  

  if result == "0":
    pass    

  elif result == "1":
    out = {
      "play":   "{}/media/ordf.wav".format(config.base_url),
      "next":   json.dumps({"connect":config.ordf_number})   
    }

  elif result == "2":
    out = {
      "play":   "{}/media/ordf.wav".format(config.base_url),
      "next":   json.dumps({"connect":config.ordf_number})   
    }

  elif result == "3":
    out = {
      "ivr": "{}/media/pick_a_note.wav".format(config.base_url),
      "digits": 2, 
      #"timeout": 10,
      "repeat": 3,
      "next": "{}/handle-note-ivr".format(config.base_url)
    }

  elif result == "4":
    pass

  elif result == "5":
    out = {
      "ivr": "{}/media/pick_a_song.wav".format(config.base_url),
      "digits": 2, 
      #"timeout": 10,
      "repeat": 3,
      "next": "{}/handle-song-ivr".format(config.base_url)
    }

  elif result == "6":
    pass

  elif result == "7":
    pass

  elif result == "8":
    pass

  elif result == "9":
    pass
  
  return json.dumps(out)

@app.route('/handle-note-ivr', methods=['POST'])
def handleNote():
  
  data = request.form
  result = int(data["result"])
  print(result) 
  
  notes = {
    1 : "a-5s.wav",
    2 : "aiss-5s.wav",
    3 : "b-5s.wav",
    4 : "c-5s.wav",
    5 : "ciss-5s.wav",
    6 : "d-5s.wav", 
    7 : "diss-5s.wav", 
    8 : "e-5s.wav", 
    9 : "f-5s.wav", 
    10 : "fiss-5s.wav", 
    11 : "g-5s.wav", 
    12 : "giss-5s.wav"
  }

  if result not in notes:
    out = {
      "ivr": "{}/media/pick_a_note.wav".format(config.base_url),
      "digits": 2, 
      #"timeout": 10,
      "repeat": 3,
      "next": "{}/handle-note-ivr".format(config.base_url)
    }
    return json.dumps(out)


  if result == None:
    return "Failed"
    
  out = {
    "play" : config.base_url+"/media/notes/"+notes[result], 
    "next" : {
      "play" : config.base_url+"/media/notes/"+notes[result], 
      "next" : {
        "play" : config.base_url+"/media/notes/"+notes[result]
      } 
    }
  }  
  
  return json.dumps(out)



@app.route('/handle-pagenote-ivr', methods=['POST'])
def handlePageNote():
  data = request.form
  result = int(data["result"])
  print(result) 
  
  songs = {
    1 : "a-5s.wav",
    2 : "aiss-5s.wav",
    3 : "b-5s.wav"
  }

  if result not in songs:
    out = {
      "ivr": "{}/media/pick_a_song.wav".format(config.base_url),
      "digits": 2, 
      #"timeout": 10,
      "repeat": 3,
      "next": "{}/handle-song-ivr".format(config.base_url)
    }
    return json.dumps(out)


  if result == None:
    return "Failed"
    
  out = {
    "play" : config.base_url+"/media/songs/"+songs[result], 
  }  
  
  return json.dumps(out)


@app.route('/handle-song-ivr', methods=['POST'])
def handleSong():
  
  data = request.form
  result = int(data["result"])
  print(result) 
  
  songs = {
    1 : "a-5s.wav",
    2 : "aiss-5s.wav",
    3 : "b-5s.wav"
  }

  if result not in songs:
    out = {
      "ivr": "{}/media/pick_a_song.wav".format(config.base_url),
      "digits": 2, 
      #"timeout": 10,
      "repeat": 3,
      "next": "{}/handle-song-ivr".format(config.base_url)
    }
    return json.dumps(out)


  if result == None:
    return "Failed"
    
  out = {
    "play" : config.base_url+"/media/songs/"+songs[result], 
  }  
  
  return json.dumps(out)

@app.route('/')
def entry_point():
  return "Hello! Welcome to Kongl. Teknologkörens automatic answering machine. Try calling me on: {}".format(config.answering_machine_number)

if __name__ == '__main__':
  app.run(debug=True)
