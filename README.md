# BGC2Tree pipeline

For creating phylogenetic trees of homologous proteins from biosynthetic gene clusters

Using [NextFlow](https://www.nextflow.io/docs/latest/index.html) and this [template](https://github.com/JBwdn/nextflow_template).

Example local usage: 

    nextflow run main.nf --in data/example_query.fasta --db data/gbk_records

Remote usage: 

    nextflow run jinfo-dev/bgc2tree --in your_local_query.fasta --db your_local_direcory_of_gbks

Description: 

    1. Accept a query fasta containing 1 sequence and a path to a folder containing .gbk records
    2. Using phmmer find a potential homolog from each record and save all into a fasta with labels
    3. Perform protein sequence alignment using MUSCLE
    4. Use alignment to calculate a phylogenetic Tree using FastTree
    5. Paths to the three output files (homologs, alignment & tree) printed to stdout

Installation: (Tested in WSL2 Ubuntu 20.04.2 LTS)

    sudo apt update
    sudo apt install hmmer muscle fasttree
    pip install jinfo Bio

See Nextflow docs for installation instructions.

References: 

- pHMMER: Eddy2009 ([10.1142/9781848165632_0019](https://doi.org/10.1142/9781848165632_0019))
- MUSCLE: Edgar2004 ([10.1186/1471-2105-5-113](https://doi.org/10.1186/1471-2105-5-113))
- FastTree: Price2010 ([10.1371/journal.pone.0009490](https://doi.org/10.1371/journal.pone.0009490))
