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
    "ivr": "{}/media/main-menu.wav".format(base_url),
    "digits": 1, 
    #"timeout": 10,
    "repeat": 3,
    "next": "{}/handle-welcome-ivr".format(base_url)
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
    "next":   "{}/new-call".format(base_url)
  }  

  if result == "0":
    pass    

  elif result == "1":
    out = {
      "play":   "{}/media/ordf.wav".format(base_url),
      "next":   json.dumps({"connect":config.ordf_number})   
    }

  elif result == "2":
    out = {
      "play":   "{}/media/ordf.wav".format(base_url),
      "next":   json.dumps({"connect":config.ordf_number})   
    }

  elif result == "3":
    pass

  elif result == "4":
    pass

  elif result == "5":
    pass

  elif result == "6":
    out = {
      "play":   "{}/media/osquar.wav".format(base_url)
    }

  elif result == "7":
    pass

  elif result == "8":
    pass

  elif result == "9":
    pass
  
  return json.dumps(out)


@app.route('/')
def entry_point():
  return 'Hello! Welcome to Kongl. Teknologkörens automatic answering machine'

if __name__ == '__main__':
  app.run(debug=True)
