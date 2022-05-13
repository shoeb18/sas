'''
DATA car
input car_model$ car_price;
DATALINES;
creta 1500000
thar 3000000
urus 45000000
fortuner 3500000
;
run;
proc print data = car;
run;

'''