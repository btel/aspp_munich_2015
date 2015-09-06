#!/bin/bash
export PYTHONPATH=../libs/pyNeuro/:$PYTHONPATH

mkdir -p ../figures ../results
SCRIPTS=../scripts

cd $SCRIPTS

python batch_analyse.py ../data/retina/data_02*.mat --dest-dir ../results

python merge_correlations.py ../results/data_02_*.npz --save ../results/merged_data.npz

python plot_correlations.py ../results/merged_data.npz --save-fig ../figures/corr_data_02.svg
