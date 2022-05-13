'''
DATA Arithmetic_operators;
INPUT @1 N1 4.2 @7 N2 3.1;
addition_total = N1+N2;
subtract_total = N1-N2;
multiply_total = N1*N2;
division_total = N1/N2;
exponential_total = N1**N2;
DATALINES;
23.2 4.33
32.3 5.11
;
run;
PROC PRINT DATA = Arithmetic_operators;
run;

'''