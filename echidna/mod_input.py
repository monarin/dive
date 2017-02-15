from __future__ import division

class ReadInputError(Exception): pass
class InvalidData(ReadInputError): pass
class InvalidRunNo(ReadInputError): pass
class InvalidPrimePhil(ReadInputError): pass

from cctbx.array_family import flex
import iotbx.phil
from libtbx.utils import Usage, Sorry
import sys, os, glob

master_phil = iotbx.phil.parse("""
data = None
  .type = path
  .multiple = True
  .help = Directory containing integrated data in pickle format.  Repeat to \
    specify additional directories.
run_no = None
  .type = str
  .help = Run no. is used as folder name that stores output files.
prime_phil_file = None
  .type = path
  .help = Path to prime parameter file (no data parameter).
title = None
  .type = str
  .help = Title of the run.
ga_params
  .help = genetic algorithm parameters.
{
  pop_size = 100
    .type = int
    .help = No. of chromosomes in the population.
  idv_length = 1000
    .type = int
    .help = No. of chromosomes in the population.
  prob_cross = 0.95
    .type = float
    .help = Probability of crossover.
  ratio_cross = 0.2
    .type = float
    .help = Fractions used in crossing over.
  prob_mutation = 0.01
    .type = float
    .help = Probability of mutation.
  n_mutations = 1
    .type = int
    .help = No. of mutation points.
  max_gen = 100
    .type = int
    .help = Maximum number of generations.
  xmap_radius = 3
    .type = int
    .help = No. of cells used during map local search.
  num_sel_mate = 15
    .type = int
    .help = NA
  crossover_start_rate = 0.2
    .type = float
    .help = Starting crossover rate.
  crossover_end_rate = 0.2
    .type = float
    .help = Final crossover rate.
  crossover_slope = 1.0
    .type = float
    .help = Slope of the crossover rate function.
}
""")

txt_help = """**************************************************************************************************

prime.echidna identify select out of group of images that deliver the best target function.

Usage: prime.echidna parameter.phil

For feedback, please contact monarin@stanford.edu.

**************************************************************************************************

List of available parameters:
"""
def process_input(argv=None, flag_check_exist=True):
  user_phil = []
  if argv == None:
    master_phil.show()
    raise Usage("Use the above list of parameters to generate your input file (.phil). For more information, run prime.echidna -h.")
  else:
    for arg in argv:
      if os.path.isfile(arg):
        user_phil.append(iotbx.phil.parse(open(arg).read()))
      elif (os.path.isdir(arg)) :
        user_phil.append(iotbx.phil.parse("""data=\"%s\"""" % arg))
      else :
        if arg == '--help' or arg == '-h':
          print txt_help
          master_phil.show(attributes_level=1)
          raise Usage("Run prime.echidna to generate a list of initial parameters.")
        else:
          try:
            user_phil.append(iotbx.phil.parse(arg))
          except RuntimeError, e :
            raise Sorry("Unrecognized argument '%s' (error: %s)" % (arg, str(e)))
  #setup phil parameters
  working_phil = master_phil.fetch(sources=user_phil)
  params = working_phil.extract()
  if not params.data:
    raise InvalidData, "Error: Data is required. Please specify path to your data folder (data=/path/to/integration/results)."
  #check prime phil file
  if not params.prime_phil_file:
    raise InvalidPrimePhil, "Error: Prime parameter file is required. Please specify a valid prime phil file (prime_phil_file=prime.phil). You can use prime.run to generate the file."
  #generate run_no folder
  if flag_check_exist:
    if not params.run_no:
      #use default name (Echidna_Run_1)
      default_run = 'Echidna_Run_'
      all_runs = glob.glob(default_run+'*')
      new_run_no = 1
      if all_runs: new_run_no = max([int(run_no.split('_')[-1]) for run_no in all_runs])+1
      params.run_no = default_run+str(new_run_no)
    elif os.path.exists(params.run_no):
      print "Warning: run number %s already exists."%(params.run_no)
      run_overwrite = raw_input('Overwrite?: N/Y (Enter for default)')
      if run_overwrite == 'Y':
        shutil.rmtree(params.run_no)
      else:
        raise InvalidRunNo, "Error: Run number exists. Please specifiy different run no."
  #make result folders
  os.makedirs(params.run_no)
  #capture input read out by phil
  from cStringIO import StringIO
  class Capturing(list):
    def __enter__(self):
      self._stdout = sys.stdout
      sys.stdout = self._stringio = StringIO()
      return self
    def __exit__(self, *args):
      self.extend(self._stringio.getvalue().splitlines())
      sys.stdout = self._stdout
  with Capturing() as output:
    working_phil.show()
  txt_out = 'prime.echidna input:\n'
  for one_output in output:
    txt_out += one_output + '\n'
  print txt_out
  return params, txt_out
