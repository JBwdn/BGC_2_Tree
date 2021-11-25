# BGC2Tree pipeline

For creating phylogenetic trees of homologous proteins from biosynthetic gene clusters

Requirements: (Tested in WSL2 Ubuntu 20.04.2 LTS)
- [NextFlow](https://www.nextflow.io/docs/latest/index.html)
- [Conda](https://docs.conda.io/en/latest/) 
    
Example local usage: 

    nextflow run main.nf --in data/example_query.fasta --db data/gbk_records

Remote usage: 

    nextflow run jbwdn/bgc_2_tree --in your_local_query.fasta --db your_local_direcory_of_gbks

Description: 

    1. Accept a query fasta containing 1 sequence and a path to a folder containing .gbk records
    2. Using phmmer find a potential homolog from each record and save all into a fasta with labels
    3. Perform protein sequence alignment using MUSCLE
    4. Use alignment to calculate a phylogenetic Tree using FastTree
    5. Paths to the three output files (homologs, alignment & tree) printed to stdout

See Nextflow and conda docs for installation instructions.

Built using this [template](https://github.com/JBwdn/nextflow_template).

## References: 

- pHMMER: Eddy2009 ([10.1142/9781848165632_0019](https://doi.org/10.1142/9781848165632_0019))
- MUSCLE: Edgar2004 ([10.1186/1471-2105-5-113](https://doi.org/10.1186/1471-2105-5-113))
- FastTree: Price2010 ([10.1371/journal.pone.0009490](https://doi.org/10.1371/journal.pone.0009490))
