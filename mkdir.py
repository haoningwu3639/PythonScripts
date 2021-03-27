# mkdir.py
# Created: 27th March 2021

"""
You can input a parameter 'input_dir' to create a new directory,
by default, it will make a sub directory in the current working directory,
you can also input an absolute path to create the directory wherever you want.
"""

__author__ = "HaoningWu"
__version__ = "1.0"

import os
import argparse

def mkdir(input_dir):
    flag = os.path.exists(input_dir)
    if not flag:
        os.makedirs(input_dir)
        print("New Directory:", input_dir)
    else:
        print("Directory already exists")

def get_parser():
    parser = argparse.ArgumentParser(description='mkdir')
    # Defaultly, it will make a sub directory in the current working Directory.
    # You must input a 'input_dir' here.
    parser.add_argument('--input_dir', type=str, default='new_dir', required=True, help='Input the directory path/name you want to make.')

    return parser
    
def main():
    parser = get_parser()
    args = parser.parse_args()

    input_dir = args.input_dir
    mkdir(input_dir)

if __name__ == '__main__':
    main()