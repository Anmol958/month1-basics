num = int(input("Enter a number to print all prime numbers up to it: "))
print(f"Prime numbers from 1 to {num}:")
for i in range(2, num+1):
    prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
print()
  
   