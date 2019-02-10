# word-indexer
There is a given input text file (ASCII). Please create an application, that makes a new file ending with -"index.txt". To the index write every word in a new line, in alphabetical order, that occurs in the textfile. After each word please display in which line in the original textfile did the word appear. Separate the numbers with commas. 


# How do i run ?

Requirements:

We would need Python 3 to be installed on the machine, also need to install module 'sortedcontainers' (Use command 'pip install sortedcontainers' to install) 

In order to run the main use the below command.

python WordIndexer.py <input-file.txt>

The above action creates an output file in the format <input-file-index.txt>

eg :  Run the below command

python WordIndexer.py files/god-sees-truth-but-waits.txt

It generates an output file with the name 'files/god-sees-truth-but-waits-index.txt'

