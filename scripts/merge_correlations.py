#!/usr/bin/env python
#coding=utf-8

import numpy as np

if __name__ == "__main__":

    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('npz_files', nargs='+')
    parser.add_argument('--save', required=True)
    
    args = parser.parse_args()

    corr_coefs = []

    for path in args.npz_files:
        data = np.load(path)
        corr_coefs.append(data['corr_coefs'])

    corr_coefs = np.concatenate(corr_coefs)

    np.savez(args.save, corr_coefs = corr_coefs)
