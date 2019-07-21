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
