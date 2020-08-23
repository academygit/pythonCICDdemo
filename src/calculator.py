"""
Calculator library containing basic math operations.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", help="first, argument to be added", type=int)
parser.add_argument("second", help="second, argument to be added", type=int)
args = parser.parse_args()

def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term

if __name__ == "__main__":
    print(f'{args.first} + {args.second} = {add(args.first, args.second)}')
    print(f'{args.first} - {args.second} = {subtract(args.first, args.second)}')