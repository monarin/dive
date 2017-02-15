from __future__ import division
from prime.echidna import mod_input
import unittest, os

class readBadInput(unittest.TestCase):
  dataDir = 'test_data'
  def testMissingData(self):
    """mod_input should fail with invalid or missing data"""
    self.assertRaises(mod_input.InvalidData, mod_input.process_input, \
        ['dummy=dummier'], False)
  def testMissingPrimePhil(self):
    """mod_input should fail with missing prime phile file"""
    self.assertRaises(mod_input.InvalidPrimePhil, mod_input.process_input, \
        ['data='+self.dataDir], False)
  def testBadRunNo(self):
    """mod_input should fail with invalid run no."""
    self.assertRaises(mod_input.InvalidRunNo, mod_input.process_input, \
        ['data='+self.dataDir,'prime_phil_file=prime.phil','run_no=dummy_run_no'])

if __name__ == "__main__":
    unittest.main()
