import argparse

parser = argparse.ArgumentParser(description="Convert GTF file to bed file format.")
parser.add_argument("--input_gtf",required=True,help="Input the path to the GTF file")
parser.add_argument("--output_bed",required=True,help="Input the path to the output bed file")
parser.add_argument("--chromosome",required=True,help="Input the chromosome name. For example: chrX")

args = parser.parse_args()


outfile = open(args.output_bed, "w")

with open(args.input_gtf, "r") as f:
    for line in f:
        if line.startswith(args.chromosome):
            items = line.rstrip('\n').split('\t')
            gene_name_list = items[8].split('; ')
            for i in gene_name_list:
                if i.startswith('gene_name'):
                    gene_name = i.split(" ")[1]
            out = [items[0], str(int(items[3])-1), items[4], gene_name.strip("\"")]
            print ('\t'.join(out), file=outfile)
