'''
DATA programmers;
INPUT emp_id emp_name$ emp_salary;
DATALINES;
101 shoeb 10000
103 ashwin 65000
105 chetana 75000
;
run;

DATA designers;
INPUT emp_id emp_name$ emp_salary;
DATALINES;
102 vishal 99999
104 dipali 95000
106 gaurav 85000
;
run;

DATA all_employee;
SET programmers designers;
run;
PROC PRINT DATA = all_employee;
run;

'''