# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8];
contain = False

for i in numbers:
    if i == 7:
        contain = True

if contain:
    print("Hoorray")
else:
    print("Noooooo")