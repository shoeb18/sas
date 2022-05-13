'''
#*** Do While Loop

DATA do_while;
salary = 50000;
purchase_items = 0;

do while(salary > 0);
salary = salary - 1000; 
purchase_items = purchase_item + 1;
end;
run;
PROC PRINT DATA = do_while;
run;


#*** Do Until Loop

DATA do_until;
salary = 50000;
purchase_items = 0;

do until(salary = 0);
salary = salary - 1000; 
purchase_items = purchase_item + 1;
end;
run;
PROC PRINT DATA = do_until;
run;

'''