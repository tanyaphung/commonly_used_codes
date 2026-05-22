# this script converts the file gencode.v39.annotation.gtf.gz to a file with the following columns:
# gene_id, gene_type, gene_name, hgnc_id

import gzip

outfile = open("gene_name_conversion.tsv", "w")
header = ["gene_id", "gene_type", "gene_name", "hgnc_id", "chr", "start", "end"]
print("\t".join(header), file=outfile)

with gzip.open("gencode.v39.annotation.gtf.gz", "rt") as infile:
    for line in infile:
        if line.startswith("#"):
            continue
        fields = line.strip().split("\t")
        attributes_field = fields[8]
        attributes = {}
        for attribute in attributes_field.split(";"):
            attribute = attribute.strip()
            if attribute:
                key, value = attribute.split(" ")
                attributes[key] = value.strip('"')
        gene_id = attributes.get("gene_id", "")
        gene_type = attributes.get("gene_type", "")
        gene_name = attributes.get("gene_name", "")
        hgnc_id = attributes.get("hgnc_id", "")
        out = [gene_id, gene_type, gene_name, hgnc_id, fields[0], fields[3], fields[4]]
        outfile.write("\t".join(out) + "\n")