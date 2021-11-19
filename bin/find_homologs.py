#!/usr/bin/env python

"""
Workflow for extracting homologous proteins from BGC .gbk records
Generates a fasta file of homologous AA sequences for MSA and phylo tree calculations

HOW TO USE:
1. Set up query sequence and add path to QUERY_SEQ_PATH varianble, 
    EG. Cyc from Act BGC to find all cyclases...

2. Set up genbank format dataset in genbank_records/ directory
    EG. Collect as many as you can automatically from MIBIG into this folder

3. Install hmmer package using: sudo apt-get install hmmer

4. Set output fasta path: 
    - This will contain phmmer's best hit for the query from each cluster BGC
    - Uses the filename of the cluster genbank file as the fasta header

5. Execute script:
    - Might take a while with many clusters depending on size
    - Only 1 second with my 3 test clusters though... 
"""

# Import modules from python standard library:
import os
import time
import subprocess
import re
import argparse

# Import bioinformatics modules:
import jinfo as j  # pip3 install jinfo
from Bio import SeqIO


# Parse CL arguments:
parser = argparse.ArgumentParser(
    description="Phmmer wrapper to find homologous genes from BGC gbk records"
)
parser.add_argument(
    "-query_fasta",
    required=True,
    help="Path to fasta containing one sequence to find homologs of",
)
parser.add_argument(
    "-db_path",
    required=False,
    default="data/gbk_records/",
    help="Path to folder containing GBK records to search",
)
parser.add_argument(
    "-out_fasta", required=False, default="phmmer_hits.fasta", help="Output fasta path"
)
args = parser.parse_args()

# Define constants:
QUERY_SEQ_PATH = args.query_fasta
GBK_PATH = args.db_path
HOMOLOGS_PATH = args.out_fasta


# Exception for if phmmer is not installed properly:
class HmmerNotInstalledError(Exception):
    pass


# Functions:
def gbk2fasta(gbk_file_path, outfile_path):
    """
    Convert .gbk file to .fasta file
    Using Bio as jinfo cant work with gbk...yet :( :
    """
    gbk_record = SeqIO.read(gbk_file_path, format="genbank")
    record_cds_only = [
        feature for feature in gbk_record.features if feature.type == "CDS"
    ]

    with open(outfile_path, "w") as outfile:
        for i, feature in enumerate(record_cds_only):
            print(
                f">!!!!!{i}", file=outfile
            )  # Using this label format to make it easy to parse later...
            print(feature.qualifiers["translation"][0], file=outfile)
    return


def parse_phmmer_output(result_path):
    """
    Read the fasta header of the sequence with highest homology
    from a phmmer result file
    returns: string
    """
    with open(result_path, "r") as infile:
        results_str = infile.read()
        # Hacky regex solution to parsing results...
        try:
            hit = re.findall(r"!!!!![0-9]*", results_str)[0]
            return hit
        except IndexError:
            return None


def phmmer_wrapper(db_path, query_seq_path):
    """
    Wrapper for the unix tool phmmer
    Query a fasta containing protein sequences for homologues
    returns jinfo.sequence.AASeq object
    """
    # Generate temporary file name to save results to:
    temp_file_path2 = time.strftime("%H_%M_%S", time.localtime()) + "_temp.txt"

    # Set up bash command to run phmmer homology query:
    bash_cmd = f"phmmer -o {temp_file_path2} {query_seq_path} {db_path}"
    subprocess.run(
        bash_cmd.split(sep=" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    # Read the fasta of the sequence of greatest homology from results:
    hit_header = parse_phmmer_output(result_path=temp_file_path2)

    if hit_header is not None:
        # Extract sequence of best hit from fasta using hit_header:
        db_list = j.utils.seq_list_from_fasta(db_path, j.sequence.AASeq)
        db_dict = {
            seq.label: seq for seq in db_list
        }  # Quickly set up dictionary to access seq from its header
        hit_seq = db_dict[hit_header]

        # Delete phmmer results file:
        os.remove(temp_file_path2)
        return hit_seq
    else:
        return None


if __name__ == "__main__":
    # Check for phmmer install:
    try:
        test_cmd = "phmmer".split(" ")
        subprocess.run(test_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise HmmerNotInstalledError

    # Read the query sequence from file as jinfo AASeq object:
    labels = []
    hits = []

    # Loop over all gbk records in directory:
    for file_name in os.listdir(GBK_PATH):

        # Generate temporary file name and convert GBK to fasta:
        temp_file_path = time.strftime("%H_%M_%S", time.localtime()) + "_temp.fasta"
        gbk2fasta(os.path.join(GBK_PATH, file_name), temp_file_path)

        # Call phmmer using wrapper function:
        hit = phmmer_wrapper(db_path=temp_file_path, query_seq_path=QUERY_SEQ_PATH)
        if hit is not None:
            hits.append(hit)
            labels.append(file_name[:-4])

        # Delete fasta seq db:
        os.remove(temp_file_path)

    # Convert list of hits and labels to fasta output:
    j.utils.seq_list_to_fasta(seq_list=hits, file_name=HOMOLOGS_PATH, label_list=labels)
