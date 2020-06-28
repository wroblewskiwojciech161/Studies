#zad 5
#RSA
from random import randrange,getrandbits
import sys
const=1
def get_new_ascii_number(char):
    asciiDict = {i*const : chr(i) for i in range(129)}
    j = 0
    index=j*const

    while asciiDict[index] != char:
        j += 1
        index=j*const

    return index
def get_new_ascii_char(num):
    asciiDict = {i*const: chr(i) for i in range(129)}

    return asciiDict[num]


def gcdExtended(a, b, x, y):

    if a == 0:
        x = 0
        y = 1
        return b

    x1 = 1
    y1 = 1
    gcd = gcdExtended(b % a, a, x1, y1)


    x = y1 - (b / a) * x1
    y = x1

    return gcd

def multinv(modulus, value):
    #modulo inverse

    x, lastx = 0, 1
    a, b = modulus, value
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x
    result = (1 - lastx * modulus) // value
    return result + modulus if result < 0 else result

def is_prime(n, k):
    #  test if n prime k times
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):

    # generate random bits
    p = getrandbits(length)
    return p
def generate_prime_number(length):

    p = 4

    while not is_prime(p,length):
        p = generate_prime_candidate(length)
    return p


def size(number):
    k=0
    number=str(number)
    for x in number:
        k+=1
    return k

def public_key(p1,p2):
    phi=(p1-1)*(p2-1)
    #print("phi: ",phi)
    n=p1*p2
    #public(e,n)
    e=3
    while gcdExtended(phi,e,1,1)!=1 :
        e+=2
    tab = []
    tab.append(e)
    tab.append(n)
    return tab

def private_key(p1,p2):
    phi = (p1 - 1) * (p2 - 1)
    n = p1 * p2
    e = 3
    while gcdExtended(phi, e, 1, 1) != 1:
        e += 2
    d = multinv(phi, e)
    tab=[]
    tab.append(d)
    tab.append(n)
    return tab
def code_rsa(input,public_key):
    e=int(public_key[0])
    n=int(public_key[1])
    output=[]
    for i in range (0,len(input)):
        output.append(get_new_ascii_number(input[i]))
    for i in range (0, len(input)):
        #output[i]=exponentiation(output[i],e,n)
        output[i]=pow(output[i],e,n)

    return output
def decode_rsa(input,private_key):
    d=int(private_key[0])
    n=int(private_key[1])
   # print("d : " ,d)
   # print ("n : ", n)
    output=[]
    for i in range (0,len(input)):
        #output.append(exponentiation(input[i],d,n))
        output.append(pow(int(input[i]), d, n))


    for i in range (0,len(input)):
        output[i]=get_new_ascii_char(output[i])
    return output

def split_into_table(tab):
    output=[]
    temp=""
    for i in range (0,len(tab)):
        temp=temp+ str(tab[i])
    for i in range (0,len(temp)):
        output.append(temp[i])
    return output


if sys.argv[1]=='--encrypt':
    string = sys.argv[2]
    public=[]
    file =open("key_pub.txt","r")
    e=file.readlines(1)[0]
    n=file.readlines()[0]
  #  print(e)
   # print(n)
    public.append(int(e))
    public.append(int(n))
    print("coded: ")
    for i in range(0,len(code_rsa(string,public))):
        print(code_rsa(string,public)[i],end=" ")
    print("\n")

elif sys.argv[1]=='--decrypt':

    string = sys.argv[2::]

    #print(string)
    private = []
    file = open("key_priv.txt", "r")
    d = file.readlines(1)[0]
    n = file.readlines()[0]

    private.append(int(d))
    private.append(int(n)) 
    print("encoded: ")
    for i in range (0,len(decode_rsa(string, private))):
        print(decode_rsa(string, private)[i], end="")
    print("\n")


elif sys.argv[1]=='--gen-keys':
    p1 = generate_prime_number(int(sys.argv[2]))
    p2 = generate_prime_number(int(sys.argv[2]))
    public = public_key(p1, p2)
    private = private_key(p1, p2)
    text_file = open("key_pub.txt", "w")
    for i in range(0, len(public)):
        n = text_file.write(str(public[i]))
        n=text_file.write("\n")
    text_file.close()
    text_file2 = open("key_priv.txt", "w")
    for i in range (0,len(private)):
        n = text_file2.write(str(private[i]))
        n=text_file2.write("\n")
    text_file2.close()