#!/usr/bin/env nextflow

// Jake Bowden 11/21

// Create a channel containing homologs from the --in path parameter:
homologs_ch = channel.fromPath(params.in)

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

// Print path to alignment (view closes but returns an identical channel):
alignment_ch = alignment_ch.view()

process FastTreePhylo {
    // Calculate tree from the alignment, open tree channel: 
    input:
    file alignment from alignment_ch

    output:
    file "output.tree" into tree_ch

    """
    FastTreeMP -out output.tree $alignment
    """
}

// Print path to output tree file:
tree_ch.view()