#!/bin/bash

python calculate_correlations.py ../retina/Data/data_02_16_12_t2.mat --save ../results/data_02_16_12_t2.npz
python plot_correlations.py ../results/data_02_16_12_t2.npz --save ../figures/data_02_16_12_t2.svg
