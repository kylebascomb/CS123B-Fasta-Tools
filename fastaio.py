

def read_fasta(filename):
    '''This function reads the input file and parses it as a FASTA File
        Returns a list of lists. 
        The outer list represents one FASTA sequences.
        The inner lists represent each line of the FASTA sequence
    
    '''
    reader = open(filename)
    fasta_list = []
    try:
        lines = reader.readlines()
        fasta = []
        for i in range(len(lines)):
            if lines[i].find('>') == 0 and i != 0:
                fasta_list.append(fasta)
                fasta = []
            fasta.append(lines[i])
        fasta_list.append(fasta)
    except:
        print("Error opening file. Exiting")
        exit()
    finally:
        reader.close()
    return fasta_list


def write_fasta(lines, label):
    '''Function writes a list of fastlines

    Parameters:
        lines (list) - lines to be written
        label (str) - path to write to

    '''
    with open(label, 'w') as writer:
        for line in lines:
            for string in line:
                writer.writelines(string)
