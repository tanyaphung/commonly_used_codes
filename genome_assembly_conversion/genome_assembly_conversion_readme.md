## rsID with tabix

### Pre-process rsID
1. Download dbSNP157
```
wget https://ftp.ncbi.nih.gov/snp/latest_release/VCF/GCF_000001405.40.gz
```

2. Process to format to be used for tabix

- Extract chr, pos, rsID, ref, alt
    - need to look up the NC value for the chromosome number (https://www.ncbi.nlm.nih.gov/grc/human/data?asm=GRCh38.p13)

```
python ./process_dbsnp157.py --chrom NC_000017.11 --new_chrom 17
```

- bgzip and tabix
```
bgzip ./dbSNP157.chr17.vcf
tabix -p vcf ./dbSNP157.chr17.vcf.gz
```

3. Example code for looking up rsID and chr:pos

- In Python
```
import tabix
rsid_tb = tabix.open("dbSNP157.chr" + chrom + ".vcf.gz")
rsid_querried_results = rsid_tb.querys(query_region) 
```