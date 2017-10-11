# group-by-author
  - Groups txt files by author, based on an input file naming format of { Author - File.txt } (not necessarily capitalized)
  - Selects only files that have proper prose: txt-files are considered as having proper prose when the average word length does not deviate too much from the average English word length of 5.1.
  - Spits out one file per author and all the files end up in one directory.
