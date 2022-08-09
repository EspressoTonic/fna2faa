from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def fna_2_faa(fna_filepath: str, faa_filepath: str):
    with open(faa_filepath, 'w') as aa_fa:
        for dna_record in SeqIO.parse(fna_filepath, 'fasta'):
            # generate all translation frames
            aa_seqs = dna_record.seq.translate(cds=True, stop_symbol="")

            # write new record
            aa_record = SeqRecord(aa_seqs, id=dna_record.id, description="")

            SeqIO.write(aa_record, aa_fa, 'fasta')
