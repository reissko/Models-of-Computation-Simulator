from tkinter import Tk
from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import Entry

class GUI:
  
  frame = None
  
  # button styles
  #############################
  BUTTON_WIDTH = 15           #
  VERT_SPACE = 10             #
  BUTTON_FONT = ("Arial", 16) #
  BUTTON_FG = "white"         #
  BUTTON_BG = "#1c1c1c"     #
  #############################
  
  def __init__(self):
    self.root = Tk()
    self.root.title("Model of Computation Validator")
    self.root.geometry("800x400") # 800x400 px
    self.root.resizable(False, False)
    
    # load main menu
    self.mainMenuScreen()
  def mainMenuScreen(self):
    # destroy previous frame if it exists
    if self.frame != None:
      self.frame.destroy()
    self.frame = ttk.Frame(self.root, padding="3 3 12 12")
    # welcome label
    welcome_label = Label(self.frame, text="Welcome to the Model of\nComputation Validator!", font=("Arial", 20), pady=10)
    welcome_label.pack()    
    
    # 1) Load and Test
    load_and_test_button = Button(self.frame, text="Load and Test", command=self.loadAndTestScreen)
    # 2) Create Model
    create_model_button = Button(self.frame, text="Create Model", command=self.createModelScreen)
    # 3) Exit
    exit_button = Button(self.frame, text="Exit", command=self.root.destroy)
    # apply button styles
    self.applyButtonStyle(load_and_test_button)
    self.applyButtonStyle(create_model_button)
    self.applyButtonStyle(exit_button)
    # pack buttons to the frame
    load_and_test_button.place(relx=0.5, rely=0.35, anchor="center")
    create_model_button.place(relx=0.5, rely=0.55, anchor="center")
    exit_button.place(relx=0.5, rely=0.75, anchor="center")
    
    # pack the frame to the root
    self.frame.pack(expand=True, fill="both")
  def loadAndTestScreen(self):
    if self.frame != None:
      self.frame.destroy()
    self.frame = ttk.Frame(self.root, padding="3 3 12 12")  
    # file name label
    filename_label = Label(self.frame, text="No file selected", font=("Arial", 16), pady=10)
    filename_label.pack()
    # user input box
    user_input_box = Entry(self.frame, font=("Arial", 14), width=17, justify="center")
    def getUserInput(event=None):
      user_input = user_input_box.get()
      print(user_input) # for debugging
      user_input_box.delete(0, "end") # clears the input box after submission
    user_input_box.bind("<Return>", getUserInput) # allows the user to press enter to submit
    user_input_box.place(relx=0.5, rely=0.35, anchor="center")
    # submit button
    submit_button = Button(self.frame, text="Submit", command=getUserInput)
    self.applyButtonStyle(submit_button)
    submit_button.place(relx=0.5, rely=0.5, anchor="center")
    # allow the user to choose a file to load
    def selectFile():
      file_path = filedialog.askopenfilename()
      file_path = file_path.split("/")[-1].strip(".json")
      # update the label to show the file name
      filename_label.config(text=file_path)
    select_file_button = Button(self.frame, text="Select File", command=selectFile)
    menu_button = Button(self.frame, text="Main Menu", command=self.mainMenuScreen)
    self.applyButtonStyle(select_file_button)
    self.applyButtonStyle(menu_button)
    menu_button.place(relx=0.8, rely=0.75, anchor="center")
    select_file_button.place(relx=0.2, rely=0.75, anchor="center")
    self.frame.pack(expand=True, fill="both")
  def createModelScreen(self):
    if self.frame != None:
      self.frame.destroy()
    print("create model screen")
 
  ########################################
  # Helper Functions
  ########################################
  @staticmethod
  def applyButtonStyle(button):
      button.config(
        width=GUI.BUTTON_WIDTH,
        pady=GUI.VERT_SPACE,
        font=GUI.BUTTON_FONT,
        fg=GUI.BUTTON_FG,
        bg=GUI.BUTTON_BG,
        cursor="hand2",
        activebackground="#009D0A",
        activeforeground="black"
      )
      
      
      
if __name__ == "__main__":
  gui = GUI()
  gui.root.mainloop()