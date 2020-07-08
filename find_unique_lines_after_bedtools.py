# In this script, we want to keep just the unique lines after bedtools intersect.
# After running bedtools intersect, there are some variants that are repeated because there are mutliple lines that are repeated in the exonic file.

import argparse

parser = argparse.ArgumentParser(description='Find unique lines after bedtools intersect.')
parser.add_argument('--infile',required=True,help='Input file.')
parser.add_argument('--outfile',required=True,help='Output file.')
parser.add_argument('--index',required=True,help='Index of the position.')

args = parser.parse_args()

pos_index = int(args.index)

positions = set()

outfile = open(args.outfile, 'w')
with open(args.infile, 'r') as f:
    for line in f:
        items = line.rstrip('\n').split('\t')
        if items[pos_index] not in positions:
            positions.add(items[pos_index])
            print (line.rstrip('\n'), file=outfile)
        else:
            continue