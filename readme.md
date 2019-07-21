# Eigen challenge

Exercise: find the most common occurring words in some given documents and the sentences where they are used to create the following table:

| Word(#) | Documents | Sentences containing the word |
|----------|----------------|--------|
| philosophy | x, y, z | I don't have time for philosophy. <br/> Surely this was a touch of fine philosophy; though no doubt he had never heard there was such a thing as that. <br/> Still, her pay-as-you-go philosophy implied she didn't take money for granted. |
| --- | --- | --- |

You have the flexibility to modify the final output display as per your wish. Idea behind it is to build a reusable solution which can be extended to other documents and text sources.

## Solution

### Data files
Data files are processed by specifying a list of directories. Each directory is checked (including any subfolders) and a list of valid files are compiled.

Valid file extensions are specified in file > extensions.py. While it currently only supports .txt files, this can be expanded to other file formats. To do so, implement a class for new file format (as shown in `Txt` class) with a method to read the file. If there is any data within the file, it must be put against `raw` attribute.

Two (incomplete) example file formats were put against extensions.py: `Pdf` and `Docx`. In order to make software useable with PDF and DOCX formats, implement `read` methods that will read the files and put the data against `raw` attribute.

Finally, any file extension class must be put against `VALID_EXTENSIONS` variable. The rest of the software uses this dictionary to figure out which file extensions are supported and can be processed.

### Most common words
Software compiles the list of most commonly used words within supported files. It excludes any 'stopwords' which are most common words in English language which appear regardless of the context. These are 'I, you, me', etc.

The list of stopwords were taken from https://gist.github.com/sebleier/554280#gistcomment-2838837 and was hardcoded in stopwords.json. If the file with stopwords is not present, it will attempt to use the standard list of stopwords from `nltk.corpus` library

### Output
Once it finds the list of most common words, it will export a `output.csv` file containing the following columns:
 - Word (#)
 - Frequency
 - Document
 - Sentence containing the word

'Word (#)' Represents one of the most common words appearing in files.
'Frequency' is the number of times the most common word was found across files.
'Document' is the location of the file it was referenced in.
'Sentence containing the word' is the sentence the most common word was mentioned within the 'Document'.

### Usage
First, relevant `nltk` packages must be installed. To do so, execute
`python main.py -i`
This should only be done once.

To find most common words used in files, run the software by passing in directory that contains relevant files. E.g. to process all files within `C:\Users\xxx\Desktop\test docs\` and `C:\Users\xxx\Documents` directories execute
`python main.py --PATHS "C:\Users\xxx\Desktop\test docs" "C:\Users\xxx\Documents"`

By default, it will export output.csv to desktop. To override output location, use `--OUTPUT` parameter. For example,
`python main.py --PATHS "C:\Users\xxx\Desktop\test docs" "C:\Users\xxx\Documents" --OUTPUT C:\Users\xxx\downloads`
would export output.csv to downloads folder instead.

Lastly, the software will look for 20 most common words by default. This can be changed using `--COUNT` parameter. Enter an integer which specifies the number of words to look for. For example,
`python main.py --PATHS "C:\Users\xxx\Desktop\test docs" "C:\Users\xxx\Documents" --OUTPUT C:\Users\xxx\downloads --COUNT 100`
would look 100 most common words instead.
