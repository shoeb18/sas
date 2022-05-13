'''
DATA string_program;
string1 = 'Hello ';
string2 = 'World';

joined_string = string1||string2;
run;
PROC PRINT DATA = string_program noobs;
run;

'''
