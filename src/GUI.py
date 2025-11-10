from tkinter import Tk
from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import Entry
from tkinter import StringVar
from tkinter import OptionMenu

from Utils import *

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
    model = None
    # destroy previous frame if it exists
    if self.frame != None:
      self.frame.destroy()
    self.frame = ttk.Frame(self.root, padding="3 3 12 12")  
    accept_reject_warning_label = Label(self.frame, text="", font=("Arial", 16), pady=10, fg="red")
    accept_reject_warning_label.place(relx=0.5, rely=0.20, anchor="center")
    # file name label
    filename_label = Label(self.frame, text="No file selected", font=("Arial", 16), pady=10)
    filename_label.pack()
    # user input box
    user_input_box = Entry(self.frame, font=("Arial", 14), width=17, justify="center")
    def getUserInput(event=None):
      if model is None:
        accept_reject_warning_label.config(text="WARNING: Please select a model file to test.")
        return
      user_input = user_input_box.get()
      accept_reject_warning_label.config(text=f"")
      # print(user_input) # for debugging
      if model.accepts(user_input):
        accept_reject_warning_label.config(text=f"{user_input} is accepted.", fg="green")
      else:
        accept_reject_warning_label.config(text=f"{user_input} is rejected.", fg="red")
      user_input_box.delete(0, "end") # clears the input box after submission
    user_input_box.bind("<Return>", getUserInput) # allows the user to press enter to submit
    user_input_box.place(relx=0.5, rely=0.35, anchor="center")
    # submit button
    submit_button = Button(self.frame, text="Submit", command=getUserInput)
    self.applyButtonStyle(submit_button)
    submit_button.place(relx=0.5, rely=0.5, anchor="center")
    # allow the user to choose a file to load
    def selectFile():
      nonlocal model # when we refer to 'model' we do not mean a local variable 'model'
      filepath = filedialog.askopenfilename()
      filename = filepath.split("/")[-1].strip(".json")
      # create model object
      model_loader = ModelLoader(filepath)
      if model_loader.validModel():
        data = model_loader.readJSON()
        if data:
          model = createModel(data)
          # update the label to show the file name
          filename_label.config(text=f"{filename} accepts the alphabet: {model.sigma}")
          accept_reject_warning_label.config(text="")
        else:
          accept_reject_warning_label.config(text="WARNING: This file contains an invalid formal definition.")
      else:
        accept_reject_warning_label.config(text="WARNING: Please select a valid model file.")
      
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
    self.frame = ttk.Frame(self.root, padding="3 3 12 12")
    # have the user fill out a form to create a model
    # 1) Model Type
    model_type_label = Label(self.frame, text="Model Type: ", font=("Arial", 16), pady=10, padx=10).grid(row=0, column=0)
    model_options = ["DFA", "NFA", "PDA", "TM"] # model options
    model_type_var = StringVar(self.frame) # variable to hold the model type
    model_type_var.set(model_options[0]) # default
    model_type_menu = OptionMenu(self.frame, model_type_var, *model_options)
    model_type_menu.grid(row=0, column=1, sticky="w")
    # 2) Q
    Q_label = Label(self.frame, text="Q: ", font=("Arial", 16), pady=10, padx=10).grid(row=1, column=0)
    Q_input = Entry(self.frame, font=("Arial", 12), width=20, justify="center")
    Q_input.grid(row=1, column=1)
    # 3) Sigma
    sigma_label = Label(self.frame, text="Sigma: ", font=("Arial", 16), pady=10, padx=10).grid(row=2, column=0)
    sigma_input = Entry(self.frame, font=("Arial", 12), width=20, justify="center")
    sigma_input.grid(row=2, column=1)
    # 4) Delta
    delta_label = Label(self.frame, text="Delta: ", font=("Arial", 16), pady=10, padx=10).grid(row=3, column=0)
    delta_input = Entry(self.frame, font=("Arial", 12), width=20, justify="center")
    delta_input.grid(row=3, column=1)
    # 5) q0
    q0_label = Label(self.frame, text="q0: ", font=("Arial", 16), pady=10, padx=10).grid(row=4, column=0)
    q0_input = Entry(self.frame, font=("Arial", 12), width=20, justify="center")
    q0_input.grid(row=4, column=1)
    # 6) F
    F_label = Label(self.frame, text="F: ", font=("Arial", 16), pady=10, padx=10).grid(row=5, column=0)
    F_input = Entry(self.frame, font=("Arial", 12), width=20, justify="center")
    F_input.grid(row=5, column=1)
    # 7) Submit
    warning_label = Label(self.frame, text="", font=("Arial", 16), padx=10, fg="red")
    warning_label.place(relx=0.75, rely=0.5, anchor="center")
    def handleModelCreation(event=None):
      model_type = model_type_var.get()
      Q = Q_input.get()
      sigma = sigma_input.get()
      delta = delta_input.get()
      q0 = q0_input.get()
      F = F_input.get()
      if not all([model_type, Q, sigma, delta, q0, F]):
        warning_label.config(text="WARNING: Please fill out all fields.")
        return
      # hide the warning label if the correct inputs are given
      warning_label.config(text="")
      # parse the model components into a dictionary
      model_json = parseModelComponents(model_type, Q, sigma, delta, q0, F)
      # create the model file and save it to the inputs directory
      writeModelToFile(model_json, "my_model.json")
      
    submit_button = Button(self.frame, text="Create Model", command=handleModelCreation)
    self.applyButtonStyle(submit_button)
    submit_button.grid(row=6, column=0, columnspan=2, pady=15)  
    
    # help button
    help_button = Button(self.frame, text="Help", command=self.modelCreationHelpScreen)
    self.applyButtonStyle(help_button)
    help_button.place(relx=0.75, rely=0.3, anchor="center")
    # main menu button
    menu_button = Button(self.frame, text="Main Menu", command=self.mainMenuScreen)
    self.applyButtonStyle(menu_button)
    menu_button.place(relx=0.75, rely=0.7, anchor="center")
    
    self.frame.pack(expand=True, fill="both")
    
    # bind all inputs to be entered with <Return> key
    Q_input.bind("<Return>", handleModelCreation)
    sigma_input.bind("<Return>", handleModelCreation)
    delta_input.bind("<Return>", handleModelCreation)
    q0_input.bind("<Return>", handleModelCreation)
    F_input.bind("<Return>", handleModelCreation)
    
  def modelCreationHelpScreen(self):
    if self.frame != None:
      self.frame.destroy()
    self.frame = ttk.Frame(self.root, padding="3 3 12 12")
    help_explanation_label = Label(self.frame, text="Just write the model out in an actual\nJSON file it's so much easier.", font=("Arial", 16), pady=10)
    help_explanation_label.place(relx=0.5, rely=0.5, anchor="center")
    
    back_button = Button(self.frame, text="Back", command=self.createModelScreen)
    self.applyButtonStyle(back_button)
    back_button.place(relx=0.5, rely=0.8, anchor="center")
    
    self.frame.pack(expand=True, fill="both")
    
    
    
    
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