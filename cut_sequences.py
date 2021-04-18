import sys
from fastaio import read_fasta
from fastaio import write_fasta



def get_src_seqs(src_list, ref_list):
    '''This function saves the ID's of the reference list and
    cross references these ID's against he src list. 

    Parameters: 
        src_list (list) : Source list of FASTA sequences with headers
        ref_list(list) : Ref list of FASTA sequences with headers

    Returns:
        out_list (list) : new list of all the sequences in the src list that match the ones
    on the reference list

    '''
    accession_set = set()
    out_list = []
    for fasta in ref_list:
        header = fasta[0]
        accession = header[1:].split(' ')[0]
        accession = accession.strip()
        accession_set.add(accession)

    for fasta in src_list:
        header = fasta[0]
        accession = header[1:].split(' ')[0]
        accession = accession.strip()
        if accession in accession_set:
            out_list.append(fasta)
            print('Appending: ' + accession)
    
    return out_list




if __name__ == '__main__':
    argument_list = sys.argv[1:]
    srcfile = ''
    reffile = ''
    outfile = ''
    start = 0
    length = 0
    #parse arguments
    for i in range(len(argument_list)):
        if argument_list[i].find('-') == 0:
            if argument_list[i][1:] == 'src' and argument_list[i+1].find('-') == -1:
                srcfile = argument_list[i+1]
            elif argument_list[i][1:] == 'out' and argument_list[i+1].find('-') == -1:
                outfile = argument_list[i+1]
            elif argument_list[i][1:] == 'ref' and argument_list[i+1].find('-') == -1:
                reffile = argument_list[i+1]

    src_list = read_fasta(srcfile)
    ref_list = read_fasta(reffile)

    out_list = get_src_seqs(src_list, ref_list)
    write_fasta(out_list, outfile)
    print('Write to file complete')

