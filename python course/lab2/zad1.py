#zad1
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        print("Number of bytes: ",statinfo.st_size)


def words(fname):
        count=0
        file = open(fname)
        wordcount = {}
        for word in file.read().split():
                count+=1
                if word not in wordcount:
                        wordcount[word] = 1
                else:
                        wordcount[word] += 1

        file.close();

        print("Number of different words:", len(wordcount))
        print("Number of words:", count)



def line_length(line):
        counter=0
        for x in range (0,len(line)-1):
                counter+=1
        return counter


def lines(fname):
        max_line_length=0
        count = 0
        with open(fname) as f:
                for line in f:
                        count += 1
                        if line_length(line)>= max_line_length:
                                max_line_length=line_length(line)

        print("max line length : ", max_line_length)
        print("Total number of lines is:", count)

file_size("test.txt")
words("test.txt")
lines("test.txt")


