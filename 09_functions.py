'''
#**** String functions


DATA string_functions;
low_case = LOWCASE('HELLO WORLD');
up_case = UPCASE('hello world');
prop_case = PROPCASE('HELLO WORLD');
reverse_string = REVERSE('Hello');
Scan_First_letter = SCAN('Hello World',1);
run;
PROC PRINT DATA = string_functions noobs;
run;


#**** Mathematical functions

DATA maths_functions;

n1=23;
n2=56;
n3=78;
n4=18;
max_value = MAX(n1,n2,n3,n4);
min_value = MIN(n1,n2,n3,n4);
med_value = MEDIAN(n1,n2,n3,n4);
sqrt_value = SQRT(sum(n1,n2,n3,n4));
run;
PROC PRINT DATA = maths_functions noobs;
run;

'''