import sys

# Check if all required arguments are provided
if len(sys.argv) != 5:
    print("Usage: python records.py <sname> <busnumber> <Ppoint> <dpnumber>")
    sys.exit()

    sname = sys.argv[1]
    busnumber = sys.argv[2]
    Ppoint = sys.argv[3 ]
    dpnumber = sys.argv[4]

else :
     sname="Rakesh"
     busnumber="9567"
     Ppoint="vijaypur"
     dpnumber=671545355


print("=== Transport Records ===")
print(f"Student Name:{sname}")
print(f"Bus Number:{busnumber}")
print(f"Pickup Point:{Ppoint}")
print(f"Driver Phone No:{dpnumber}")
