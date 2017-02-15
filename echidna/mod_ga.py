from __future__ import division
""" A genetic algorithm with population id as int """

__author__ = 'Monarin Uervirojnangkoorn, monarin@gmail.com'

import random

class ga_handler(object):

  def __init__(self, iparams, idv_range):
    """ generate population storing integer sampled from a given range """
    self.pop_size = iparams.ga_params.pop_size
    self.idv_length = iparams.ga_params.idv_length
    self.idv_range = idv_range
    self.prob_cross = iparams.ga_params.prob_cross
    self.prob_mutation = iparams.ga_params.prob_mutation
    self.n_mutations = iparams.ga_params.n_mutations
    self.pop = [random.sample(range(idv_range), self.idv_length) for _ in range(self.pop_size)]
    self.fit = [0]*self.pop_size
    #generate crossover template
    n_cross_points = int(round(iparams.ga_params.ratio_cross * self.idv_length))
    self.cross_template = random.sample(range(self.idv_length), n_cross_points)

  def crossover(self, parent1, parent2):
    """ do unicross crossover - return two offsprings """
    child1 = parent1[:]
    child2 = parent2[:]
    if random.random() < self.prob_cross:
      child1[self.cross_template] = parent2[self.cross_template]
      child2[self.cross_template] = parent1[self.cross_template]
    return child1, child2

  def mutation(self, parent):
    child=parent[:];
    if random.random() < self.prob_mutation:
      mut_template = random.sample(range(self.idv_length), self.n_mutations)
      child[mut_template] = random.sample(range(idv_range), self.n_mutations)
    return child
