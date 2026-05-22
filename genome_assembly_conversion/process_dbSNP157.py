# this script processed the downloaded file GCF_000001405.40.gz for easily convert to chromosome position to GRCh38 coordinates from rsID or vice versa
# one file for each chromosome
# columns in each file: chromsome (number), position, rsID, ref, alt

import gzip
import argparse
import os

parser = argparse.ArgumentParser(description="Format downloaded dbSNP file to use for tabix")
parser.add_argument("--in_gzip",required=True,help="For example: GCF_000001405.40.gz")
parser.add_argument("--directory",required=True,help="Input the directory")
parser.add_argument("--chrom",required=True,help="chrom name in the downloaded dbSNP file. For example: NC_000017.11")
parser.add_argument("--new_chrom",required=True,help="chromosome number to use in the output file. For example: 17")

args = parser.parse_args()

chrom=args.chrom
chrom_number=args.new_chrom

outfile=open(f"{args.directory}/dbSNP157.chr{chrom_number}.vcf", "w")

with gzip.open(os.path.join(args.directory, args.in_gzip), "rt") as infile:
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

# count lines in the output file
import subprocess
line_count = int(subprocess.check_output(["wc", "-l", f"{args.directory}/dbSNP157.chr{chrom_number}.vcf"]).split()[0])
print(f"Total {line_count} lines written to dbSNP157.chr{chrom_number}.vcf")
    