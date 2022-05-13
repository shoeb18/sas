'''
DATA array
INPUT l1$ l2$ l3$;
Array languages(3)$ l1-l3;
DATALINES;
c cpp java python
;
run;
PROC PRINT DATA = array;
run;

'''