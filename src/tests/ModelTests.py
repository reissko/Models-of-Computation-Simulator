import unittest
import sys
sys.path.append("../")
from ModelLoader import ModelLoader
from Models.NFA import NFA

class DFAUnitTests(unittest.TestCase):
  pass    

class NFAUnitTests(unittest.TestCase):

  def setUp(self):
    self.model_loader = ModelLoader("exampleNFA.json")
    # needs a special path for tests since they are doubly nested in src folder
    self.model_loader.filepath = "../../inputs/exampleNFA.json"
    self.data = self.model_loader.readJSON()
    assert self.data != None
    self.model = NFA(
      self.data["Q"],
      self.data["sigma"],
      self.data["delta"],
      self.data["q0"],
      self.data["F"]
    )
    
  def test_accept_cases(self):
    self.assertTrue(self.model.accepts("aa"))
    self.assertTrue(self.model.accepts("aaa"))
    self.assertTrue(self.model.accepts("bbaa"))
    
  def test_reject_cases(self):
    self.assertFalse(self.model.accepts("ba"))
    self.assertFalse(self.model.accepts("bab"))
    self.assertFalse(self.model.accepts("baab"))
    
class PDAUnitTests(unittest.TestCase):
  pass

class TMUnitTests(unittest.TestCase):
  pass

if __name__ == '__main__':
  unittest.main()