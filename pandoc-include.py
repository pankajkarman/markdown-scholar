import re, argparse
from pandoc import replace_include

parser = argparse.ArgumentParser(description='Pandoc filter for include statement')
parser.add_argument('--infile', help='Give input filename.')
parser.add_argument('--outfile', default='new.md', help='Give output filename.')
args = parser.parse_args()
print("Arguments:", args)
replace_include(args.infile, args.outfile)
