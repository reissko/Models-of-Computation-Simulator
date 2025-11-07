import json

class ModelLoader:

  dynamic_path = ""
  
  def __init__(self, filepath: str):
    self.dynamic_filepath = filepath
    
    
    
  """
  Attemps to open the user-provided json file and return the model as a python dictionary. If
  The file cannot be opened, the program will catch the exception and issue a warning.
  """
  def readJSON(self):
    try:
      with open(self.dynamic_filepath) as f:
        return json.load(f)
    except FileNotFoundError:
      print("File not found")
  
  """
  Checks if the user-provided json file exists.
  """  
  def validModel(self):
    try:
      with open(self.dynamic_filepath) as f:
        return True
    except FileNotFoundError:
      print("File not found")
      return False