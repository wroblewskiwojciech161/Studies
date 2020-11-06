# v2 using space detection in Ascii
# note that xor(space,any char) >= 65 in ascii

def conv_to_dec(array1):
    output=[]
    for x in array1:
        output.append(int(ord(x)))
    return output


def make_cipher(array1,key):
    output = []
    for i in range(0,len(array1)-1):
        output.append(int(array1[i]) ^ int(key[i]))

    return output

def conv_to_char(array1):
    output = []
    for i in range(0,len(array1)-1):
        output.append(chr(int(array1[i])))

    return output




ciphers =[]
max = 0
iter = []
with open('crypto.txt', 'r') as file:
        for line in file.readlines():
            if len(line) > 0:
                line=line.split()
               
                out = []
                for element in line:
                    out.append(int(element,2))
                out = conv_to_char(out)
                if len(out)> max:
                    max = len(out)
             
                ciphers.append(out)


max_length = max
SPACE = ' '
key = bytearray(b'^' * max_length)
unknown_char = '^'

for k in range(max):

    #cipher -> len(cipher) >= k
	cts = [c for c in ciphers if len(c) > k] 

	#holds guess for current key char	
	guess = ord(unknown_char)
		
	for n in range(len(cts)):
		for m in range(len(cts)):
				
			if m == n:
					continue
			
			xor = ord(str(cts[n][k])) ^ ord(str(cts[m][k]))
				
			if 0 < xor < 65:
				guess = ord(unknown_char)
				break
 
			guess = SPACE
 
        #if space appears we can decrypt key for whole column
		if guess == SPACE: 
			key[k] = ord(cts[n][k]) ^ ord(SPACE)
			break
    
# cipher xor space (if appears) to encode msg
# msg cor cipher to encode key
for c in ciphers:
    c = conv_to_dec(c)
    c = make_cipher(c,key)
    c = conv_to_char(c)
    str = ""
    for element in c:
        str+=element
    print(str)
 