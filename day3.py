x = float(input())
if (x % 2) != 0:
    print("Weird")
elif (x % 2) == 0 and x in range(2, 6):
    print("Not Weird")
elif (x % 2) == 0 and x in range(6, 21):
    print("Weird")
elif  (x % 2) == 0 and x > 20:
    print("Not Weird")

