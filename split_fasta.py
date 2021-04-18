import sys
import random
from fastaio import read_fasta
from fastaio import write_fasta


def train_test_split(fasta_list, test_percent):
    '''
    This function shuffles a list and splits it according to the test percentage

    Parameters: 
    fasta_list (list)-- list to be shuffled
    test_percent (float)-- percentage of the original list that will be in the test set

    Returns:
    Training list and a testing list
    '''
    random.shuffle(fasta_list)
    test_target = int(len(fasta_list) * float(test_percent))
    test = fasta_list[:test_target]
    train = fasta_list[test_target:]
    
    return train,test



if __name__ == '__main__':
    #Variables
    argument_list = sys.argv[1:]
    infile = ''
    outfile = ''
    test_percent = 0.0

    # Read Arguments
    for i in range(len(argument_list)):
        if argument_list[i].find('-') == 0:
            if argument_list[i][1:] == 'in' and argument_list[i+1].find('-') == -1:
                infile = argument_list[i+1]
            elif argument_list[i][1:] == 'out' and argument_list[i+1].find('-') == -1:
                outfile = argument_list[i+1]
            elif argument_list[i][1:] == 'split' and argument_list[i+1].find('-') == -1:
                test_percent = argument_list[i+1]




    train,test = train_test_split(read_fasta(infile), test_percent)
    print(str(len(train)) + ' Sequences for training')
    print(str(len(test)) + ' Sequences for testing')
    train_label = infile[:-6] + '_train.fasta'
    test_label = infile[:-6] + '_test.fasta'
    write_fasta(train, train_label)
    write_fasta(test, test_label)
    print("Done")

            