# Spelling Bee Solver

This relatively lightweight program will take a .txt file of English words and 
the criteria of a round of the New York Times' Spelling Bee and both print and
output a file containing a subset of English words that meet said criteria.
The New York Times' Spelling Bee can be found at the following URL:
https://www.nytimes.com/puzzles/spelling-bee

## Instructions

### How to run

- To run the program, simply run `spelling_bee_solver.py`, either using the command `python` on the command line (while in the same directory as the source files), or the IDE of your choice
	- This program was written in Python 3.8.6
- This program requires the provision of 1 (one) command line argument:
	- The command line argument should be the name of the desired input (text) file (including the `.txt` extension) containing (newline-delimited) English words to parse
    	- e.g.: `dictionary.txt`
		- The desired file should be placed in the root of this project
    		- If the file is placed in a project *subdirectory*, the file can *still* be specified via relative pathing
            	- e.g.: If you were to place `dictionary.txt` in a new subdirectory called `data`, `.\data\dictionary.txt` would be the correct argument to provide

- Failure to follow these instructions will result in the program writing a brief error message to console and immediately halting

### Results

- After (successfully) executing the program, it will:
	- Write the results to console
	- Output the results to `spelling_bee_words.txt`
		- The output (text) file is found in the project root
- Note that generating new results will overwrite any existing results
