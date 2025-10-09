class NFA():
  """
  Formal Definition of an NFA:
  (Q, Σ, δ, q0, F)
  
           Q - Set of all states.
   Σ (sigma) - Alphabet accepted by the model.
   δ (delta) - Transition table.
          q0 - Initial state/Start state.
           F - Set of all accepting states.
  """
  def __init__(self, Q, sigma, delta, q0, F):
    self.Q = Q
    self.sigma = sigma
    self.delta = delta
    self.q0 = q0
    self.F = F
    
  """
  Method: accepts()
  
  Argument(s):
    - input_string: a string being checked to see if it is accepted by the model
  
  Returns:
    - True: if the string is accepted by the NFA
    - False: if the string is not accepted by the NFA
  """
  def accepts(self, input_string: str) -> bool:
    # start in the initial state
    current_states = [self.q0]       # note we make current state a list to account for non-determinism
    
    # for each character in the input_string follow the model's transitions
    for char in input_string:
      if char not in self.sigma: # if the character isn't in the alphabet the input is invalid (string is not accepted regardless)
        return False
      result_states = []
      for state in current_states:
        if char in self.delta[state]:
          # follow transitions make current state all the possible next states
          result_states += self.delta[state][char]
      current_states = result_states
    
    for state in current_states:
      # if any of the current states we're in are apart of F (accepting states) then the string is accepted.
      if state in self.F:
        return True
    return False
        
      
    