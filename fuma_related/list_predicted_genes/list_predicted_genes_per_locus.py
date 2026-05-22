import argparse
import os, sys
from collections import defaultdict

parser = argparse.ArgumentParser(description="List predicted genes per locus from positional mapping and xQTLs mapping")
parser.add_argument("--filedir",required=True,help="Input the directory")

args = parser.parse_args()

def main():
    filedir = args.filedir
    pos_fp = os.path.join(filedir, "positional_mapped_genes.txt")
    xqtls_fp = os.path.join(filedir, "xqtls_mapped_genes.txt")
    flames_fp = os.path.join(filedir, "flames_mapped_genes.txt")
    outfile = os.path.join(filedir, "mapped_genes.txt")
    out = open(outfile, "w")

    with open(pos_fp) as f:
        for line in f: 
            if line.startswith("ensg"):
                continue
            items = line.rstrip().split("\t")
            if not int(items[11]) > 0:
                continue
            print(",".join([items[15], "positional", items[1], ""]), file=out)

    xqtls_genes = defaultdict(set)        
    with open(xqtls_fp) as f:
        for line in f: 
            if line.startswith("uniqID"):
                continue
            items = line.rstrip().split("\t")
            qtl_id = items[5] + ":" + items[2]
            xqtls_genes[qtl_id].add((items[6], items[3]))
    for k, v in xqtls_genes.items():
        for i in v:
            print(",".join([i[0], "xqtls", i[1], k]), file=out)
            
    with open(flames_fp) as f:
        for line in f:
            if line.startswith("locus"):
                continue
            items = line.rstrip().split("\t")
            print(",".join([items[0], "flames", items[1], ""]), file=out)
            
    out.close()
    
if __name__ == "__main__":
    main()