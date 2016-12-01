demo:main.o svm.o
	g++ -o demo main.o svm.o
main.o:main.cpp svm.cpp
	g++ -c -o main.o main.cpp
test.o:svm.cpp svm.h
	gcc -c -o svm.o svm.cpp

clean:
	rm *.o
