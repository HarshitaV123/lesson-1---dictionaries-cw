userS=input("Enter a word or phrase?").lower()
c=0
for ch in userS:
    if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        c=c+1
print(f"The total number of vowels is {c}")