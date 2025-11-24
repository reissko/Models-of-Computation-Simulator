# imports
import os
import json
from .ModelLoader import ModelLoader
from .Models.NFA import NFA


"""
  Parameters:
    - formal_definition: string = An array representing the formal definition of a model of computation
  Returns:
    - model_json: dict = A dictionary representation of the model
"""
def parseModelComponents(model_type: str, Q: str, sigma: str, delta: str, q0: str, F: str) -> dict:
  # variables for creating model parts
  Q_var: list[str] = []
  sigma_var: list[str] = []
  delta_var: dict = {}
  q0_var: str = q0
  F_var: list[str] = []
  # begin parsing
  value = ""
  for char in Q: # parse Q
    if char == "[" or char == "]" or char == "\'" or char == "\"" or char == " ":
      continue
    elif char == ",":
      if value != "":
        Q_var.append(value)
        value = ""
    else:
      value += char
  if value != "":
    Q_var.append(value)
    value = ""
  for char in sigma: # parse sigma
    if char == "[" or char == "]" or char == "\'" or char == "\"" or char == " ":
      continue
    elif char == ",":
      if value != "":
        sigma_var.append(value)
        value = ""
    else:
      value += char
  if value != "":
    sigma_var.append(value)
    value = ""
  
  delta_table = json.loads(delta)
  print(delta_table)
  for key in delta_table.keys():
    delta_var[key] = delta_table[key]
  # strip quotes off of q0
  q0_var = q0_var.strip("\"")
  value = ""
  for char in F: # parse F
    if char == "[" or char == "]" or char == "\'" or char == "\"" or char == " ":
      continue
    elif char == ",":
      if value != "":
        F_var.append(value)
        value = ""
    else:
      value += char
  if value != "":
    F_var.append(value)
    value = ""
  
  # create the dictionary
  model_dict = {
    "model": model_type,
    "Q": Q_var,
    "sigma": sigma_var,
    "delta": delta_var,
    "q0": q0_var,
    "F": F_var
  }
  return model_dict
      
"""
  Description:
    Writes a model to a file in json format.
  Parameters:
    - model_json: dict = A dictionary representation of the model
    - filename: string = The name of the file to write the model to
"""
def writeModelToFile(model_json: dict, filename: str):
  downloads_folder = ""
  if os.name == "nt":  # Windows
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
  else: # Unix, macOS, etc.
    downloads_folder = os.path.join(os.getenv('HOME'), 'Downloads')
  with open(downloads_folder + "/" + filename, "w") as f:
    json.dump(model_json, f)

"""
  Parameters:
    - data: dict = A dictionary representation of the model
  Returns:
    - model: (DFA/NFA/PDA/TM) = An instance of the model
"""
def createModel(data: dict):
  
  match data["model"]:
    case "DFA":
      pass
    case "NFA":
      model = NFA(
        data["Q"],
        data["sigma"],
        data["delta"],
        data["q0"],
        data["F"]
      )
    case "PDA":
      pass
    case "TM":
      pass
    case _:
      print("Something Unexpected Happened. :(")
      exit()
  return model