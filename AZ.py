 
# az 97-122

for i in range(65, 91):
    print(chr(i),end=" ")
############################
def main():
    print("Alphabets from (A-Z) are:")
    # ASCII value of A=65 and Z=90
    for i in range(65, 91):
        # Integer i with chr() will be converted to character
        # before printing. chr() will take its equivalent
        # character value
        print(chr(i), end=" ")
 
    print("\nAlphabets from (a-z) are:")
    # ASCII value of a=97 and z=122
    for i in range(97, 123):
        # Integer i with chr() will be converted to character
        # before printing. chr() will take its equivalent
        # character value
        print(chr(i), end=" ")
 
 
if __name__ == "__main__":
    main()

# Python program to print
# Alphabets from A to Z

# Declare the variable
i = 'A'

# Display the alphabets
print "The Alphabets from A to Z are:"

# Traverse each character
# with the help of a while loop
while ord(i) <= ord('Z'):
	print i,
	i = chr(ord(i) + 1)

# Display the alphabets
i = 'a'

print "\nThe Alphabets from a to z are:"

while ord(i) <= ord('z'):
	print i,
	i = chr(ord(i) + 1)
