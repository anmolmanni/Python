p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter commment :")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is spam")

else:
    print("not scam")