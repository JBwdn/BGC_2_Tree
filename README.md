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

References: 

- MUSCLE
- FastTree
