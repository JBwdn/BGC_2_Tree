#!/usr/bin/env nextflow

homologs_ch = channel.fromPath(params.in)

process MuscleAlign {
    input:
    file homologs from homologs_ch

    output:
    file "alignment.fasta" into alignment_ch

    """
    muscle -in $homologs -out alignment.fasta
    """
}

process FastTreePhylo {
    input:
    file alignment from alignment_ch

    output:
    file "output.tree" into tree_ch

    """
    FastTreeMP -out output.tree $alignment
    """
}

alignment_ch.view()
tree_ch.view()