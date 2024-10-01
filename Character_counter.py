##Letter counter
import argparse
import string
import re
import time

import numpy as np
import matplotlib.pyplot as plt
from loguru import logger

def dict_bar_plot(data, xtitle="xtitle", ytitle="ytitle", tit="title"):
    ''' Creates a bar plot from a dictionary of keys and occurrances

    Arguments
    ---------
    data : dict
            Keys as x-axis and values as occurrances
    '''
    objects = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot
    plt.bar(objects, values, color ='maroon',
        width = 0.4)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.title(tit)
    plt.show()


def process_file(file_path, countall, plot, stats):
    '''Unpacks a text file and counts the characters present

    Arguments
    ---------
    file_path : str
            Path to the input file
    '''
    #Read the file
    start = time.time()
    assert file_path.endswith('.txt'), "Please input a text file"
    logger.info(f'Opening input file {file_path}...')
    with open(file_path) as input_file:
        data = input_file.read()
    logger.info(f'Done reading, commencing the count...')

    #Makes the whole file lowercase
    data = data.lower()

    #Initialize a dictionary containing the lowercase letters and numbers
    chars = {}
    for char in (string.ascii_lowercase + '0123456789'):
        chars[char] = 0

    #Count the characters in the file (depends on countall)
    for char in data:
        if char in chars:
            chars[char] += 1
        else:
            if countall:
                chars[char] = 0
            else:
                pass
    logger.info(f'Done counting, found {len(chars)} different characters, {sum(chars.values())} total characters')
    end = time.time()
    logger.info(f'Time elapsed: {end-start:.2f}s')
    #Make the bar graph
    if plot:
        frequencies = {}
        for char in chars: frequencies[char]=chars[char]/sum(chars.values())
        logger.debug(f'Sum of the frequencies = {sum(frequencies.values())}')
        dict_bar_plot(frequencies, "Characters", "Frequencies", "Frequencies of the different characters")

    #Print out the basic stats
    if stats:
        linecount = data.count("\n")
        logger.info(f'Number of lines: {linecount}')
        wordcount = len(re.findall(r'\w+', data))
        logger.info(f'Number of words: {wordcount}')

parser = argparse.ArgumentParser(prog='Character counter',
    description='Count the letter frequency in a text')
parser.add_argument('infile', help='path to the input file')
parser.add_argument('--countall', action='store_true',
    help='Count all characters, not just the letters and numbers')
parser.add_argument('--plot', action='store_true', help="Plots a bar graph of the frequencies of the characters present")
parser.add_argument('--stats', action='store_true', help="Prints out the basic stats of the book")

if __name__ == '__main__':
    args = parser.parse_args()
    process_file(args.infile, args.countall, args.plot, args.stats)






