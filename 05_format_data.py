'''
DATA employee;
INPUT emp_name$ emp_salary;
FORMAT emp_name$ UPCASE10;
DATALINES;
shoeb 100000
vishal 999999
gaurav 800000
ashwin 100000
;
run;
PROC PRINT DATA = employee;
run;

'''