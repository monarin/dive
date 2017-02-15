from __future__ import division
# LIBTBX_SET_DISPATCHER_NAME prime.echidna
""" prime.echidna start a genetic algorithm to identify best images """
__author__ = 'Monarin Uervirojnangkoorn, monarin@gmail.com'

import sys
from prime.echidna.mod_input import process_input
from prime.echidna.mod_optimize import xfel_pattern_optimizer

def run(args):
  #read inputs
  iparams, txt_out_input = process_input(args)
  xfelph = xfel_pattern_optimizer(iparams)

if (__name__ == "__main__"):
  run(sys.argv[1:] if len(sys.argv) > 1 else None)
