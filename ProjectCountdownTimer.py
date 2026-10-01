import time

strt = input("Enter starting time: ").strip()

while not strt.isdigit():
    print("Invalid value type. Use digits")
    strt = input("Enter starting time: ").strip()

strt = int(strt)

for i in range(strt, 0, -1):
    print(i)
    time.sleep(1)
    
print("LIFT OFF!")



#CHANGES: print("Lift off outside") -> The loop dies naturally as it hits 0. Then instantly shouts lift off

#PAST ver:for i in range(strt, -1, -1):
#    print(i)
 #   time.sleep(1)
 #   if i == 0:
  #      print("LIFT OFF!")