''' 
DATA students;
input roll_no name$ class$;
DATALINES;
154 ashwin sybca
145 shoeb sybca
23 gaurav sybca
58 vishal sybca
80 chetana sybca
83 dipali sybca
;
run;
PROC SORT DATA = students;
by roll_no;
run;
PROC PRINT DATA = students;
run;

'''