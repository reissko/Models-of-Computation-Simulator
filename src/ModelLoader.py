import json

class ModelLoader:
    
  def __init__(self):
      pass
    
  def readJSON(self, path):
    with open(path) as f:
      return json.load(f)