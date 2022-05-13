'''
DATA student;
INPUT result;

if result > 50 then group = "Pass";
else if result < 50 then group = "Fail";

DATALINES;
99
100
34
23
1
;
run;
PROC PRINT DATA = student;
run;

'''