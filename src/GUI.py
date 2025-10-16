from tkinter import Tk
from tkinter import ttk

class GUI:
  def __init__(self):
    self.root = Tk()
    self.root.title("Model of Computation Validator")
    self.root.geometry("800x400") # 800x400 px
    self.root.resizable(False, False)

    
 
if __name__ == "__main__":
  gui = GUI()
  gui.root.mainloop()