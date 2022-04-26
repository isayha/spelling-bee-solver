'''
Project Name: Spelling Bee Solver
Project Description: This relatively lightweight program will take a .txt file of English words and 
                     the criteria of a round of the New York Times' Spelling Bee and both print and
                     output a file containing a subset of English words that meet said criteria.
                     The New York Times' Spelling Bee can be found at the following URL:
                     https://www.nytimes.com/puzzles/spelling-bee
Project Author: Isayha Raposo
'''

from sys import argv, exit
from os import path

def process_data_file(data_file_name, opt_chars, mand_char):
    opt_chars.append(mand_char)

    words = []
    data_file = open(data_file_name, 'r')
    current_word = data_file.readline().strip().upper()
    while(current_word):
        if (len(current_word) > 3) and (mand_char in current_word) and all([char in opt_chars for char in current_word]):
            words.append(current_word)
        current_word = data_file.readline().strip().upper()
    return words

def print_and_write(output_file, string):
    print(string)
    output_file.write(string + '\n')

def main():
    arg_count = len(argv)
    if arg_count < 2:
        print("ERROR: No command line argument provided. See README.md.")
        exit(1)

    data_file_name = argv[1]
    if not path.isfile(data_file_name):
        print("ERROR: Specified data file " + data_file_name + " not found. See README.md.")
        exit(1)

    print("Enter optional characters (comma-delimited): ")
    opt_chars = input().upper().strip().split(',')
    print("Enter mandatory characters (comma-delimited): ")
    mand_char = input().upper().strip()

    words = process_data_file(data_file_name, opt_chars.copy(), mand_char)

    output_file = open("spelling_bee_words.txt", "w")
    print_and_write(output_file, "Optional characters:" + str(opt_chars) + "\nMandatory character: " + str(mand_char))
    for current_word in words:
        print_and_write(output_file, current_word)
    output_file.close()

if __name__ == "__main__":
    main()