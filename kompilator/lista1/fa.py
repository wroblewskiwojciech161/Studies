# Wojciech Wroblewski 

#finite automata pattern matcher

class AUTOMATA:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.alphabet = ""
        self.pattern_len = len(self.pattern)
        self.text_len = len(self.text)

    #get alphabet from text
    def get_alphabet(self):

        alpha = ""
        for e in self.text:

            if e not in alpha :
                alpha += e

        self.alphabet = alpha


    
    # rcompute transition function
    def transition(self):

        transitions = {}

        for q in range(self.pattern_len + 1):
           
            for char in self.alphabet:
                k = min(self.pattern_len + 1, q + 2) - 1

                while not (self.pattern[:q] + char).endswith(self.pattern[:k]):
                    k -= 1
                transitions[(q, char)] = k

        return transitions


    # fa matcher
    def automata_matcher(self):     

        #load alphabet
        self.get_alphabet()

        # get transitions
        transitions = self.transition()
        q = 0
        
        for i in range(self.text_len):

            q = transitions[(q, self.text[i])]

            if q == self.pattern_len:
                print("index wystapienia :", i - self.pattern_len + 1)
               
