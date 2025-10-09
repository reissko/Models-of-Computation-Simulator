import json

class ModelLoader:

  path = "inputs/"
  
  def __init__(self, filename):
    self.filepath = self.path + filename
    
    
  """
  Attemps to open the user-provided json file and return the model as a python dictionary. If
  The file cannot be opened, the program will catch the exception and issue a warning.
  """
  def readJSON(self):
    try:
      with open(self.filepath) as f:
        return json.load(f)
    except FileNotFoundError:
      print("File not found")
  
  """
  Checks if the user-provided json file exists.
  """  
  def validModel(self):
    try:
      with open(self.filepath) as f:
        return True
    except FileNotFoundError:
      print(self.filepath.replace("inputs/", "") + " does not exist. Please check the spelling and try again. Make sure to include the .json extension.")
      return False