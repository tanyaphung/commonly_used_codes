# this script processed the downloaded file GCF_000001405.40.gz for easily convert to chromosome position to GRCh38 coordinates from rsID or vice versa
# one file for each chromosome
# columns in each file: chromsome (number), position, rsID, ref, alt

import gzip
import argparse

parser = argparse.ArgumentParser(description="Format downloaded dbSNP file to use for tabix")
parser.add_argument("--chrom",required=True,help="chrom name in the downloaded dbSNP file. For example: NC_000017.11")
parser.add_argument("--new_chrom",required=True,help="chromosome number to use in the output file. For example: 17")

args = parser.parse_args()

chrom=args.chrom
chrom_number=args.new_chrom

outfile=open(f"dbSNP157.chr{chrom_number}.vcf", "w")

with gzip.open("GCF_000001405.40.gz", "rt") as infile:
    for line in infile:
        if not line.startswith(chrom):
            continue
        fields = line.rstrip("\n").split("\t")
        pos = fields[1]
        rsid = fields[2]
        ref = fields[3]
        alt = fields[4]
        
        print("\t".join([chrom_number, pos, rsid, ref, alt]), file=outfile)
        
outfile.close()
    