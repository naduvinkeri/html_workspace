#leap year without using the modulus operator
def is_leap(year):
    i=4
    while i<=year:
        if i==year:
            return True
        i+=4
    return False


year = int(input("enter the year "))
if is_leap(year):
    print("leap year")
else:
    print("not leap year")
