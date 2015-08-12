#!/bin/bash

mkdir -p ../figures ../results

python batch_analyse.py ../retina/Data/data_02*.mat --dest-dir ../results

python merge_script.py ../results/data_02_*.npz ../results/merged_data.npz

python plot_correlations.py ../results/merged_data.npz --save-fig ../figures/corr_data_02.svg
