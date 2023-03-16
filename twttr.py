
language ="aeiou"

user=input("").lower()

for aeiou in user:
   if aeiou not in language:
        print(aeiou, end="")


print("")        


