from Bio import SeqIO
from Bio.Data.CodonTable import TranslationError
from Bio.SeqRecord import SeqRecord
import argparse
import tqdm


def fna_2_faa(fna_filepath: str, faa_filepath: str):
    skipped = 0
    with open(faa_filepath, 'w') as aa_fa:
        for dna_record in tqdm.tqdm(SeqIO.parse(fna_filepath, 'fasta'),  desc='reqding faa', unit='lines'):
            # generate all translation frames
            try:
                aa_seqs = dna_record.seq.translate(cds=True, table=11, stop_symbol="")
            except TranslationError:
                try:
                    aa_seqs = dna_record.seq.translate(cds=True, table=4, stop_symbol="")
                except:
                    skipped += 1
                    continue
            except:
                print("funny!")

            # write new record
            aa_record = SeqRecord(aa_seqs, id=dna_record.id, description="")

            SeqIO.write(aa_record, aa_fa, 'fasta')
    print(skipped)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('fna', type=str)
    parser.add_argument('faa', type=str)
    args = parser.parse_args()
    fna_2_faa(args.fna, args.faa)
