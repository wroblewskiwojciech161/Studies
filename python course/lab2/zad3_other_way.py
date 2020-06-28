import os
#os.rename(r'C:\Users\Ron\Desktop\Test\Products.txt',r'C:\Users\Ron\Desktop\Test\Shipped Products.txt')

path = "/home/sparrovsky/Desktop/test_folder/"

def merge(tab1,tab2):
    for i in range (0,len(tab1)):
       tab1[i]=str(tab1[i])+str(tab2[i]).lower()


fname_old=[]
fname_root = []
fname_file=[]
dname_root = []
dname_dir=[]
dname_old=[]


for root, dirs, files in os.walk(path):
    for name in dirs:
        dname_old.append(os.path.join(root,name))
        dname_root.append(os.path.join(root))
        dname_dir.append(os.path.join(name))
#fname_root = list(dict.fromkeys(fname_root))
#fname_file=list(dict.fromkeys(fname_file))
#dname_root = list(dict.fromkeys(dname_root))
#dname_dir=list(dict.fromkeys(dname_dir))


merge(dname_root,dname_dir)

for i in range(0, len(dname_old)):
    os.rename(dname_old[len(dname_old)-i-1], dname_root[len(dname_old)-i-1])
"""
for root,d_names,f_names in os.walk(path):
    for f in f_names:
        fname_old.append(os.path.join(root,f))
        fname_root.append(os.path.join(root))
        fname_file.append(os.path.join(f))

merge(fname_root,fname_file)
for i in range(0, len(fname_old)):
    os.rename(fname_old[len(fname_old)-i-1], fname_root[len(fname_old)-i-1])"""
