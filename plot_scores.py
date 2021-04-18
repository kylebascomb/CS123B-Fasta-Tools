import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def parse_scores(filename):
    '''This functions parses a tab separated value file
        and saves the columns labeled name, score, and seq in 
        a pandas dataframe

        Parameters:
        filename (str): name of the file to parse

        Returns:
        returns a pandas dataframe of the values in the file

    '''
    filepath = './' + filename
    data = pd.read_csv(filepath, sep='\t', header = None)
    data.columns=['name', 'score', 'seq']
    return data

def plot_scores(scores, colors_dict):
    ''' This function plots the scores and colors each point according to the colors_dict.
        The plot is made using matplotlib

    Parameters:
    scores (dataframe) : pandas dataframe that has a column of scores and a columns of classes
    colors_dict (dict) : dictionary linking each class to a color for plotting

    '''
    
    plt.title('Viterbi Scores')
    plt.scatter(scores['score'], np.zeros_like(scores['score']) + 1, s = 10, color=[colors_dict[i] for i in scores['class']])
    markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in colors_dict.values()]
    plt.legend(markers, colors_dict.keys(), numpoints = 1)
    plt.xlabel('Viterbi Scores')
    plt.yticks([])
    plt.show()


def write_dataframe(df, outfile):
    ''' This function writes a dataframe to a file as in csv format

    Parameters: 
    df (dataframe) : dataframe to write
    outfile (str) : path to output file

    '''
    try:
        df.to_csv(outfile)
        print('Output saved to:' + str(outfile))
    except:
        print("Error Saving File. Check file name")
        print("Exiting Now")


if __name__ == '__main__':
    argument_list = sys.argv[1:]
    infile = ''
    outfile = infile + '.out.csv'
    color_list = ['red', 'blue', 'green', 'purple', 'pink', 'orange', 'brown']
    current_color = 0
    color_dict = {}

    for i in range(len(argument_list)):
        if argument_list[i].find('-') == 0:
            if argument_list[i][1:] == 'in' and argument_list[i+1].find('-') != 0:
                infile = argument_list[i+1]
            elif argument_list[i][1:] == 'out' and argument_list[i+1].find('-') != 0:
                outfile = argument_list[i+1]   

    files = pd.read_csv(infile)
    scores = None

    # iterate over files to fill scores and color_dict
    for index, row in files.iterrows():
        filename = row['filename']
        if index != 0:
            file_data = parse_scores(filename)
            file_data['class'] = row['class']
            scores = scores.append(file_data, ignore_index = True)
        else:
            scores = parse_scores(filename)
            scores['class'] = row['class']
        if row['class'] not in color_dict:
            color_dict[row['class']] = color_list[current_color]
            current_color += 1

    #plot scores
    print('Close plot to save and exit')
    plot_scores(scores, color_dict)

    # save
    write_dataframe(scores, outfile)

