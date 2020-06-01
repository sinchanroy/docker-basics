import argparse
import time

def input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', help='take program number as input')
    args = parser.parse_args()
    return args

def root(args):
    for i in range(10):
        print("Hello World from : " + str(args.number))
        time.sleep(2)


if __name__ == "__main__":
    args = input()
    root(args)