'''
DATA students;
INPUT s_roll s_name$;
DATALINES;
1 john
2 sunny
3 peter
4 sam
;
run;

DATA faculty;
INPUT s_roll s_faculty$;
DATALINES;
1 MBA
2 MBA
3 MBA
4 MBA
;
run;

DATA student_details;
MERGE students faculty;
BY s_roll;
run;

PROC PRINT DATA = student_details;
run;

'''