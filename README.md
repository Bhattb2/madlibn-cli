# Madlib
### Link to Latest PR:
https://github.com/Bhattb2/madlibn-cli/pull/5

## Description
- Print a welcome message to the user, explaining the Madlib process and command line interactions
- Read a template Madlib file (Example), and parse that file into usable parts.
- You need to decide what components of this file are useful, and how to break those useful pieces apart
- Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
- With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
- After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
- Write the completed template (Example)to a new file on your file system (in the repo).
## Usage
The programs prompts the user to enter 21 different words. These words are appended to a list 'words'. The the function def read_template() opens the template.txt file and reads it. The system will loop through each character and if it will look for any words surrounded by the curly braces { }. It will then replace the word with a word from the words array. If the program encounters an error opening a file, it will create a new error_log file in the assests folder with a description of the error.