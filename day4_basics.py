num = int(input("enter a number: "))
print(f"\n multiplication table of {num} is: ")
for i in range(1, 11):
    print(num, "x", i, "=", num*i)