from ModelLoader import ModelLoader
from Models.NFA import NFA
from tests.ModelTests import *

def main():
  
  IS_VALID_MODELFILE = False  
  
  while(not IS_VALID_MODELFILE):
    """Prompt user to enter the file name (with .json extension) and load the model."""
    filename = input("Enter the file name (with .json extension): ")
    model_loader = ModelLoader(filename)
    IS_VALID_MODELFILE = model_loader.validModel()
  data = model_loader.readJSON()
  # print(data)
  
  """Create an instance of the model class with the data provided in the JSON file."""
  if data == None: # if the data didn't load properly exit the program
    exit()
  model = createModel(data)
  
  programLoop(model)
  
  
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
      print("Attempted to load an unknown model of computation.")
      exit()
  return model

def programLoop(model):
  """Enter program loop."""
  print("This model accepts the alphabet: ", model.sigma)
  while(True):
    input_string = str(input("Enter a test string: "))
    accepted = model.accepts(input_string)
    print(f"\'{input_string}\' is accepted.") if accepted else print(f"\'{input_string}\' is rejected.")
        
  
if __name__ == "__main__":
  main()
