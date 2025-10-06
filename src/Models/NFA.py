import Model 

class NFA(Model.Model):
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
      super().__init__(Q, sigma, delta, q0, F)
    