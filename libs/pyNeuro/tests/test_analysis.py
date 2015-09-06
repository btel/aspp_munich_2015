#!/usr/bin/env python
#coding=utf-8


from pyNeuro import analysis
import numpy as np

def test_correlations_not_exceeding_one():
    spt1 = np.array([2, 5, 5.5, 10,  12], dtype=float) 
    r = analysis.calc_corr_coef(spt1, spt1, 1.)
    assert np.abs(r-1.) < 0.05

def test_random_spikes():
    spt1 = np.cumsum(np.random.exponential(100, size=1000))
    spt2 = np.cumsum(np.random.exponential(100, size=1000))
    r = analysis.calc_corr_coef(spt1, spt2, 10.)
    assert np.abs(r) < 0.05

def test_empty_spikes():
    spt1 = np.array([])
    spt2 = np.array([2, 4, 5])
    assert analysis.calc_corr_coef(spt1, spt2) == 0
    assert analysis.calc_corr_coef(spt2, spt1) == 0
