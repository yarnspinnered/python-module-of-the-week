import argparse

parser = argparse.ArgumentParser(description='This parses arguments')

#arguments trigger actions
# Action 1: store argument
# Action 2: Store a constant value
# Count number of arguments

parser.add_argument('necessary', nargs='+', action='store', default=False)
parser.add_argument('-a', action='store_true', default=False)
parser.add_argument('-b', action='store', dest='b', default=33)
parser.add_argument('-c', action='store', dest='c', type=int, help="help for c")

#file args
parser.add_argument('-infile', action='store',  type=argparse.FileType('rt'), help="a file")
ns = parser.parse_args(['1','2','3', '-infile', '/home/j/testio', '-a'])

print(ns)