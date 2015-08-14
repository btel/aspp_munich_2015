#!/usr/bin/env python
#coding=utf-8

from glob import glob
import os
from pathlib import Path

root = Path('..')
data_folder = root / 'data' / 'retina'

input_files = list(data_folder.glob('*.mat'))
result_files = [str(root / 'results' / inp.with_suffix('.npz').name)
                for inp in input_files]

def task_calculate_correlations():
    
    for inp, out in zip(input_files, result_files):
        yield {
                'actions'  : ['python calculate_correlations.py '
                              '%(dependencies)s --save %(targets)s'],
                'file_dep' : [str(inp)],
                'targets'  : [out],
                'name'     : inp.name
              }

def task_merge_correlations():
    output = str(root / 'results' / 'merged_correlations.npz')
    return {
            'actions'  : ['python merge_script.py '
                         '%(dependencies)s %(targets)s'],
            'file_dep' : result_files,
            'targets'  : [output]
           }

def task_plot_correlations():
    input_file = str(root / 'results' / 'merged_correlations.npz') 
    svg_file = str(root / 'figures' / 'correlation_plot.svg')
    return {
            'actions'  : ['python plot_correlations.py '
                          '%(dependencies)s --save %(targets)s'],
            'file_dep' : [input_file],
            'targets'  : [svg_file]
           }
