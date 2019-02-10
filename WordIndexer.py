#!/usr/bin/python
#==============================================================================
# title           : WordIndexer.py
# description     : Used for generating word indexes.
# author          : Rahul Anand Akkina
# email           : rahul.akkina@gmail.com
# date            : 20190210
# version         : 0.1
#==============================================================================

import os
import re
import sys
import logging
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet


''' WordIndexer - Extracts the file and generates the index file.'''
class WordIndexer(object):

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    #Input file
    input_file = ''

    # Datastructure to build the word index.
    word_index_lkup = SortedDict()

    #Regular Expression for delimiting words in a given sentence.
    sentence_pattern = re.compile('[\s\t\r\n,;?!{}()"\'\[\]\./]+')


    ''' Initializes the class.'''
    def __init__(self, file = sys.argv[1]):
        self.new()

    '''Method that resets the existing index and adds a new file for extraction'''
    def new(self, input_file=sys.argv[1]):
        self.word_index_lkup.clear()
        self.add(input_file)

        return self

    '''Adds a new file for extraction and checks for the file.'''
    def add(self, input_file):
        if not os.path.isfile(input_file):
            logging.error("File '%s' does not exist. Exiting ..." % (input_file))
            sys.exit()

        self.input_file = input_file

        return self

    ''' Extracts the input file and builds the index data-structure'''
    def extract(self):

        logging.info("Extracting from file '%s' ..."%(self.input_file))

        with open(self.input_file) as fp:
            line_number = 0
            for line in fp:
                line_number += 1
                self.__add_to_index(line, line_number)

        logging.info("Extracted %d words from file '%s' with %d lines." % (len(self.word_index_lkup), self.input_file, line_number))

        return self

    '''Performs word extraction and arranges them appropriately (as per requirement'''
    def __add_to_index(self, line, line_number):
        for word in self.sentence_pattern.split(line):
            if word:
                lc_word = word.lower()

                if lc_word not in self.word_index_lkup:
                    self.word_index_lkup[lc_word] = SortedSet()

                self.word_index_lkup[lc_word].add(line_number)

    ''' Generates file-index.* file'''
    def generate(self):
        file_delimited = self.input_file.split('.')
        index_filepath = "%s%s.%s" %(file_delimited[0], "-index",  file_delimited[1])

        logging.info("Generating file '%s' ...... " % (index_filepath))

        with open(index_filepath, 'w') as index_file:
            for key, value in self.word_index_lkup.items():
                index_file.write("%s %s %s" %(key, ",".join(map(str, value)), "\n"))
            index_file.flush()

        logging.info("Generated file '%s' with %d words." %(index_filepath, len(self.word_index_lkup)))

        return self



#Main Section
if __name__ == '__main__':
    WordIndexer().extract().generate()


