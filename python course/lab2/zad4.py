
import os
import hashlib
import collections
import sys
#path="/home/sparrovsky/Desktop/test_folder/"
path=sys.argv[1]

def same_arrays(tab1,tab2):
    if set(tab1) == set(tab2):
        return True
    else:
        return False

def check_if_subtable(table,subtable):
    for i in range(0,len(table)):
        if same_arrays(subtable,table[i]):
            return True
    return False


fname = []
for root,d_names,f_names in os.walk(path):
	for f in f_names:
		fname.append(os.path.join(root, f))

print("----------------------------------------------------")
print("----------------------------------------------------")
main=[]
for name in fname:
    temp = [x for i,x in enumerate(fname) if i!=fname.index(name)]
    store = []
    inputFile = name
    openedFile = open(inputFile)
    readFile = openedFile.read()
    for i in range (0,len(temp)):

        inputFile2 = temp[i]
        openedFile2 = open(inputFile2)
        readFile2 = openedFile2.read()
        if hashlib.md5(readFile2.encode()).hexdigest() == hashlib.md5(readFile.encode()).hexdigest() and os.path.getsize(inputFile)==os.path.getsize(inputFile2):
            if inputFile2 not in store:
                store.append(inputFile2)
            if inputFile not in store:
                store.append(inputFile)
    if len(store)!=0 and check_if_subtable(main,store)==False:
        main.append(store)


for x in main :
    for i in range(0,len(x)):
        print( x[i], sep='\n')
    print("----------------------------------------------------")
    print("----------------------------------------------------")

