#zad3
import sys
import os
import getopt


def rename(srcpath):
    srcpath = os.path.normpath(srcpath)
    if os.path.isdir(srcpath):
        # zmien na male litery w dir
        newpath = name_to_lowercase(srcpath)
        # rekursja
        for entry in os.listdir(newpath):
            nextpath = os.path.join(newpath, entry)
            rename(nextpath)
    elif os.path.isfile(srcpath):
        name_to_lowercase(srcpath)
    else:
        print("zly argument : " + srcpath)
        sys.exit()

def name_to_lowercase(srcpath):
    srcdir, srcname = os.path.split(srcpath)
    newname = srcname.lower()
    if newname == srcname:
        return srcpath
    newpath = os.path.join(srcdir, newname)
    os.rename(srcpath, newpath)
    return newpath

path=sys.argv[1]
print(path)
rename(path)
