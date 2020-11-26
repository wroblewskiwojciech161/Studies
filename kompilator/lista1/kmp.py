#Wojciech Wroblewski

#kmp pattern matcher

class KMP:

    def __init__(self, text, pattern):
        self.text  = self.to_dict(text)
        self.pattern = self.to_dict(pattern)
        self.pattern_len = len(self.pattern)
        self.text_len = len(self.text)
        self.pi = self.compute_prefix()


    #conv to dictionary
    def to_dict(self,string):

        dict={}
        idx = 1

        for i in range(0,len(string)):

            dict[i+1] = string[i]

        return dict

    #kmp
    def kmp(self):

        q = 0

        for i in range(1, self.text_len + 1):

            while q > 0 and self.pattern[q + 1] != self.text[i]:  

                q = self.pi[q]

            if self.pattern[q + 1] == self.text[i]:

                q += 1

            if q == self.pattern_len:

                print('index wystapienia : ', i - self.pattern_len)
                q = self.pi[q]


    # compute prefix function
    def compute_prefix(self):
        
        pi = { 1: 0}
        k = 0

        for q in range(2, self.pattern_len + 1):

            while k > 0 and self.pattern[k + 1] != self.pattern[q]:

                k = pi[k]

            if self.pattern[k + 1] == self.pattern[q]:
                k += 1

            pi[q] = k

        return pi

    
