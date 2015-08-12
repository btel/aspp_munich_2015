#!/usr/bin/env python
#coding=utf-8

from subprocess import call
import os

if __name__ == "__main__":

    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mat_files', nargs='+')
    parser.add_argument('--dest-dir')
    
    args = parser.parse_args()

    for path in args.mat_files:
        _, filename = os.path.split(path)

        result_name = os.path.join(args.dest_dir, filename)

        cmd_args = ' {} --save {}'.format(path, result_name)
        cmd = 'python calculate_correlations.py'
        call([cmd + cmd_args], shell=True)

