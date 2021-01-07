all: calculator.tab lex.l.c
	g++ -o calculator calculator.tab.cpp functions.cpp lex.l.c

lex.l.c: lex.l
	flex -o lex.l.c lex.l

calculator.tab: calculator.ypp
	bison -d calculator.ypp

clean:
	rm calculator.tab.* lex.l.*

cleanall: clean
	rm calculator
