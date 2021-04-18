from Bio import Entrez, SeqIO
import pandas as pd
import sys

email = 'kylebascomb@gmail.com'     # should be moved to an environment variable or argument

def get_seq(id, email = email):
    '''This function calls the Entrez efetch function to get the FASTA 
        sequence related to the id.

        Parameters:
            id (str): id of the protein sequence
            email (email) : user email necessary for Entrez usage
        Returns:
            returns a SeqIO seq record of the FASTA sequence
    '''
    Entrez.email = email
    try:
        request = Entrez.efetch(db="protein", id=id, rettype="fasta")
        seq_record = SeqIO.read(request, "fasta")
        return seq_record
    except Exception as e:
        print("ERROR: Protein ID not found:", id)
        print("Error Message:", e)

    return None


if __name__ == '__main__':
    argument_list = sys.argv[1:]
    infile = ''
    outfile = ''
    # parse sys arguments
    for i in range(len(argument_list)):
        if argument_list[i].find('-') == 0:
            if argument_list[i][1:] == 'in' and argument_list[i+1].find('-') != 0:
                infile = argument_list[i+1]
            elif argument_list[i][1:] == 'out' and argument_list[i+1].find('-') != 0:
                outfile = argument_list[i+1]

    # load csv file
    df = pd.read_csv(infile)

    # Iterate over each id in df and call get_seq
    print("Expecting:", len(df.index), "Sequences")
    seq_list = []
    for index, row in df.iterrows():
        seq_rec = get_seq(row['id'])
        if seq_rec is not None: 
            seq_list.append(seq_rec)

    # write sequences to outfile
    with open(outfile, '+a') as output_handle:
        SeqIO.write(seq_list, output_handle, 'fasta')
    print("Received: ", len(seq_list), "Sequences")
    print("Write to file complete")