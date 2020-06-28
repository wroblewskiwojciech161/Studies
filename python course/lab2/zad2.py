#zad2
import sys
def decimal_to_bin(num):
    num=bin(num)
    num=str(num)
    num=num[2:]
    size=len(num)
    return  (8-size)*'0' +num
def split_into_nbit(string,n):
    # Defining splitting point

    # Using list comprehension
    out = [(string[i:i + n]) for i in range(0, len(string), n)]

    return out
    # Printing output
   # print(out)

def to_string(s):
   new=""
   for x in s:
       new=new + x

   return new

def convert(input):
    tab_base64_transform = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    tab_asci=[]
    tab_bin=[]
    tab_bin_6=[]
    for i in range (0,len(input)):
        tab_asci.append(ord(input[i]))
    #print(tab_asci)
    for a in range(0,len(tab_asci)):
        tab_bin.append(decimal_to_bin(tab_asci[a]))
    #print(tab_bin)
    tab_bin=to_string(tab_bin)
    tab_bin_6=split_into_nbit(tab_bin,6)
    final=[]
    #print(tab_bin_6)
    for i in range (0,len(tab_bin_6)):
        final.append(int(tab_bin_6[i],2))
    #print(final)
    for i in range (0,len(final)):
        final[i]=tab_base64_transform[final[i]]
    return final

def de_convert(input):
    tab_base64_transform = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    numbers=[]
    tab_bin_6=[]
    for i in range (0,len(input)):
        numbers.append(tab_base64_transform.index(input[i]))
    #print(numbers)
    for i in range (0,len(numbers)):
        bin=decimal_to_bin(numbers[i])
        tab_bin_6.append(bin[2:])
    #print(tab_bin_6)
    tab_bin_6=to_string(tab_bin_6)
    #print(tab_bin_6)
    tab_bin_8=split_into_nbit(tab_bin_6,8)
    #print(tab_bin_8)
    final=[]
    for i in range (0,len(tab_bin_8)):
        final.append(int(tab_bin_8[i],2))
   # print(final)
    for i in range (0, len(final)):
        final[i]=chr(final[i])
    return final
print(convert("Python"))

#convert("Python")
#print("------------------------------------------")
#de_convert("UHl0aG9u")

if sys.argv[1] == "--encode":
    print(sys.argv[2])
    file = open(sys.argv[2], "r")
    string = file.read()
    #nie do konca bo wsawia nowa linie
    string=string[0:-1]
    print(string.split(" "))
   # print(string)


    text_file = open(sys.argv[3], "w")
    output=""
    for i in range (0,len(convert(string))):
        output=output +""+convert(string)[i]
    print("output ",output)
    n = text_file.write(output)
    text_file.close()

    #convert("temp")
elif sys.argv[1] == "--decode":
    #print(sys.argv[2])
    file = open(sys.argv[2], "r")
    string = file.read()
    print(string)

    text_file = open(sys.argv[3], "w")
    output = ""
    for i in range(0, len(de_convert(string))):
        output = output + "" + de_convert(string)[i]

    n = text_file.write(output)
    text_file.close()
    print(output)

else:
    print("wrong syntax")

