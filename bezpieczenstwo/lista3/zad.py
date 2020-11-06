
#lista 3 bezpieczenstwo

import ast

message = "00011100 10001101 10111011 11000101 11000001 10101101 10101011 00100101 01111001 00001101 11111011 11111101 00010010 01011000 10011111 00011000 11001110 00001001 10111000 00001101 11101010 11010111 10100011 11000000 11010001 10100111 10001110 11010000 10100110 01011101 10010110 11110100 11001111 01111000 11101010 00001010 01111111 00111001 01010100 01111000 00011001 01000100 10111110 00110111 01110100 11101000 11111011 10000000 01110110 01000101 00000001 01110111 01010011 01100001 10001110 01110011 10111000 01101110 11101010 10011000 10101010 11000100 00011110 01001000 01100100 11100110 10010101 10010100 10010101 00010100 00111110 01110011 11011110 01001000 10101110 01000111 "



class Decryptor:
    def __init__(self,limit):

        self.messages = [message.split()]
        self.cryptograms = get_cryptograms(limit,1)
        self.MAX = get_max_length(self.cryptograms)
        self.key = []
        self.guess_letter_storage = get_letters()

    def message_decription(self):

        for i in range(0, self.MAX):

            partial_candidates = {}

            matching_cryptograms = [c for c in self.cryptograms if len(get_cryptogram_chars(c)) > i]

            for c in matching_cryptograms:
                
                #n-th char of given c cryptogram
                char = get_cryptogram_chars(c)[i]
        
                # xor  n-th char of c  with  freq-dict
                for letter_key, freq in self.guess_letter_storage.items():

                    # after xoring we should get n-th key element
                    candidate = (ord(char) ^ (ord(letter_key)), freq)

                    #print(c_chars[n] ,"   ",letter,"  ",tmp)

                    if candidate[0] not in partial_candidates.keys():
                        partial_candidates[candidate[0]] = freq

                    #such xor output appeared so incerment freq of n-th key candidate
                    else:
                        partial_candidates[candidate[0]] = partial_candidates.get(candidate[0]) + freq

            # add nth best candidate
            self.key.append(get_best_nth_candidate(partial_candidates))

        get_message(self.cryptograms,self.key)

        print("--------------------------------")
        print("TO ENCODED")
        print("--------------------------------")
        get_message(self.messages,self.key)


def get_letters():
    file = open("alphabet.txt", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary

def conv_bin_to_hex(string):

    return str(hex(int(string,2)))


def get_cryptograms(limit,percentage):
    ceps = []
    with open('crypto.txt', 'r') as file:
            for line in file.readlines():
                if len(line) > 1:
                    temp = []
                    upper_bound = int(percentage*len(line.split()))
                    if upper_bound % 2 != 0:
                        upper_bound -=1
                    for i in range(upper_bound):
                        temp.append(line.split()[i])
                    
                    ceps.append(temp)
    file.close()
    return ceps[:limit]

def get_cryptogram_chars(cryptogram):
    out = []
    for e in cryptogram:
        out.append(chr(int(conv_bin_to_hex(e),16)))
    
    return out

def get_cryptogram_decimals(cryptogram):
    out = []
    for e in cryptogram:
        out.append(int(conv_bin_to_hex(e),16))
    
    return out

def get_max_length(cryptograms):
    max = 0
    for c in cryptograms:
        if len(get_cryptogram_chars(c)) > max:
            max = len(get_cryptogram_chars(c))
    return max


def get_best_nth_candidate(dictionary):

    temp = dict(sorted((value, key) for (key,value) in dictionary.items()))
    return temp.popitem()[1]
        
def get_message(cryptograms , key):
    for c in cryptograms:
        msg = ""
        for i, char in enumerate(get_cryptogram_chars(c)):
            msg += chr(ord(char) ^ key[i])
        print(msg)



d = Decryptor(20)
d.message_decription()

