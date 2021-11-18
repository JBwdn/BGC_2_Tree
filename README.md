# Phylogenetics pipeline

Using [NextFlow](https://www.nextflow.io/docs/latest/index.html) and [this  template](https://github.com/JBwdn/nextflow_template).

Local usage: 

    nextflow run main.nf --in data/example_homologs.fasta

Remote usage: 

    nextflow run jbwdn/nextflow_simple_phylogenetics --in your_local_homologs.fasta

Description: 

    1. Accept a set of homolog protein sequeces in fasta format
    2. Perform protein sequence alignment using MUSCLE
    3. Use alignment to calculate a phylogenetic Tree using FastTree

Installation: (Tested in WSL2 Ubuntu 20.04.2 LTS)

    sudo apt update
    sudo apt install muscle
    sudo apt install fasttree

See Nextflow docs for installation instructions.

References: 

- MUSCLE: Edgar2004 ([10.1186/1471-2105-5-113](https://doi.org/10.1186/1471-2105-5-113))
- FastTree: Price2010 ([10.1371/journal.pone.0009490](https://doi.org/10.1371/journal.pone.0009490))
