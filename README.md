# word-indexer
There is a given input text file (ASCII). Please create an application, that makes a new file ending with -"index.txt". To the index write every word in a new line, in alphabetical order, that occurs in the textfile. After each word please display in which line in the original textfile did the word appear. Separate the numbers with commas. 

**Requirements:**

 We would need Python 3 to be installed on the machine, also need to install module **sortedcontainers** (Use command `pip install sortedcontainers` to install)
 
**Approach** 

  We shall create a datastructure `SortedDictionary of SortedSets`, parse the given file with assumed delimiters [\s\t\r\n,;?!{}()"\'\[\]\./]+ (Space, Period, Tab, newline, Comma, Question Mark, Exclamation, Flower Braces, Braces, Square Braces, \, Single & Double Quotes) we shall extracts word line-by-line and build the datastructure. Once a single parse is completed we shall export the datastrcture into discussed format. 

**How do i run ?**


In order to run the main usecase the below command.

`python WordIndexer.py <input-file.txt>`

The above action creates an output file in the format <input-file-index.txt>

eg :  Run the below command

`python WordIndexer.py files/god-sees-truth-but-waits.txt`

It generates an output file with the name `files/god-sees-truth-but-waits-index.txt`

In order to run the unit tests please run the below command 

`python -m unittest WordIndexerTest`



