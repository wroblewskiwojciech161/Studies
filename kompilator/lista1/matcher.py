
from kmp import KMP
from fa import AUTOMATA
import sys 


matcher = sys.argv[1]
pattern = sys.argv[2]
file = open(sys.argv[3],"r")
text=""
for a in file.read().splitlines():
    text+=a

if matcher == "KMP":
    
    print("wyszukiwanie wzorca za pomoca KMP")
    print("=================================")
    kmp = KMP(text, pattern)
    kmp.kmp()

else:

    print("wyszukiwanie wzorca za pomoca FA")
    print("================================")
    finite = AUTOMATA(text, pattern)
    finite.automata_matcher()



