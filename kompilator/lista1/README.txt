
Wojciech Wróblewski 250349  lista1  lab jftt


W pliku kmp.py znajduje się implementacja algorytmu KMP(Knutha-Morrisa-Pratta).
Plik fa.py zawiera implementacje wyszukiwania wzorca z wykorzystaniem auto-matów skończonych.
Aby przetestować oba algorytmy uruchamiamy program matcher.py.


============================================================
przykładowe wywołanie dla algorytmu kmp 
============================================================
> python3 matcher.py KMP <pattern> <nazwa pliku z tekstem> 

gdy wzorcem jest "abc", a nazwa pliku z tekstem to "input.txt"

> python3 matcher.py KMP "abc" input.txt 


============================================================
przykładowe wywołanie dla algorytmu fa 
============================================================
> python3 matcher.py FA <pattern> <nazwa pliku z tekstem> 

gdy wzorcem jest "abc", a nazwa pliku z tekstem to "input.txt"

> python3 matcher.py FA "abc" input.txt 