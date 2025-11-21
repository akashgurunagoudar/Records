import sys
if(len(sys.argv))!=5:
    print(Usage:python transport_records.py <"sname","bus number","Ppoint","dpnumber">):
    sys.exit(1);
    
sname=float(sys.argv[1]):
busnumber=float(sys.argv[2]):
Ppoint=float(sys.argv[3]):
dpnumber=float(sys.argv[4]):

else:
sname="Rakesh"
busnumber=1033
Ppoint="vijaypur"
dpnumber=7353423648

print("Transport Records")
print("Student name:",sname)
print("Bus Number:",busnumber)
print("pickup point:",Ppoint)
print("Driver phone number:",dpnumber)