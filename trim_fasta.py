import sys
from fastaio import read_fasta
from fastaio import write_fasta


LINE_LENGTH = 60


def trim_fasta(fasta_list, start, length):
    '''Trims a list of FASTA sequences from index start:start_length

    Parameters:
        fasta_list : list of fasta sequences
        start : index of the start of the trim
        length: length of the trim

    Returns:
        new_list : trimmed list of fasta sequences
    '''
    new_list = []
    for fasta in fasta_list:
        header = fasta[0]
        seq = ''.join([str(line) for line in fasta[1:]])
        seq_formatted = seq.replace('\n', '')
        trimmed_seq = seq_formatted[start:start+length]
        final_seq = '\n'.join(trimmed_seq[i: i+LINE_LENGTH] for i in range(0, len(trimmed_seq), LINE_LENGTH))
        final_seq += '\n'
        new_fasta = [header, final_seq]
        new_list.append(new_fasta)
    return new_list


if __name__ == '__main__':
    argument_list = sys.argv[1:]
    infile = ''
    outfile = ''
    start = 0
    length = 0
    for i in range(len(argument_list)):
        if argument_list[i].find('-') == 0:
            if argument_list[i][1:] == 'in' and argument_list[i+1].find('-') == -1:
                infile = argument_list[i+1]
            elif argument_list[i][1:] == 'out' and argument_list[i+1].find('-') == -1:
                outfile = argument_list[i+1]
            elif argument_list[i][1:] == 'start' and argument_list[i+1].find('-') == -1:
                start = int(argument_list[i+1])
            elif (argument_list[i][1:] == 'len' or argument_list[i][1:] == 'length') and argument_list[i+1].find('-') == -1:
                length = int(argument_list[i+1]) 



    in_list = read_fasta(infile)
    out_list = trim_fasta(in_list, start, length)
    write_fasta(out_list, outfile)
    print("Succesfully Trimmed Sequences")
