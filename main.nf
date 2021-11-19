#!/usr/bin/env nextflow

// Jake Bowden 11/21

// Default DB path:
params.db = "data/gbk_records/" 
// Creates a channel with a symbolic link to gbk database:
gbk_db_ch = channel.fromPath(params.db, type: "dir")
// Create a channel containing the query fasta from the --in path parameter:
query_seq_ch = channel.fromPath(params.in)


process phmmerHomologWrapper {
    // Call the phmmer wrapper python script which calls and parses results:
    input:
    file query_seq from query_seq_ch
    file gbk_db from gbk_db_ch

    output:
    file "query_homologs.fasta" into homologs_ch 

    """
    find_homologs.py -query_fasta $query_seq -db_path $gbk_db -out "query_homologs.fasta"
    """
}
homologs_ch = homologs_ch.view()


process MuscleAlign {
    // Pass homolog channel to muscle and open alignment channel:
    input:
    file homologs from homologs_ch

    output:
    file "alignment.fasta" into alignment_ch

    """
    muscle -in $homologs -out alignment.fasta
    """
}
alignment_ch = alignment_ch.view()


process FastTreePhylo {
    // Calculate tree from the alignment, open tree channel: 
    input:
    file alignment from alignment_ch

    output:
    file "output.tree" into tree_ch

    """
    fasttreeMP -out output.tree $alignment
    """
}
tree_ch.view()
