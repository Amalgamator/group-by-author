import os
import sys

rootdir = '/path_to_txt_files/'

def averageLen(words):
    lengths = [len(i) for i in words]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths))

i = 0
for file in os.listdir(rootdir):
    # txt files need to be named in the format {author - title.txt}
    ext = str(file).split("-",1)
    exte = len(ext)
    if ".txt" in ext[exte-1]:
        i += 1
        author = ext[0].lower()
        author = author.replace(" ","")
        
        print(i, author)
        
        if len(author) >= 5: # clears serials and shorts with no explicit author in the name
            try:
                fileObj = open(file,'r')
                file_text = fileObj.read()
                fileObj.close()
                
                words = file_text.split(" ")
                avgwordlen = averageLen(words)
                
                # Is the text proper prose? calculation:
                # avg english wordlength (5.1) plusmin 1*stdev
                # stdev taken from 9,000 txt files with a ~110,000 word average (3.9gb total)
                if 4.24828962123251 <= avgwordlen <= 5.95171037876749:
                    # print(int(i), str(file))
                    authorfile = open("/path_to_the_output_directory/"+str(author)+".txt", 'a')
                    authorfile.write(file_text+"\n"+"\n")
                    authorfile.close()
                else:
                    # you can add rules here
                    error_log = open("--Files_to_review.TXT", 'a')
                    error_log.write(str(file)+'\n')
                    error_log.close()
                    print("Review anomalous file: ",file)
            except:
                error_log = open("-AUTHOR-ERRORS.TXT", 'a')
                error_log.write(str(file) + '\n' + str(sys.exc_info()) + '\n')
                error_log.close()
        else:
            continue
