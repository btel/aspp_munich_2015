#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('npz_file')
    parser.add_argument('--save-fig')
    
    args = parser.parse_args()

    data = np.load(args.npz_file)
    corr_coefs = data['corr_coefs']

    plt.hist(corr_coefs, 100)
    plt.xlabel('correlation coefficients')
    plt.ylabel('count')

    if args.save_fig:
        plt.savefig(args.save_fig)
    else:
        plt.show()
